import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Generate Realistic Synthetic Data
np.random.seed(42)
data = {
    'Product_Category': ['Electronics', 'Apparel', 'Home Goods', 'Beauty', 'Books', 'Toys'],
    'Customer_Satisfaction_Score': np.random.uniform(3.5, 4.9, 6).round(2)
}
df = pd.DataFrame(data)
df = df.sort_values(by='Customer_Satisfaction_Score', ascending=False)

# 2. Set Professional Styling
sns.set_theme(style="whitegrid", palette="viridis")
sns.set_context("poster")

# 3. Create the Bar Plot
# Set a slightly larger figure size to ensure all elements fit without `bbox_inches`
plt.figure(figsize=(8, 8)) 

ax = sns.barplot(
    data=df,
    x='Product_Category',
    y='Customer_Satisfaction_Score'
)

plt.title('Average Customer Satisfaction Score by Product Category', pad=20)
plt.xlabel('Product Category')
plt.ylabel('Average Customer Satisfaction Score')

for p in ax.patches:
    ax.annotate(f'{p.get_height():.2f}', 
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', 
                xytext=(0, 10), 
                textcoords='offset points',
                fontsize=20)

plt.ylim(3.0, 5.0)
plt.xticks(rotation=45, ha='right')

# 4. Save the chart with the correct dpi and remove bbox_inches='tight'
# 512 pixels / 8 inches = 64 dpi
# The final command should be:
plt.savefig('chart.png', dpi=64)
# Make sure no other plotting commands come after this line.

print("chart.png has been generated with 512x512 pixel dimensions.")
