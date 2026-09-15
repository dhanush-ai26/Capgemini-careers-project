import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("reports", exist_ok=True)

# Read jobs data
df = pd.read_csv("data/all_jobs.csv")

# Count jobs by location
location_count = df["Location"].value_counts()

print("\nLocation Summary:")
print(location_count)

# Create graph
plt.figure(figsize=(8, 5))

location_count.plot(
    kind="bar",
    color=["steelblue", "orange"]
)

plt.title("Jobs by Location")
plt.xlabel("Location")
plt.ylabel("Number of Jobs")

plt.tight_layout()

plt.savefig(
    "reports/jobs_report.png"
)

plt.show()

print("\nLocation Report Generated")
print("Chart Saved: reports/jobs_report.png")