from textwrap import dedent

# ----------------------------------------------------
# Your Details
# ----------------------------------------------------

YOUR_NAME = "Shanmukha Penta"

YOUR_ROLE = "Python Full Stack Developer"

YOUR_EMAIL = "pentashanmukha2002@gmail.com"

YOUR_PHONE = "+91-8096085857"

YOUR_GITHUB = "https://github.com/shannu1653"

YOUR_LINKEDIN = "https://www.linkedin.com/in/shanmukhapenta/"

YOUR_PORTFOLIO = "https://shanmukha-portfolio-three.vercel.app/"


# ----------------------------------------------------
# Subject Generator (Optional)
# ----------------------------------------------------

def generate_subject(job):
    role = job.get("role", "Software Developer")

    if not role:
        role = "Software Developer"

    role = role.strip()

    if len(role) > 60:
        role = "Software Developer"

    return f"Application for {role}"


# ----------------------------------------------------
# Email Body Generator
# ----------------------------------------------------

def generate_body(job):

    company = job.get("company", "your company")

    role = job.get("role", "Software Developer")

    skills = job.get("skills", [])

    if isinstance(skills, list) and skills:
        skill_text = ", ".join(skills)
    else:
        skill_text = (
            "Python, Django, REST APIs, MySQL, HTML, CSS, "
            "JavaScript, Bootstrap, Git"
        )

    body = f"""
Dear Hiring Team,

I hope you are doing well.

I am writing to express my interest in the {role} position at {company}.

I recently completed my Master of Computer Applications (MCA) and I am actively seeking an opportunity as a Python Full Stack Developer.

My technical skills include:

{skill_text}

I have worked on projects involving:

• Python
• Django
• Django REST Framework
• React
• MySQL
• REST APIs
• Authentication (JWT)
• Git & GitHub
• HTML, CSS, Bootstrap, JavaScript

Please find my resume attached for your review.

I would be grateful for the opportunity to discuss how my skills and enthusiasm can contribute to your team.

Thank you for your time and consideration.

Best Regards,

{YOUR_NAME}
{YOUR_ROLE}

Email: {YOUR_EMAIL}

Phone: {YOUR_PHONE}

GitHub:
{YOUR_GITHUB}

LinkedIn:
{YOUR_LINKEDIN}

Portfolio:
{YOUR_PORTFOLIO}
"""

    return dedent(body).strip()


# ----------------------------------------------------
# Main Function
# ----------------------------------------------------

def generate_email(job, resume_text=None):
    """
    Returns ONLY the email body.

    This is compatible with your current auto_apply.py
    """

    return generate_body(job)