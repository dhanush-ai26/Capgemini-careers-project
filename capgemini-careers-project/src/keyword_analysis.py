import pandas as pd
import re
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os

# Create reports folder if it doesn't exist
os.makedirs("reports", exist_ok=True)

# Read jobs data
df = pd.read_csv("data/all_jobs.csv")

# Combine all descriptions
all_text = " ".join(df["Description"].astype(str)).lower()

# Extract words
words = re.findall(r"\b[a-zA-Z]{3,}\b", all_text)

# Stop words
stop_words = {
    "the", "and", "for", "with", "you",
    "your", "are", "our", "all", "job",
    "will", "can", "have", "this", "that",
    "from", "their", "they", "who", "what",
    "when", "where", "how"
}

# Remove stop words
filtered_words = [
    word for word in words
    if word not in stop_words
]

# Count frequencies
counter = Counter(filtered_words)

# Top 100 keywords
keyword_df = pd.DataFrame(
    counter.most_common(100),
    columns=["Keyword", "Frequency"]
)

# Save keyword report
keyword_df.to_csv(
    "data/keyword_frequency.csv",
    index=False
)

print("\nTop 20 Keywords:")
print(keyword_df.head(20))

# Create Word Cloud
wordcloud = WordCloud(
    width=1200,
    height=600,
    background_color="white"
).generate(" ".join(filtered_words))

plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Keyword Word Cloud")

plt.savefig(
    "reports/wordcloud.png"
)

plt.show()

print("\nKeyword Analysis Completed")
print("CSV Saved: data/keyword_frequency.csv")
print("Image Saved: reports/wordcloud.png")