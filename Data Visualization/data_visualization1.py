import matplotlib.pyplot as plt
import numpy as np

# Step 2: Create some sample data
data = np.random.randn(1000)  # Generating 1000 random data points from a normal distribution

# Step 3: Plot the histogram
plt.hist(data, bins=30, edgecolor='black')

# Adding titles and labels
plt.title('Histogram of Random Data')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Step 4: Show the plot
plt.show()
