import pandas as pd

# load the dataset
df = pd.read_csv("crime.csv")

# create risk column
df["risk"] = df["ViolentCrimesPerPop"].apply(
    lambda x: "HighCrime" if x >= 0.50 else "LowCrime"
)

# group by risk and calculate average unemployment
avg_unemployment = df.groupby("risk")["PctUnemployed"].mean()

# print results clearly
print("Average Unemployment Rate:")
print("HighCrime:", avg_unemployment["HighCrime"])
print("LowCrime:", avg_unemployment["LowCrime"])
