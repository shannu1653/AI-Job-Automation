"""
Downloads a web page and extracts readable text.
"""

import requests
from bs4 import BeautifulSoup

from automation.logger import logger


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/138.0 Safari/537.36"
    )
}


def download_page(url: str) -> str | None:
    """
    Download a webpage and return clean text.
    """

    try:
        logger.info(f"Downloading: {url}")

        response = requests.get(
            url,
            headers=HEADERS,
            timeout=15,
        )

        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Remove unwanted tags
        for tag in soup(["script", "style", "noscript"]):
            tag.decompose()

        text = "\n".join(
            line.strip()
            for line in soup.get_text(separator="\n").splitlines()
            if line.strip()
        )

        logger.info("Download completed")

        return text

    except Exception as e:
        logger.error(f"Download failed: {e}")
        return None