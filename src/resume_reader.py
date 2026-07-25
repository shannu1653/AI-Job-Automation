import fitz


def read_resume(resume_path):
    """
    Read a PDF resume and return its text.
    """

    document = fitz.open(resume_path)

    resume_text = ""

    for page in document:
        resume_text += page.get_text()

    document.close()

    return resume_text