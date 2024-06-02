import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict, Counter

data = pd.read_csv('data.csv')

category_review_counts = defaultdict(list)
category_review_percentages = defaultdict(list)

for idx, row in data.iterrows():
    categories = row['game_tags'][1:-1].replace("'", "").split(', ')
    review_count = row['review_count']
    review_percentage = row['review_percentage']
    
    for category in categories[:5]:
        category_review_counts[category].append(review_count)
        category_review_percentages[category].append(review_percentage)

most_common_categories = [category for category, count in Counter([category for row in data['game_tags'] for category in row[1:-1].replace("'", "").split(', ')]).most_common(25)]

avg_review_counts = {category: sum(category_review_counts[category])/len(category_review_counts[category]) for category in most_common_categories}
avg_review_percentages = {category: sum(category_review_percentages[category])/len(category_review_percentages[category]) for category in most_common_categories}

categories = list(avg_review_counts.keys())
avg_counts = list(avg_review_counts.values())
avg_percentages = list(avg_review_percentages.values())

df = pd.DataFrame({'Category': categories, 'Average Review Count': avg_counts, 'Average Review Percentage': avg_percentages})

fig, ax1 = plt.subplots(figsize=(15, 8))

color = 'tab:blue'
ax1.set_xlabel('Game Categories')
ax1.set_ylabel('Average Review Count', color=color)
ax1.bar(df['Category'], df['Average Review Count'], color=color, alpha=0.6, label='Average Review Count')
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_xticklabels(df['Category'], rotation=90)

ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Average Review Percentage', color=color)
ax2.plot(df['Category'], df['Average Review Percentage'], color=color, marker='o', linestyle='-', label='Average Review Percentage')
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
plt.title('Average Review Count and Percentage by Top 25 Game Categories')
plt.show()