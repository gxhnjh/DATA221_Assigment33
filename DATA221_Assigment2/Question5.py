import pandas as pd

# load the dataset
df = pd.read_csv("student.csv")

# create grade_band column
def grade_band(grade):
    if grade <= 9:
        return "Low"
    elif grade <= 14:
        return "Medium"
    else:
        return "High"

df["grade_band"] = df["grade"].apply(grade_band)

# grouped summary table
summary = df.groupby("grade_band").agg(
    number_of_students=("grade", "count"),
    average_absences=("absences", "mean"),
    internet_percentage=("internet", "mean")
)

# convert internet proportion to percentage
summary["internet_percentage"] = summary["internet_percentage"] * 100

# save to csv
summary.to_csv("student_bands.csv")

# print table
print(summary)
