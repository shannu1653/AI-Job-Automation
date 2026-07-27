"""
Configuration settings for the Job Search Automation module.
"""

# ==========================================
# JOB SEARCH SETTINGS
# ==========================================

# Search keywords
SEARCH_KEYWORDS = [
    "Python Fresher",
    "Python Developer Fresher",
    "Python Django Developer",
    "AI Python Intern",
    "Backend Python Developer",
]

# Search locations
SEARCH_LOCATIONS = [
    "Hyderabad",
]

# Maximum number of jobs to process
MAX_JOBS = 30

# Delay (seconds) between requests
REQUEST_DELAY = 3

# ==========================================
# SEARCH ENGINES
# ==========================================

USE_GOOGLE = True
USE_BING = True

# ==========================================
# TARGET WEBSITES
# ==========================================

TARGET_SITES = [
    "linkedin.com",
    "naukri.com",
    "indeed.com",
    "foundit.in",
    "wellfound.com",
    "internshala.com",
]