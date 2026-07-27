from pathlib import Path

from automation.logger import logger
from automation.page_processor import process_page
from automation.storage import already_searched, add_searched_url
from automation.filter import should_skip
from automation.parser_v2 import parse_job_description
from automation.validator import validate_job
from automation.email_generator_v2 import generate_email
from automation.search_engine_v2 import search_jobs
from automation.company_website import find_company_website
from automation.company_finder import find_company_email

from src.resume_reader import read_resume
from src.email_sender import send_email
from src.database import save_application


# Resume location
PROJECT_ROOT = Path(__file__).resolve().parent.parent
RESUME_PATH = PROJECT_ROOT / "resume" / "Shanmukha_Resume.pdf"

print("Resume Path:", RESUME_PATH)
print("Exists:", RESUME_PATH.exists())


def apply_to_job(url):
    logger.info("=" * 60)

    # ---------------------------------
    # Skip blocked domains
    # ---------------------------------
    skip, reason = should_skip(url)

    if skip:
        logger.info(f"Skipped: {reason}")
        return

    logger.info(f"Processing: {url}")

    # ---------------------------------
    # Skip duplicate URLs
    # ---------------------------------
    # if already_searched(url):
    #     logger.info("Already processed.")
    #     return

    # add_searched_url(url)

    # ---------------------------------
    # Download page
    # ---------------------------------
    job_text = process_page(url)

    if not job_text:
        logger.warning("Unable to download page.")
        return

    # ---------------------------------
    # Parse job description
    # ---------------------------------
    job = parse_job_description(job_text)

    if not job:
        logger.warning("Unable to parse job.")
        return

    # ---------------------------------
    # Find recruiter email
    # ---------------------------------
    if not job.get("recruiter_email"):

        # Try directly from current URL
        email = find_company_email(url)

        # If not found, search company website
        if not email and job.get("company"):

            website = find_company_website(job["company"])

            if website:
                email = find_company_email(website)

        if email:
            job["recruiter_email"] = email

    # ---------------------------------
    # Print parsed job
    # ---------------------------------
    print("\n========== JOB ==========")

    for key, value in job.items():
        print(f"{key}: {value}")

    print("=========================\n")

    # ---------------------------------
    # Validate Job
    # ---------------------------------
    valid, reason = validate_job(job)

    if not valid:
        logger.warning(f"Validation Failed: {reason}")
        return

    recruiter_email = job.get("recruiter_email")

    if not recruiter_email:
        logger.warning("Recruiter email not found.")
        return

    # ---------------------------------
    # Read Resume
    # ---------------------------------
    resume_text = read_resume(str(RESUME_PATH))

    # ---------------------------------
    # Generate Email
    # ---------------------------------
    email_body = generate_email(job, resume_text)

    subject = f"Application for {job.get('role', 'Software Engineer')}"

    # ---------------------------------
    # Send Email
    # ---------------------------------
    send_email(
        recruiter_email,
        subject,
        email_body,
        str(RESUME_PATH),
    )

    # ---------------------------------
    # Save to database
    # ---------------------------------
    save_application(job, "Sent")

    logger.info("Application Sent Successfully")
    logger.info("=" * 60)


def run():
    jobs = search_jobs("Python Developer Hyderabad")

    for url in jobs:
        apply_to_job(url)


if __name__ == "__main__":
    run()