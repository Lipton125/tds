import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Create a placeholder for the supply chain dataset with 60 transactions
# In a real scenario, you would use: df = pd.read_csv('your_data.csv')
data = {
    'Supplier_Lead_Time': np.random.uniform(5, 30, 60),
    'Inventory_Levels': np.random.uniform(100, 1000, 60),
    'Order_Frequency': np.random.uniform(1, 12, 60),
    'Delivery_Performance': np.random.uniform(85, 100, 60),
    'Cost_Per_Unit': np.random.uniform(10, 50, 60)
}
df = pd.DataFrame(data)

# 2. Generate the correlation matrix
correlation_matrix = df.corr()

# 3. Save the correlation matrix to a CSV file as 'correlation.csv'
correlation_matrix.to_csv('correlation.csv')

# 4. Create the heatmap visualization
plt.figure(figsize=(5, 5))  # Set figure size to get desired image dimensions
heatmap = sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap='RdYlGn',  # Red-Yellow-Green colormap as requested
    fmt=".2f",
    linewidths=.5,
    vmin=-1, vmax=1
)
plt.title('Supply Chain Metrics Correlation Heatmap')

# 5. Save the heatmap as a PNG file with the required dimensions (400x400 to 512x512)
# The dpi is adjusted to achieve the desired output resolution
plt.savefig('heatmap.png', dpi=100)  # Saves a 500x500 pixel image

print("Correlation matrix saved to 'correlation.csv'")
print("Heatmap saved to 'heatmap.png'")

# Optional: Display the plot for viewing (this might show a UserWarning in a non-interactive environment)
# plt.show()
