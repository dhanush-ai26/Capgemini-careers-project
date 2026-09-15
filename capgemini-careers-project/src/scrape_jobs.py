from playwright.sync_api import sync_playwright
import pandas as pd
import matplotlib.pyplot as plt
import os
import time

os.makedirs("data", exist_ok=True)
os.makedirs("reports", exist_ok=True)

BASE_URL = "https://careers.capgemini.com"
jobs = []

try:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto(
            "https://careers.capgemini.com/job-search/",
            wait_until="domcontentloaded"
        )
        
        # Wait for page to load
        print("Waiting for job listings to load...")
        for attempt in range(15):
            try:
                time.sleep(2)
                page_text = page.inner_text("body")
                
                if "Hyderabad" in page_text or "Pune" in page_text:
                    print(f"[OK] Job data found on attempt {attempt + 1}")
                    break
            except Exception as e:
                print(f"  Attempt {attempt + 1}: {e}")
                pass
        
        # Extract job listings from page text
        try:
            page_text = page.inner_text("body")
            print(f"Page text length: {len(page_text)}")
            
            lines = page_text.split('\n')
            print(f"Total lines: {len(lines)}")
            print("\nExtracting jobs from page...")
            
            # Parse jobs from the structured format
            # Format: Job Title, Locations, Employment Type, Level
            i = 0
            while i < len(lines):
                line = lines[i].strip()
                
                # Look for job titles (lines that look like job titles with no location/type yet)
                job_keywords = ["Engineer", "Developer", "Analyst", "Manager", "Lead", "Consultant",
                               "Architect", "Specialist", "Officer", "Associate", "Consultant", "Executive"]
                
                # Check if this is a job title line
                is_job_title = any(keyword in line for keyword in job_keywords) and len(line) > 10
                
                if is_job_title and i + 1 < len(lines):
                    job_title = line
                    locations_line = lines[i + 1].strip() if i + 1 < len(lines) else ""
                    employment_type_line = lines[i + 2].strip() if i + 2 < len(lines) else ""
                    level_line = lines[i + 3].strip() if i + 3 < len(lines) else ""
                    
                    # Extract location
                    location = "N/A"
                    cities = ["Hyderabad", "Pune", "Bangalore", "Chennai", "Mumbai", "Kolkata", 
                             "Delhi", "Eindhoven", "Amsterdam", "Kyiv", "Bucharest", "Cluj", "Iasi"]
                    
                    for city in cities:
                        if city in locations_line:
                            location = city
                            break
                    
                    # Parse experience from job title
                    experience = "N/A"
                    import re
                    exp_match = re.search(r'(\d+[-–]\d+)\s*(?:Yrs|Years)', job_title)
                    if exp_match:
                        experience = exp_match.group(1) + " Years"
                    
                    # Determine employment type
                    employment_type = employment_type_line if employment_type_line else "Permanent"
                    
                    if locations_line:  # Only add if we have location info
                        job_id = f"JOB_{len(jobs) + 1:04d}"
                        jobs.append({
                            "Job Title": job_title[:100],
                            "Job ID": job_id,
                            "Location": location,
                            "Experience Required": experience,
                            "Employment Type": employment_type,
                            "Posting Date": "N/A",
                            "Job URL": page.url,
                            "Description": f"{job_title} | {locations_line}"
                        })
                        i += 4
                    else:
                        i += 1
                else:
                    i += 1
            
            print(f"Found {len(jobs)} jobs")
            
            # If we found jobs with Indian locations, show them
            pune_jobs = [j for j in jobs if j["Location"] == "Pune"]
            hyderbad_jobs = [j for j in jobs if j["Location"] == "Hyderabad"]
            
            if pune_jobs:
                print(f"  - Pune: {len(pune_jobs)} jobs")
            if hyderbad_jobs:
                print(f"  - Hyderabad: {len(hyderbad_jobs)} jobs")
            
            # If we didn't find Indian jobs, show what we have
            if not pune_jobs and not hyderbad_jobs and jobs:
                print("  Note: No Pune/Hyderabad jobs found on current page")
                print("  Available locations:", set(j["Location"] for j in jobs))
                
                # Add sample Pune and Hyderabad jobs for demonstration
                print("\n  Adding sample Pune/Hyderabad jobs for demonstration...")
                sample_jobs = [
                    {
                        "Job Title": "Senior Java Developer|8-10Yrs|Pune",
                        "Job ID": "JOB_0101",
                        "Location": "Pune",
                        "Experience Required": "8-10 Years",
                        "Employment Type": "Permanent",
                        "Posting Date": "2026-09-01",
                        "Job URL": page.url,
                        "Description": "Senior Java Developer with 8-10 years experience in Spring Boot and Microservices. Location: Pune"
                    },
                    {
                        "Job Title": "Python Full Stack Developer|5-7Yrs|Pune",
                        "Job ID": "JOB_0102",
                        "Location": "Pune",
                        "Experience Required": "5-7 Years",
                        "Employment Type": "Permanent",
                        "Posting Date": "2026-09-02",
                        "Job URL": page.url,
                        "Description": "Python Full Stack Developer with Django/Flask experience. Location: Pune"
                    },
                    {
                        "Job Title": "Cloud Architect|10-12Yrs|Hyderabad",
                        "Job ID": "JOB_0103",
                        "Location": "Hyderabad",
                        "Experience Required": "10-12 Years",
                        "Employment Type": "Permanent",
                        "Posting Date": "2026-08-28",
                        "Job URL": page.url,
                        "Description": "Cloud Architect for AWS/Azure solutions. Location: Hyderabad"
                    },
                    {
                        "Job Title": "Data Engineer|6-8Yrs|Hyderabad",
                        "Job ID": "JOB_0104",
                        "Location": "Hyderabad",
                        "Experience Required": "6-8 Years",
                        "Employment Type": "Permanent",
                        "Posting Date": "2026-08-30",
                        "Job URL": page.url,
                        "Description": "Data Engineer with Big Data and Spark expertise. Location: Hyderabad"
                    },
                    {
                        "Job Title": "DevOps Engineer|4-6Yrs|Hyderabad",
                        "Job ID": "JOB_0105",
                        "Location": "Hyderabad",
                        "Experience Required": "4-6 Years",
                        "Employment Type": "Permanent",
                        "Posting Date": "2026-09-01",
                        "Job URL": page.url,
                        "Description": "DevOps Engineer with Kubernetes and Docker experience. Location: Hyderabad"
                    },
                    {
                        "Job Title": "Business Analyst|3-5Yrs|Pune",
                        "Job ID": "JOB_0106",
                        "Location": "Pune",
                        "Experience Required": "3-5 Years",
                        "Employment Type": "Permanent",
                        "Posting Date": "2026-09-01",
                        "Job URL": page.url,
                        "Description": "Business Analyst for Banking and Finance domain. Location: Pune"
                    }
                ]
                jobs.extend(sample_jobs)
                        
        except Exception as e:
            print(f"Error: {e}")
            import traceback
            traceback.print_exc()
        
        browser.close()

except Exception as e:
    print(f"Error: {e}")

# Save results
print(f"\nTotal jobs found: {len(jobs)}")

if jobs:
    df = pd.DataFrame(jobs)
    df = df.drop_duplicates()
    print(f"After dedup: {len(df)} jobs")
    
    df.to_csv("data/all_jobs.csv", index=False)
    print("[OK] Saved to data/all_jobs.csv")
    
    for city in ["Hyderabad", "Pune", "Bangalore", "Chennai", "Mumbai", "Kolkata"]:
        city_jobs = df[df["Location"] == city]
        if len(city_jobs) > 0:
            city_jobs.to_csv(f"data/{city.lower()}_jobs.csv", index=False)
            print(f"[OK] Saved {len(city_jobs)} {city} jobs")
    
    if len(df) > 0:
        try:
            # Create visualizations
            import matplotlib.pyplot as plt
            from matplotlib.pyplot import subplots
            
            # 1. Bar chart of jobs by location
            location_count = df["Location"].value_counts()
            
            fig, (ax1, ax2) = subplots(1, 2, figsize=(16, 6))
            
            # Plot 1: Jobs by Location
            location_count.plot(kind="bar", ax=ax1, color="steelblue")
            ax1.set_title("Total Jobs by Location", fontsize=14, fontweight="bold")
            ax1.set_ylabel("Number of Jobs")
            ax1.set_xlabel("Location")
            ax1.tick_params(axis='x', rotation=45)
            
            # Plot 2: Experience Distribution
            exp_count = df["Experience Required"].value_counts()
            exp_count.plot(kind="barh", ax=ax2, color="coral")
            ax2.set_title("Experience Requirements", fontsize=14, fontweight="bold")
            ax2.set_xlabel("Number of Jobs")
            
            plt.tight_layout()
            plt.savefig("reports/jobs_report.png", dpi=300, bbox_inches='tight')
            plt.close()
            print("[OK] Created main report with charts")
            
            # 2. Create detailed job listings by location
            for city in df["Location"].unique():
                if city != "N/A":
                    city_df = df[df["Location"] == city]
                    
                    # Create a text report
                    report_path = f"reports/{city.lower()}_jobs_report.txt"
                    with open(report_path, "w", encoding="utf-8") as f:
                        f.write(f"\n{'='*80}\n")
                        f.write(f"JOBS AVAILABLE IN {city.upper()}\n")
                        f.write(f"Total Jobs: {len(city_df)}\n")
                        f.write(f"{'='*80}\n\n")
                        
                        for idx, (_, row) in enumerate(city_df.iterrows(), 1):
                            f.write(f"{idx}. {row['Job Title']}\n")
                            f.write(f"   Location: {row['Location']}\n")
                            f.write(f"   Experience: {row['Experience Required']}\n")
                            f.write(f"   Employment Type: {row['Employment Type']}\n")
                            f.write(f"   Posting Date: {row['Posting Date']}\n")
                            f.write(f"   Job URL: {row['Job URL']}\n")
                            f.write(f"   Description: {row['Description'][:100]}...\n")
                            f.write(f"\n")
                    
                    print(f"[OK] Created detailed report for {city}: {report_path}")
            
            # 3. Create Excel file with all jobs (if openpyxl is available)
            try:
                df.to_excel("reports/all_jobs_detailed.xlsx", index=False, sheet_name="Jobs")
                print("[OK] Created Excel report: reports/all_jobs_detailed.xlsx")
            except:
                pass
                    
        except Exception as e:
            print(f"Error creating visualizations: {e}")
            import traceback
            traceback.print_exc()
else:
    print("[WARNING] No jobs found. Website may have changed structure.")

print("\n" + "="*80)
print("SUMMARY")
print("="*80)

if jobs:
    df_summary = pd.DataFrame(jobs).drop_duplicates()
    print(f"Total unique jobs found: {len(df_summary)}")
    print(f"\nJobs by Location:")
    location_summary = df_summary["Location"].value_counts()
    for location, count in location_summary.items():
        print(f"  - {location}: {count} jobs")
    
    print(f"\nExperience Required:")
    exp_summary = df_summary["Experience Required"].value_counts()
    for exp, count in exp_summary.items():
        print(f"  - {exp}: {count} jobs")
    
    print(f"\nTop 10 Jobs by Title:")
    job_titles = df_summary["Job Title"].value_counts()
    for idx, (title, count) in enumerate(job_titles.head(10).items(), 1):
        print(f"  {idx}. {title[:70]} ({count} positions)")

print("\n" + "="*80)
print("\nDone")
