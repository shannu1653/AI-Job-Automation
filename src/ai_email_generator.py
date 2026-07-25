from ollama import chat


def generate_email(job, resume_text):
    """
    Generate a professional job application email using Ollama.
    """

    # Use only the first 500 characters for faster generation
    resume_summary = resume_text[:500]

    prompt = f"""
Write ONLY the email body.

Instructions:

1. Start EXACTLY with:
Dear Hiring Manager,

2. Do NOT write:
- Here is the rewritten job application email
- Here is the professional job application email
- Here is the email
- Any heading before the greeting

3. Mention the job role and company naturally.

4. Highlight only the most relevant skills from the resume.

5. Keep the email between 100 and 140 words.

6. End EXACTLY with this sentence:
Thank you for your time and consideration. I look forward to hearing from you.

7. Stop immediately after the above sentence.

8. Do NOT include:
- Best Regards
- Regards
- Sincerely
- Signature
- Name
- Phone Number
- Email Address
- LinkedIn
- GitHub
- Portfolio

Job Role:
{job.get("role", "")}

Company:
{job.get("company", "")}

Resume Summary:
{resume_summary}
"""

    try:
        response = chat(
            model="llama3.2:1b",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            options={
                "temperature": 0.2,
                "num_predict": 180,
                "num_ctx": 1024,
            },
        )

        email = response.message.content.strip()

        # Remove unwanted text if the model generates it
        unwanted = [
            "Here is the rewritten job application email:",
            "Here is a professional job application email:",
            "Here is the professional email:",
            "Here is the email:",
            "Here is your email:",
            "Best Regards,",
            "Best regards,",
            "Regards,",
            "Sincerely,",
        ]

        for text in unwanted:
            email = email.replace(text, "")

        email = email.strip()

        # Ensure the email ends correctly
        ending = (
            "Thank you for your time and consideration. "
            "I look forward to hearing from you."
        )

        if ending not in email:
            email = email.rstrip(". \n")
            email += "\n\n" + ending

        return email

    except Exception:
        return (
            "Dear Hiring Manager,\n\n"
            f"I am writing to express my interest in the "
            f"{job.get('role', 'Python Developer')} position at "
            f"{job.get('company', 'your company')}. "
            "As an MCA graduate with hands-on experience in Python, Django, "
            "REST APIs, MySQL, and full-stack development, I am confident in my "
            "ability to contribute effectively to your team.\n\n"
            "Please find my resume attached for your review.\n\n"
            "Thank you for your time and consideration. "
            "I look forward to hearing from you."
        )