import os

print("=" * 60)
print("CAPGEMINI CAREERS DATA EXTRACTION PROJECT")
print("=" * 60)

os.system("python src/scrape_jobs.py")
os.system("python src/skills_analysis.py")
os.system("python src/keyword_analysis.py")

print("\nAll scenarios completed successfully.")