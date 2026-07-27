# automation/company_website.py

from duckduckgo_search import DDGS
from urllib.parse import urlparse

BLOCKED_DOMAINS = {
    "linkedin.com",
    "indeed.com",
    "naukri.com",
    "glassdoor.com",
    "glassdoor.co.in",
    "ambitionbox.com",
    "wellfound.com",
    "bebee.com",
    "jobrapido.com",
    "jooble.org",
    "internshala.com",
    "placementindia.com",
    "foundit.in",
    "monsterindia.com",
    "shine.com",
    "timesjobs.com",
}


def is_blocked(url: str) -> bool:
    """
    Check whether a URL belongs to a blocked domain.
    """
    try:
        domain = urlparse(url).netloc.lower()

        if domain.startswith("www."):
            domain = domain[4:]

        for blocked in BLOCKED_DOMAINS:
            if domain == blocked or domain.endswith("." + blocked):
                return True

        return False

    except Exception:
        return True


def find_company_website(company_name: str):
    """
    Search the official website of a company.

    Returns:
        Official website URL
        or None
    """

    if not company_name:
        return None

    query = f"{company_name} official website"

    print(f"\nSearching official website for: {company_name}")

    try:

        with DDGS() as ddgs:

            results = ddgs.text(
                keywords=query,
                max_results=10,
            )

            for result in results:

                url = result.get("href")

                if not url:
                    continue

                if is_blocked(url):
                    continue

                print(f"Official Website Found: {url}")

                return url

    except Exception as e:
        print("Website Search Error:", e)

    return None


if __name__ == "__main__":

    company = input("Company Name: ")

    website = find_company_website(company)

    print("\nResult:", website)