import pandas as pd

# Load the dataset and let crime.csv be in the same folder
crime_data = pd.read_csv("crime.csv")

# Select the ViolentCrimesPerPop column
violent_crime_rates = crime_data["ViolentCrimesPerPop"]

#Remove missing values
violent_crime_rates = violent_crime_rates.dropna()

#Calculate the statistical measures
mean_crime_rate = violent_crime_rates.mean()
median_crime_rate = violent_crime_rates.median()
std_crime_rate = violent_crime_rates.std()
min_crime_rate = violent_crime_rates.min()
max_crime_rate = violent_crime_rates.max()

# Print all results
print("ViolentCrimesPerPop Statistics")
print("Mean:", mean_crime_rate)
print("Median:", median_crime_rate)
print("Standard Deviation:", std_crime_rate)
print("Minimum:", min_crime_rate)
print("Maximum:", max_crime_rate)

#Written answers
# Mean vs Median:
# If the mean is greater than the median, the distribution is right-skewed, meaning a small number of high crime values pull the average upward.
#If the mean and median are close, the distribution is roughly symmetric.

# Effect of extreme values:
# The mean is more affected by extreme values because it includes every value in its calculation. The median is more resistant to extreme values since it
#depends only on the middle value after sorting.
