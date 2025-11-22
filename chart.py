import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Generate synthetic data
np.random.seed(42)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
segments = ['Enterprise', 'SMB', 'Consumer']
data = []

for segment in segments:
    if segment == 'Enterprise':
        base = 80000; growth = 2000; variance = 5000
    elif segment == 'SMB':
        base = 40000; growth = 1000; variance = 3000
    else:
        base = 20000; growth = 500; variance = 2000
        
    for i, month in enumerate(months):
        seasonal_effect = 0
        if month in ['Nov', 'Dec']:
            seasonal_effect = base * 0.2
        revenue = base + (growth * i) + seasonal_effect + np.random.normal(0, variance)
        data.append({'Month': month, 'Revenue': revenue, 'Segment': segment})

df = pd.DataFrame(data)

# Create plot
plt.figure(figsize=(8, 8))
sns.set_style("whitegrid")
sns.set_context("talk")

sns.lineplot(data=df, x='Month', y='Revenue', hue='Segment', style='Segment', markers=True, dashes=False, palette='deep')

plt.title('Monthly Revenue Trends by Customer Segment')
plt.xlabel('Month')
plt.ylabel('Revenue ($)')
plt.legend(loc='best')
plt.tight_layout()

# Save as 512x512
plt.savefig('chart.png', dpi=64)
