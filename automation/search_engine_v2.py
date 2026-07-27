from ddgs import DDGS

SEARCH_QUERIES = [
    # Direct email opportunities
    'Python Developer Hyderabad "send resume"',
    'Python Developer Hyderabad "apply by email"',
    'Python Developer Hyderabad "hr@"',
    'Python Developer Hyderabad "jobs@"',
    'Python Developer Hyderabad "careers@"',

    'Python Fresher Hyderabad "send resume"',
    'Python Fresher Hyderabad "apply by email"',
    'Python Fresher Hyderabad "hr@"',

    'Django Developer Hyderabad "send resume"',
    'Backend Python Hyderabad "send resume"',
    'Python Intern Hyderabad "send resume"',

    # Company career pages
    "site:careers.* Python Developer Hyderabad",
    "site:company.* careers Python Hyderabad",
]

BAD_DOMAINS = {
    "linkedin.com",
    "indeed.com",
    "glassdoor.com",
    "jooble.org",
    "naukri.com",
    "monsterindia.com",
    "shine.com",
    "foundit.in",
    "internshala.com",
    "placementindia.com",
    "freshersworld.com",
    "youtube.com",
    "facebook.com",
    "instagram.com",
}

BAD_KEYWORDS = [
    "course",
    "training",
    "tutorial",
    "salary",
    "interview",
    "blog",
    "news",
]


from ddgs import DDGS

BAD_DOMAINS = {
    "linkedin.com",
    "indeed.com",
    "glassdoor.com",
    "jooble.org",
    "naukri.com",
    "monsterindia.com",
    "shine.com",
    "foundit.in",
    "internshala.com",
    "placementindia.com",
    "freshersworld.com",
    "youtube.com",
    "facebook.com",
    "instagram.com",
}

BAD_KEYWORDS = [
    "course",
    "training",
    "tutorial",
    "salary",
    "interview",
    "blog",
    "news",
]


def search_jobs(search_query, limit=20):
    urls = set()

    with DDGS() as ddgs:

        print(f"\nSearching: {search_query}")

        try:
            results = ddgs.text(
                search_query,
                region="in-en",
                safesearch="off",
                max_results=limit,
            )

            for result in results:

                url = result.get("href")

                if not url:
                    continue

                lower = url.lower()

                if any(domain in lower for domain in BAD_DOMAINS):
                    continue

                if any(word in lower for word in BAD_KEYWORDS):
                    continue

                urls.add(url)

        except Exception as e:
            print(f"Search Error: {e}")

    return list(urls)