import pyperclip


def get_job_description():
    print("\n📋 Reading Job Description from Clipboard...")

    job_description = pyperclip.paste().strip()

    if not job_description:
        print("❌ Clipboard is empty.")
        return ""

    print("\n========== CLIPBOARD CONTENT ==========\n")
    print(job_description)
    print("\n=======================================\n")

    return job_description