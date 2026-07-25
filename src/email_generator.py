def generate_email(job, applicant_name="Shanmukha Penta"):
    """
    Generate a dynamic email subject and body.
    """

    company = job.get("company") or "Your Company"
    role = job.get("role") or "Software Developer"
    location = job.get("location") or ""
    skills = ", ".join(job.get("skills", []))

    subject = f"Application for {role}"

    body = f"""Dear Hiring Team,

I hope you are doing well.

I am writing to apply for the {role} position at {company}.

I have skills in {skills}. I am enthusiastic about learning new technologies and contributing to your team.

Please find my resume attached for your consideration.

Thank you for your time and consideration. I look forward to hearing from you.

Regards,
{applicant_name}
"""

    return subject, body