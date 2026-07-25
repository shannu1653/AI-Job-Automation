def print_job_details(company, role, location, email, phone):
    print("\n" + "=" * 60)
    print("JOB DETAILS")
    print("=" * 60)

    print(f"Company : {company}")
    print(f"Role    : {role}")
    print(f"Location: {location}")
    print(f"Email   : {email}")
    print(f"Phone   : {phone}")


def print_job_skills(job_skills):
    print("\n" + "=" * 60)
    print("JOB SKILLS")
    print("=" * 60)

    if not job_skills:
        print("No skills found.")
        return

    for i, skill in enumerate(job_skills, start=1):
        print(f"{i}. {skill}")


def print_resume_skills(resume_skills):
    print("\n" + "=" * 60)
    print("RESUME SKILLS")
    print("=" * 60)

    if not resume_skills:
        print("No resume skills found.")
        return

    for i, skill in enumerate(resume_skills, start=1):
        print(f"{i}. {skill}")


def print_ats_report(score, matched, missing):
    print("\n" + "=" * 60)
    print("ATS MATCH REPORT")
    print("=" * 60)

    print(f"\nATS Match Score : {score}%")

    print("\nMatched Skills")

    if matched:
        for skill in matched:
            print(f"✓ {skill}")
    else:
        print("None")

    print("\nMissing Skills")

    if missing:
        for skill in missing:
            print(f"✗ {skill}")
    else:
        print("None")

import os

def save_ats_report(
    company,
    role,
    location,
    email,
    phone,
    job_skills,
    resume_skills,
    matched,
    missing,
    score
):
    os.makedirs("outputs", exist_ok=True)

    file_path = "outputs/ATS_Report.txt"

    with open(file_path, "w", encoding="utf-8") as file:

        file.write("=" * 60 + "\n")
        file.write("AI JOB APPLICATION AUTOMATION REPORT\n")
        file.write("=" * 60 + "\n\n")

        file.write("JOB DETAILS\n")
        file.write("-" * 40 + "\n")
        file.write(f"Company : {company}\n")
        file.write(f"Role    : {role}\n")
        file.write(f"Location: {location}\n")
        file.write(f"Email   : {email}\n")
        file.write(f"Phone   : {phone}\n\n")

        file.write("JOB SKILLS\n")
        file.write("-" * 40 + "\n")

        for skill in job_skills:
            file.write(f"- {skill}\n")

        file.write("\n")

        file.write("RESUME SKILLS\n")
        file.write("-" * 40 + "\n")

        for skill in resume_skills:
            file.write(f"- {skill}\n")

        file.write("\n")

        file.write(f"ATS MATCH SCORE : {score}%\n\n")

        file.write("MATCHED SKILLS\n")
        file.write("-" * 40 + "\n")

        for skill in matched:
            file.write(f"✓ {skill}\n")

        file.write("\n")

        file.write("MISSING SKILLS\n")
        file.write("-" * 40 + "\n")

        for skill in missing:
            file.write(f"✗ {skill}\n")

    return file_path