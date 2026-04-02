import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

url ="https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.csv"
df = pd.read_csv(url)
# print(df.shape)
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# print(df.columns.to_list())
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# print(df.dtypes)
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# missing = df.isnull().sum()
# print(f"Missing Values:\n{missing}")
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# missing_percent = (missing / len(df) * 100).round(2)
# print(f"Missing Percentage:\n{missing_percent}")
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# print(df.head)
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# print(df.sample(5, random_state=48))
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# print(df.describe())

# Plot distributions for all numerical columns at once
# numerical_cols = df.select_dtypes(include="number").columns

# fig, axes = plt.subplots(3, 3, figsize=(14, 10))
# axes = axes.flatten() # convert 3*3 grid to a flat list for easy looping

# for i, col in enumerate(numerical_cols):
#     sns.histplot(data=df, x=col, kde=True, ax=axes[i], color="steelblue")
#     axes[i].set_title(col, fontsize=10)
#     axes[i].set_xlabel("")

# plt.suptitle("Distribution of All Numerical Features", fontsize=14, fontweight="bold")
# plt.tight_layout()
# plt.show()

# # -0.5 and 0.5 normal range
# # if more than -1 and 1 --> High skewness
# skewness = df.select_dtypes(include="number").skew().sort_values(ascending=False)
# print("Skewness by Column:")
# print(skewness.round(2))

# # correlation
# corr_matrix = df.select_dtypes(include="number").corr()
# plt.figure(figsize=(10, 8))
# sns.heatmap(
#     corr_matrix,
#     annot = True,
#     fmt = ".2f",
#     cmap = "coolwarm",
#     vmin = -1,
#     vmax = 1
# )
# plt.show()

# Detect Outlier
def detect_outlier_iqr(d, column):
    Q1 = d[column].quantile(0.25)
    Q3 = d[column].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outlier = d[(d[column] < lower_bound)| (d[column] > upper_bound)]

    print(f"Column: {column}")
    print(f"Lower Bound: {lower_bound:.2f}")
    print(f"Upper Bound: {upper_bound:.2f}")
    print(f"Outliers Found: {len(outlier)}({len(outlier)/len(d)*100:.1f}%)")
    return outlier

outlier_rooms = detect_outlier_iqr(df, "total_rooms")
# df = sns.load_dataset("mpg").dropna()
# print(df.shape)
# print(df.columns.to_list())
# print(df.dtypes)
