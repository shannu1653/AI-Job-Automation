import re
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

# ==========================================================
# Browser Headers
# ==========================================================

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/138.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "*/*",
    "Connection": "keep-alive",
}

# ==========================================================
# Email Regex
# ==========================================================

EMAIL_REGEX = re.compile(
    r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
)

# ==========================================================
# Preferred recruiter keywords
# ==========================================================

GOOD_KEYWORDS = [
    "hr",
    "career",
    "careers",
    "job",
    "jobs",
    "recruit",
    "recruitment",
    "talent",
    "talentacquisition",
    "hiring",
    "staffing",
]

# ==========================================================
# Ignore these emails
# ==========================================================

BAD_KEYWORDS = [
    "support",
    "admin",
    "privacy",
    "legal",
    "security",
    "help",
    "billing",
    "abuse",
    "noreply",
    "no-reply",
    "donotreply",
    "webmaster",
]

# ==========================================================
# Pages to search
# ==========================================================

COMMON_PATHS = [

    "/contact",

    "/contact-us",

    "/careers",

    "/career",

    "/jobs",

    "/join-us",

    "/about",

    "/about-us",

    "/team",

]

# ==========================================================
# Job Aggregator Domains
# ==========================================================

AGGREGATOR_DOMAINS = [

    "jobringer.com",

    "noticebard.com",

    "linkedin.com",

    "naukri.com",

    "foundit.in",

    "monsterindia.com",

    "indeed.com",

    "freshersworld.com",

    "internshala.com",

    "shine.com",

]

# ==========================================================
# Base URL
# ==========================================================

def get_base_url(url):

    parsed = urlparse(url)

    return f"{parsed.scheme}://{parsed.netloc}"

# ==========================================================
# Download Page
# ==========================================================

def download_page(url):

    try:

        response = requests.get(

            url,

            headers=HEADERS,

            timeout=15,

            allow_redirects=True,

        )

        response.raise_for_status()

        return response.text

    except Exception as e:

        print(f"Download failed: {url}")

        return None

# ==========================================================
# Email Extraction
# ==========================================================

def extract_emails(html):

    if not html:

        return []

    soup = BeautifulSoup(html, "html.parser")

    emails = set()

    # ------------------------------------------------------
    # Visible Text
    # ------------------------------------------------------

    text = soup.get_text(" ", strip=True)

    for email in EMAIL_REGEX.findall(text):

        emails.add(email.lower())

    # ------------------------------------------------------
    # mailto:
    # ------------------------------------------------------

    for tag in soup.find_all("a", href=True):

        href = tag["href"]

        if href.startswith("mailto:"):

            email = href.replace("mailto:", "").split("?")[0]

            emails.add(email.lower())

    # ------------------------------------------------------
    # Hidden HTML attributes
    # ------------------------------------------------------

    attrs = [

        "data-email",

        "data-mail",

        "data-contact",

        "content",

    ]

    for tag in soup.find_all():

        for attr in attrs:

            value = tag.get(attr)

            if not value:

                continue

            found = EMAIL_REGEX.findall(value)

            for email in found:

                emails.add(email.lower())

    return sorted(emails)

# ==========================================================
# Email Scoring
# ==========================================================

def score_email(email):
    """
    Higher score = better recruiter email
    """

    email = email.lower()

    username = email.split("@")[0]

    score = 0

    # Prefer HR usernames
    for word in GOOD_KEYWORDS:
        if username.startswith(word):
            score += 50
        elif word in username:
            score += 20

    # Penalize generic/support emails
    for word in BAD_KEYWORDS:
        if word in username:
            score -= 100

    # Small bonus for company domains
    if not email.endswith("@gmail.com"):
        score += 5

    if not email.endswith("@yahoo.com"):
        score += 5

    if not email.endswith("@hotmail.com"):
        score += 5

    return score


# ==========================================================
# Aggregator Detection
# ==========================================================

def is_aggregator(url):

    domain = urlparse(url).netloc.lower()

    if domain.startswith("www."):
        domain = domain[4:]

    for site in AGGREGATOR_DOMAINS:

        if site in domain:
            return True

    return False


# ==========================================================
# Remove Duplicate Emails
# ==========================================================

def unique_emails(emails):

    cleaned = []

    seen = set()

    for email in emails:

        email = email.lower().strip()

        if email not in seen:

            cleaned.append(email)

            seen.add(email)

    return cleaned


# ==========================================================
# Filter Recruiter Emails
# ==========================================================

def filter_recruiter_emails(emails):

    if not emails:
        return []

    emails = unique_emails(emails)

    emails.sort(
        key=score_email,
        reverse=True,
    )

    valid = []

    for email in emails:

        if score_email(email) >= 0:
            valid.append(email)

    return valid


# ==========================================================
# Company Domain
# ==========================================================

def get_company_domain(url):

    domain = urlparse(url).netloc.lower()

    if domain.startswith("www."):
        domain = domain[4:]

    return domain


# ==========================================================
# Print Emails (Debug)
# ==========================================================

def print_found_emails(emails):

    if not emails:

        print("No emails found.")

        return

    print("\nEmails Found:")

    for email in emails:

        print(f"   {email}  Score={score_email(email)}")

def find_company_email(website_url):
    """
    Find the best recruiter email from a company website.
    """

    print(f"\nSearching company pages: {website_url}")

    html = download_page(website_url)

    if not html:
        print("Unable to download page.")
        return None

    emails = extract_emails(html)

    emails = filter_recruiter_emails(emails)

    if emails:
        print(f"Recruiter Email Found: {emails[0]}")
        return emails[0]

    base = get_base_url(website_url)

    for path in COMMON_PATHS:

        url = urljoin(base, path)

        print(f"Checking: {url}")

        html = download_page(url)

        if not html:
            continue

        emails = extract_emails(html)

        emails = filter_recruiter_emails(emails)

        if emails:
            print(f"Recruiter Email Found: {emails[0]}")
            return emails[0]

    print("No recruiter email found.")

    return None