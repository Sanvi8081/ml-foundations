import numpy as np
import matplotlib.pyplot as plt

# ----------------------------
# Step 1: Create Dataset
# ----------------------------

# Example: Hours studied vs Marks
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

# ----------------------------
# Step 2: Calculate Mean
# ----------------------------

x_mean = x.mean()
y_mean = y.mean()

# ----------------------------
# Step 3: Calculate Slope (m)
# Formula:
# m = Σ (x - x̄)(y - ȳ) / Σ (x - x̄)^2
# ----------------------------

numerator = np.sum((x - x_mean) * (y - y_mean))
denominator = np.sum((x - x_mean) ** 2)

m = numerator / denominator

# ----------------------------
# Step 4: Calculate Intercept (b)
# b = ȳ - m*x̄
# ----------------------------

b = y_mean - m * x_mean

# ----------------------------
# Step 5: Predictions
# ----------------------------

y_pred = m * x + b

# ----------------------------
# Step 6: Print Results
# ----------------------------

print("Slope (m):", m)
print("Intercept (b):", b)

# ----------------------------
# Step 7: Plot Graph
# ----------------------------

plt.scatter(x, y)
plt.plot(x, y_pred)
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.title("Linear Regression From Scratch")
plt.show()