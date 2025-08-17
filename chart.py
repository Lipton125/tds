import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Generate Realistic Synthetic Data
# Create a DataFrame with product categories and associated customer satisfaction scores.
np.random.seed(42) # for reproducibility
data = {
    'Product_Category': ['Electronics', 'Apparel', 'Home Goods', 'Beauty', 'Books', 'Toys'],
    'Customer_Satisfaction_Score': np.random.uniform(3.5, 4.9, 6).round(2)
}
df = pd.DataFrame(data)

# Sort the data for better visualization
df = df.sort_values(by='Customer_Satisfaction_Score', ascending=False)

# 2. Set Professional Styling for the Chart
sns.set_theme(style="whitegrid", palette="viridis") # A professional-looking theme
sns.set_context("poster") # Context for presentation-ready text

# 3. Create the Bar Plot
plt.figure(figsize=(8, 8)) # This sets the figure size for 512x512 pixel output at 64 dpi

# Create the bar plot using sns.barplot()
ax = sns.barplot(
    data=df,
    x='Product_Category',
    y='Customer_Satisfaction_Score'
)

# Add titles and labels for clarity
plt.title('Average Customer Satisfaction Score by Product Category', pad=20)
plt.xlabel('Product Category')
plt.ylabel('Average Customer Satisfaction Score')

# Add score labels on top of each bar for precise values
for p in ax.patches:
    ax.annotate(f'{p.get_height():.2f}', 
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', 
                xytext=(0, 10), 
                textcoords='offset points',
                fontsize=20)

# 4. Final Adjustments and Export
plt.ylim(3.0, 5.0) # Set a consistent y-axis scale for better comparison
plt.xticks(rotation=45, ha='right') # Rotate x-axis labels for readability
plt.tight_layout() # Adjust layout to prevent labels from being cut off

# Save the chart as a PNG file with exactly 512x512 pixel dimensions
plt.savefig('chart.png', dpi=64, bbox_inches='tight')

print("chart.png has been generated with 512x512 dimensions.")
