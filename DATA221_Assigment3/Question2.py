import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
crime_data = pd.read_csv("crime.csv")

# Select the ViolentCrimesPerPop column and remove missing values
violent_crime_rates = crime_data["ViolentCrimesPerPop"].dropna()

#Histograms
plt.figure()
plt.hist(violent_crime_rates, bins=20)
plt.title("Distribution of Violent Crimes Per Population")
plt.xlabel("Violent Crimes Per Population")
plt.ylabel("Frequency")
plt.show()

#Box plot
plt.figure()
plt.boxplot(violent_crime_rates)
plt.title("Box Plot of Violent Crimes Per Population")
plt.xlabel("Violent Crimes Per Population")
plt.ylabel("Value")
plt.show()

#Written answers
# The histogram shows that most communities have relatively low violent crime rates,
# with fewer communities having very high values.
# The spread of the data is uneven, suggesting the distribution is not symmetric.
# There is a noticeable right tail, indicating that higher crime values are less common.
# The box plot shows the median as the line inside the box, representing the middle crime rate.
# The median is closer to the lower end of the data range, supporting the idea of right skew.
# Points beyond the whiskers suggest the presence of outliers with unusually high crime rates.
