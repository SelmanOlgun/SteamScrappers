import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Veri setini yükle
data = pd.read_csv("data.csv")

# Game Tags Word Cloud
game_tags = ' '.join(data['game_tags'])
wordcloud = WordCloud(width = 800, height = 800, background_color ='white').generate(game_tags)
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
plt.show()