"""
Filter search results and keep only valid job URLs.
"""

from urllib.parse import urlparse


# Words that usually indicate a real job page
JOB_KEYWORDS = [
    "job",
    "jobs",
    "career",
    "careers",
    "vacancy",
    "vacancies",
    "hiring",
    "viewjob",
    "internship",
]

# Words we want to reject
BLOCK_KEYWORDS = [
    "youtube",
    "course",
    "training",
    "blog",
    "tutorial",
    "news",
    "salary",
    "interview-questions",
]


def is_valid_job_url(url: str) -> bool:
    """
    Return True if the URL looks like a job page.
    """

    url = url.lower()

    # Reject unwanted URLs
    for word in BLOCK_KEYWORDS:
        if word in url:
            return False

    # Accept URLs containing job-related words
    for word in JOB_KEYWORDS:
        if word in url:
            return True

    return False


def clean_urls(results):
    """
    Remove duplicate and unwanted URLs.
    """

    cleaned = []
    seen = set()

    for job in results:

        url = job["url"]

        # Remove query parameters
        parsed = urlparse(url)
        clean_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"

        if clean_url in seen:
            continue

        if not is_valid_job_url(clean_url):
            continue

        seen.add(clean_url)

        job["url"] = clean_url
        cleaned.append(job)

    return cleaned