def compare_skills(job_skills, resume_skills):
    job_set = set(job_skills)
    resume_set = set(resume_skills)

    matched = sorted(job_set & resume_set)
    missing = sorted(job_set - resume_set)

    if len(job_set) == 0:
        score = 0
    else:
        score = round((len(matched) / len(job_set)) * 100, 2)

    return matched, missing, score