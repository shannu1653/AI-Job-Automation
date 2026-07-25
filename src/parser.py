import re
from skills import SKILLS


def clean(text):
    if not text:
        return None
    return " ".join(text.strip().split())


def search(pattern, text):
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        return clean(match.group(1))
    return None


def parse_job_description(job_text):
    data = {
        "company": None,
        "role": None,
        "email": None,
        "phone": None,
        "location": None,
        "experience": None,
        "education": [],
        "skills": [],
        "salary": None,
        "job_type": None,
        "work_mode": None,
        "deadline": None,
    }

    lower = job_text.lower()

    # ----------------------------------------------------
    # EMAIL
    # ----------------------------------------------------

    email = re.search(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        job_text,
    )

    if email:
        data["email"] = email.group()

    # ----------------------------------------------------
    # PHONE
    # ----------------------------------------------------

    phone = re.search(
        r"(?:\+91[- ]?)?[6-9]\d{9}",
        job_text,
    )

    if phone:
        data["phone"] = phone.group()

    # ----------------------------------------------------
    # COMPANY
    # ----------------------------------------------------

    company_patterns = [
        r"Company\s*[:\-]\s*(.+)",
        r"Company Name\s*[:\-]\s*(.+)",
        r"Organization\s*[:\-]\s*(.+)",
        r"Client\s*[:\-]\s*(.+)",
        r"([A-Z][A-Za-z0-9 &().,-]+)\s+is hiring",
        r"Join\s+([A-Z][A-Za-z0-9 &().,-]+)",
    ]

    for pattern in company_patterns:
        value = search(pattern, job_text)
        if value:
            data["company"] = value
            break

    # Fallback from email
    if not data["company"] and data["email"]:
        domain = data["email"].split("@")[1].split(".")[0]
        data["company"] = domain.title()

    # ----------------------------------------------------
    # ROLE
    # ----------------------------------------------------

    role_patterns = [
        r"Role\s*[:\-]\s*(.+)",
        r"Position\s*[:\-]\s*(.+)",
        r"Job Title\s*[:\-]\s*(.+)",
        r"Hiring\s+for\s+(.+)",
        r"We are hiring\s+(.+)",
        r"Looking for\s+(.+)",
    ]

    for pattern in role_patterns:
        value = search(pattern, job_text)
        if value:
            data["role"] = value
            break

    common_roles = [
        "Python Full Stack Developer",
        "Backend Python Developer",
        "Python Developer",
        "Full Stack Developer",
        "Django Developer",
        "Backend Developer",
        "Frontend Developer",
        "Java Full Stack Developer",
        "Java Developer",
        "Software Engineer",
        "Software Developer",
        "React Developer",
        "Data Analyst",
        "AI Engineer",
        "ML Engineer",
    ]

    if not data["role"]:
        for role in common_roles:
            if role.lower() in lower:
                data["role"] = role
                break

    if not data["role"]:
        data["role"] = "Software Developer"

    # ----------------------------------------------------
    # LOCATION
    # ----------------------------------------------------

    location_patterns = [
        r"Location\s*[:\-]\s*(.+)",
        r"Work Location\s*[:\-]\s*(.+)",
        r"Based in\s*(.+)",
    ]

    for pattern in location_patterns:
        value = search(pattern, job_text)
        if value:
            data["location"] = value
            break

    # ----------------------------------------------------
    # EXPERIENCE
    # ----------------------------------------------------

    exp = re.search(
        r"Freshers?|Fresher|\d+\+?\s*Years?|\d+\s*(?:-|to)\s*\d+\s*Years?",
        job_text,
        re.IGNORECASE,
    )

    if exp:
        data["experience"] = exp.group()

    # ----------------------------------------------------
    # EDUCATION
    # ----------------------------------------------------

    education = [
        "B.Tech",
        "B.E",
        "M.Tech",
        "MCA",
        "BCA",
        "B.Sc",
        "M.Sc",
        "Graduate",
        "Bachelor",
        "Master",
    ]

    data["education"] = sorted(
        [
            e
            for e in education
            if e.lower() in lower
        ]
    )

    # ----------------------------------------------------
    # SKILLS
    # ----------------------------------------------------

    data["skills"] = sorted(
        [
            skill
            for skill in SKILLS
            if skill.lower() in lower
        ]
    )

    # ----------------------------------------------------
    # SALARY
    # ----------------------------------------------------

    salary_patterns = [
        r"Salary\s*[:\-]\s*(.+)",
        r"CTC\s*[:\-]\s*(.+)",
        r"Package\s*[:\-]\s*(.+)",
    ]

    for pattern in salary_patterns:
        value = search(pattern, job_text)
        if value:
            data["salary"] = value
            break

    # ----------------------------------------------------
    # JOB TYPE
    # ----------------------------------------------------

    job_types = [
        "Full-Time",
        "Internship",
        "Contract",
        "Part Time",
        "Freelance",
    ]

    for jt in job_types:
        if jt.lower() in lower:
            data["job_type"] = jt
            break

    # ----------------------------------------------------
    # WORK MODE
    # ----------------------------------------------------

    work_modes = [
        "Remote",
        "Hybrid",
        "Onsite",
        "Work From Home",
    ]

    for wm in work_modes:
        if wm.lower() in lower:
            data["work_mode"] = wm
            break

    # ----------------------------------------------------
    # DEADLINE
    # ----------------------------------------------------

    deadline_patterns = [
        r"Last Date\s*[:\-]\s*(.+)",
        r"Apply Before\s*[:\-]\s*(.+)",
        r"Deadline\s*[:\-]\s*(.+)",
    ]

    for pattern in deadline_patterns:
        value = search(pattern, job_text)
        if value:
            data["deadline"] = value
            break

    return data