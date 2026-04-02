import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")
print(tips.head())

# Task 1 — Your First Matplotlib Chart
# Using Matplotlib, create a bar chart that shows the total tip amount collected on each day of the week.
# x-axis: day, y-axis: total sum of tip
# Add a title, x-label, and y-label
# Set the figure size to (8, 5) using plt.figure(figsize=(8, 5))
# Call plt.show() to display the chart
# Hint: Use tips.groupby("day")["tip"].sum() to get the total tips per day before plotting.

# sum_of_tip = tips.groupby("day")["tip"].sum()
# plt.figure(figsize=(8, 5))
# plt.bar(sum_of_tip.index, sum_of_tip.values , color="steelblue")
# plt.title("Total Tip Amount per Day")
# plt.xlabel("Day")
# plt.ylabel("Total Bill (₹)")
# plt.show()

# Task 2 — Seaborn Histogram
# Using Seaborn, create a histogram of the tip column to see how tip amounts are distributed across all customers.
# Set bins=20
# Overlay a KDE curve on the histogram
# Add the title: "Distribution of Tip Amounts"
# Call plt.show() to display the chart
# In a markdown cell below your chart, write 2–3 sentences describing what the chart tells you — for example: where most tips fall, whether the distribution is skewed, and what the KDE line adds to the histogram.

# sns.histplot(data=tips, x="tip", bins=20, kde=True, color="steelblue") 
# plt.title("Distribution of Tip Amounts")
# plt.xlabel("Tip (₹)")
# plt.ylabel("Count")
# plt.tight_layout()
# plt.show()

# Task 3 — Seaborn Scatter Plot
# Using Seaborn, create a scatter plot to explore the relationship between the total bill and the tip amount.
# x-axis: total_bill, y-axis: tip
# Color the points by day using the hue parameter
# Add the title: "Total Bill vs Tip Amount"
# Call plt.show() to display the chart
# In a markdown cell below, write 1–2 sentences describing any pattern you notice — for example, does a higher bill generally lead to a higher tip?

sns.scatterplot(data=tips, x="total_bill", y="tip", hue="day", style="smoker", alpha=0.7)
plt.title("Total Bill vs Tip Amount")
plt.xlabel("Total Bill (₹)")
plt.ylabel("Tip (₹)")
plt.tight_layout()
plt.show()