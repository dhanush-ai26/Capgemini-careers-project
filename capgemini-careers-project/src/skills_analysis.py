import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import os

# Create reports folder if not exists
os.makedirs("reports", exist_ok=True)

# Read jobs data
df = pd.read_csv("data/all_jobs.csv")

# Skills list
skills = [
    "Python",
    "Java",
    "SQL",
    "AWS",
    "Azure",
    "Power BI",
    "Tableau",
    "Machine Learning",
    "Data Analysis",
    "Docker",
    "Kubernetes",
    "Spark",
    "Hadoop"
]

# Count skill occurrences
counter = Counter()

for desc in df["Description"]:
    text = str(desc).lower()

    for skill in skills:
        if skill.lower() in text:
            counter[skill] += 1

# Create DataFrame
skill_df = pd.DataFrame(
    counter.items(),
    columns=["Skill", "Count"]
)

# Sort by count
skill_df = skill_df.sort_values(
    by="Count",
    ascending=False
)

# Save skill report
skill_df.to_csv(
    "data/skill_frequency.csv",
    index=False
)

# Print result
print("\nTop Skills:")
print(skill_df)

# Create chart
plt.figure(figsize=(10, 6))

plt.bar(
    skill_df["Skill"],
    skill_df["Count"],
    color="steelblue"
)

plt.title("Top Demanded Skills")
plt.xlabel("Skills")
plt.ylabel("Frequency")
plt.xticks(rotation=45)

plt.tight_layout()

# Save chart
plt.savefig(
    "reports/top_skills.png"
)

plt.show()

print("\nSkill analysis completed.")
print("CSV Saved: data/skill_frequency.csv")
print("Chart Saved: reports/top_skills.png")