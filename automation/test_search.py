from search_jobs import search_jobs

jobs = search_jobs()

print()

print("=" * 80)

print(f"Total Jobs Found : {len(jobs)}")

print("=" * 80)

for i, job in enumerate(jobs, start=1):

    print()

    print(f"{i}. {job['title']}")

    print(job["source"])

    print(job["url"])