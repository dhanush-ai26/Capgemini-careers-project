# Capgemini-careers-project
A comprehensive job analytics platform that automates job data collection, processing, and visualization from career websites and job portals. The system enables users to explore opportunities, analyze hiring trends, filter jobs by skills and locations, and gain actionable insights through interactive dashboards.

Job Analytics Dashboard
Overview

The Job Analytics Dashboard is a data-driven platform that automates the collection, processing, and visualization of job postings from career websites and job portals. The system helps job seekers, recruiters, and analysts gain insights into hiring trends, in-demand skills, experience requirements, and location-based opportunities.

Features
Automated job data extraction
Data cleaning and preprocessing
Job search and filtering
Location-based analysis
Experience-level categorization
Hiring trend visualization
Interactive dashboards
CSV data export
Scalable architecture for multiple job portals
Technology Stack
Python
Pandas
Requests
Streamlit
Plotly
HTML/CSS

CSV Data Storage

Project Structure
capgemini-careers-project/
│
├── data/
│   ├── bangalore_jobs.csv
│   ├── chennai_jobs.csv
│   ├── hyderabad_jobs.csv
│   ├── kolkata_jobs.csv
│   ├── mumbai_jobs.csv
│   ├── pune_jobs.csv
│   ├── keyword_frequency.csv
│   └── skill_frequency.csv
│
├── reports/
│   ├── bangalore_jobs_report.txt
│   ├── bucharest_jobs_report.txt
│   ├── chennai_jobs_report.txt
│   ├── cluj_jobs_report.txt
│   ├── eindhoven_jobs_report.txt
│   ├── hyderabad_jobs_report.txt
│   ├── kolkata_jobs_report.txt
│   ├── kyiv_jobs_report.txt
│   ├── mumbai_jobs_report.txt
│   ├── pune_jobs_report.txt
│   ├── jobs_report.png
│   ├── top_skills.png
│   └── wordcloud.png
│
├── src/
│   ├── scrape_jobs.py
│   ├── keyword_analysis.py
│   ├── skills_analysis.py
│   ├── location_report.py
│   └── run_project.py
│
├── debug_jobs_lines.txt
├── requirements.txt
└── README.md

Workflow

Job Websites
      │
      ▼
Data Extraction
      │
      ▼
CSV Dataset Generation
      │
      ▼
Skill & Keyword Analysis
      │
      ▼
Location-wise Reports
      │
      ▼
Visualizations & Insights
      │
      ▼
Final Analytics Dashboard

Key Insights

Jobs by Location
Jobs by Experience Level
Hiring Trends
Employment Type Distribution
Most In-Demand Roles
Market Growth Analysis

Use Cases

Job Market Research
Career Planning
Recruitment Analytics
Talent Acquisition
Workforce Trend Analysis
Opportunity Discovery

Future Enhancements

Multi-website job aggregation
Skill gap analysis
AI-powered job recommendations
Salary trend predictions
Resume matching system
Real-time job notifications

Author

Dhanush D
