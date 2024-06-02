import pandas as pd
import matplotlib.pyplot as plt
import os
from matplotlib.colors import LogNorm

data = pd.read_csv('data.csv')

data = data[data['price'] < 100]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6), sharex=True)

hb1 = ax1.hexbin(data['price'], data['review_count'], gridsize=50, cmap='Blues', mincnt=1, norm=LogNorm())
cb1 = fig.colorbar(hb1, ax=ax1, label='Count')
ax1.set_title('Review Count vs Price')
ax1.set_xlabel('Price')
ax1.set_ylabel('Review Count')
ax1.grid(True)

hb2 = ax2.hexbin(data['price'], data['review_percentage'], gridsize=50, cmap='Reds', mincnt=1, norm=LogNorm())
cb2 = fig.colorbar(hb2, ax=ax2, label='Percentage')
ax2.set_title('Review Percentage vs Price')
ax2.set_xlabel('Price')
ax2.set_ylabel('Review Percentage')
ax2.grid(True)

plt.suptitle('Relationship Between Price, Review Count, and Review Percentage')


plt.show()