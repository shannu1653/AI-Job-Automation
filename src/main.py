import traceback

from input_handler import get_job_description
from parser import parse_job_description
from resume_reader import read_resume
from ai_email_generator import generate_email
from email_sender import send_email
from database import create_database, save_application

from config import (
    NAME,
    TITLE,
    PHONE,
    EMAIL,
    LINKEDIN,
    GITHUB,
    PORTFOLIO,
)

# ==========================================================
# CONFIGURATION
# ==========================================================

RESUME_PATH = "resume/Shanmukha_Resume.pdf"

SIGNATURE = f"""Best Regards,

{NAME}
{TITLE}
📞 {PHONE}
📧 {EMAIL}
🔗 LinkedIn: {LINKEDIN}
💻 GitHub: {GITHUB}
🌐 Portfolio: {PORTFOLIO}
"""


# ==========================================================
# NORMALIZE JOB DATA (NEW)
# ==========================================================

def normalize_job(job):
    """
    Fill missing fields so the AI can always generate
    a professional email.
    """

    # Email is mandatory
    job["email"] = (job.get("email") or "").strip()

    # Company
    if not job.get("company"):
        if job["email"] and "@" in job["email"]:
            domain = job["email"].split("@")[1].split(".")[0]
            job["company"] = domain.title()
        else:
            job["company"] = "Hiring Company"

    # Role
    if not job.get("role"):
        skills = [s.lower() for s in job.get("skills", [])]

        if "django" in skills or "fastapi" in skills:
            job["role"] = "Python Developer"

        elif "react" in skills:
            job["role"] = "Frontend Developer"

        elif "java" in skills:
            job["role"] = "Java Developer"

        elif "sql" in skills:
            job["role"] = "Software Developer"

        else:
            job["role"] = "Software Professional"

    # Optional fields
    job["location"] = job.get("location") or "Not Mentioned"
    job["phone"] = job.get("phone") or "Not Mentioned"

    return job


# ==========================================================
# UI
# ==========================================================

def print_header():
    print("=" * 70)
    print("🤖 AI JOB APPLICATION AUTOMATION SYSTEM".center(70))
    print("=" * 70)


# ==========================================================
# MAIN
# ==========================================================

def main():

    print_header()

    create_database()

    job_description = get_job_description()

    if not job_description:
        print("❌ No job description found.")
        return

    print("\n" + "=" * 70)
    print("📋 CLIPBOARD CONTENT")
    print("=" * 70)
    print(job_description)
    print("=" * 70)

    # Parse
    job = parse_job_description(job_description)

    # NEW
    job = normalize_job(job)

    print("\n📌 PARSED JOB DETAILS")
    print("-" * 70)
    print(f"Company : {job.get('company')}")
    print(f"Role    : {job.get('role')}")
    print(f"Email   : {job.get('email')}")
    print(f"Phone   : {job.get('phone')}")
    print("-" * 70)

    if not job["email"]:
        print("\n❌ Recruiter email not found.")
        return

    resume_text = read_resume(RESUME_PATH)

    print("\n🤖 Generating AI Email...\n")

    email_body = generate_email(job, resume_text)

    unwanted = [
        "Here is the rewritten job application email:",
        "Here is a professional job application email:",
        "Here is the professional email:",
        "Here is the email:",
        "Best Regards,",
        "Best regards,",
        "Regards,",
        "Sincerely,"
    ]

    for text in unwanted:
        email_body = email_body.replace(text, "")

    email_body = email_body.strip()
    email_body += "\n\n" + SIGNATURE

    subject = f"Application for {job['role']}"

    print("\n📧 Sending Email To:", job["email"])

    try:

        send_email(
            to_email=job["email"],
            subject=subject,
            body=email_body,
            resume_path=RESUME_PATH,
        )

        save_application(job, "Sent")

        print("\n" + "=" * 70)
        print("🎉 APPLICATION SENT SUCCESSFULLY!".center(70))
        print("=" * 70)
        print(f"🏢 Company : {job['company']}")
        print(f"💼 Role    : {job['role']}")
        print(f"📧 Email   : {job['email']}")
        print("📌 Status  : Sent Successfully ✅")

    except Exception:

        print("\n❌ Failed to send email.\n")
        traceback.print_exc()

        try:
            save_application(job, "Failed")
        except Exception:
            pass


if __name__ == "__main__":
    main()