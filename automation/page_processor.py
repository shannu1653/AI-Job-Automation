"""
Page Processor

Downloads a webpage and extracts clean text
ready for AI analysis.
"""

import re

import requests
from bs4 import BeautifulSoup

from automation.logger import logger

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 "
        "(Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/138.0 Safari/537.36"
    )
}


REMOVE_WORDS = [
    "Login",
    "Register",
    "Menu",
    "Facebook",
    "WhatsApp",
    "Telegram",
    "Twitter",
    "LinkedIn",
    "Privacy Policy",
    "Terms",
    "Cookie",
    "Advertisement",
    "Sponsored",
    "Upgrade to Premium",
    "Notifications",
    "Share",
]


def clean_text(text: str) -> str:
    """
    Clean extracted webpage text.
    """

    for word in REMOVE_WORDS:
        text = text.replace(word, "")

    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+", " ", text)

    return text.strip()


def process_page(url: str):
    """
    Download webpage and return cleaned text.
    """

    logger.info(f"Processing: {url}")

    response = requests.get(
        url,
        headers=HEADERS,
        timeout=15,
    )

    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    for tag in soup([
        "script",
        "style",
        "noscript",
        "svg",
        "footer",
        "nav",
        "header",
        "aside",
    ]):
        tag.decompose()

    text = "\n".join(
        line.strip()
        for line in soup.get_text(separator="\n").splitlines()
        if line.strip()
    )

    return clean_text(text)