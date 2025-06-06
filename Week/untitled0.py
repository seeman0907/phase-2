# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-xGtYAiXAeTVDFcEJGdPHsDHVuKMW0Wt
"""

import numpy as np
import pandas as pd
from scipy import stats

# Sample dataset
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
import numpy as np
import pandas as pd
from scipy import stats

# Sample dataset
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Mean
mean_value = np.mean(data)
print(f"Mean: {mean_value}")

# Variance
variance = np.var(data, ddof=1)  # Sample variance

# Standard Deviation
std_dev = np.std(data, ddof=1)
print(f"Variance: {variance}, Standard Deviation: {std_dev}")

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample Data: Student Scores in Different Subjects
data = {
    'Math': [80, 85, 78, 90, 88, 92, 76, 89, 95, 84],
    'Science': [75, 82, 79, 91, 87, 95, 72, 88, 97, 83],
    'English': [85, 80, 78, 88, 90, 85, 76, 89, 92, 81]
}

# Create a DataFrame
df = pd.DataFrame(data)
# Generate Correlation Matrix
correlation_matrix = df.corr()
# Plot Heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Student Scores Correlation Heatmap")
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = [10, 12, 14, 15, 17, 20, 30, 100]  # 100 is an outlier

# Convert to DataFrame
df = pd.DataFrame(data, columns=['values'])

# Calculate Q1, Q3, and IQR
Q1 = df['values'].quantile(0.25)
Q3 = df['values'].quantile(0.75)
IQR = Q3 - Q1

# Define outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = df[(df['values'] < lower_bound) | (df['values'] > upper_bound)]

# Plot Boxplot
plt.boxplot(df['values'])
plt.title("Box Plot to Detect Outliers")
plt.show()

# Print outliers
print("Outliers:\n", outliers)

from scipy import stats

# Convert to NumPy array
data_array = np.array(data)

# Calculate Z-scores
z_scores = np.abs(stats.zscore(data_array))

# Find outliers (Z-score > 3)
outliers = data_array[z_scores > 3]

print("Outliers using Z-score method:", outliers)

plt.scatter(range(len(data)), data, color='blue', label="Data Points")
plt.scatter([data.index(100)], [100], color='red', label="Outlier")  # Highlight outlier
plt.xlabel("Index")
plt.ylabel("Values")
plt.title("Scatter Plot Showing Outlier")
plt.legend()
plt.show()

plt.scatter(range(len(data)), data, color='blue', label="Data Points")
plt.scatter([data.index(100)], [100], color='red', label="Outlier")  # Highlight outlier
plt.xlabel("Index")
plt.ylabel("Values")
plt.title("Scatter Plot Showing Outlier")
plt.legend()
plt.show()