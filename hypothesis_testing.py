import pandas as pd
from scipy.stats import ttest_ind
from openpyxl import Workbook

print("Loading cleaned sales dataset...")

# Load dataset
df = pd.read_excel("Cleaned_Sales_Dataset.xlsx")

print("Dataset loaded successfully!")
print("Dataset shape:", df.shape)

# ---------------------------------------------------------
# HYPOTHESIS TEST
# ---------------------------------------------------------

print("\nHypothesis Testing")
print("-" * 50)

print("Business Question:")
print("Do male and female customers have significantly different")
print("average sales per order?")

print("\nNull Hypothesis (H0):")
print("Male and female customers have the same average sales per order.")

print("\nAlternative Hypothesis (H1):")
print("Male and female customers have different average sales per order.")

# Separate groups
male_sales = df[df["Gender"] == "Male"]["Total_Sales"]
female_sales = df[df["Gender"] == "Female"]["Total_Sales"]

# Calculate means
male_mean = male_sales.mean()
female_mean = female_sales.mean()

print("\nMale Average Sales per Order:", round(male_mean, 2))
print("Female Average Sales per Order:", round(female_mean, 2))

# Independent two-sample t-test
t_stat, p_value = ttest_ind(
    male_sales,
    female_sales,
    equal_var=False
)

print("\nStatistical Test:")
print("Independent Two-Sample t-test")

print("\nT-statistic:", round(t_stat, 4))
print("P-value:", round(p_value, 6))

# ---------------------------------------------------------
# 95% CONFIDENCE INTERVAL
# ---------------------------------------------------------

import numpy as np

male_n = len(male_sales)
female_n = len(female_sales)

male_std = male_sales.std()
female_std = female_sales.std()

difference = male_mean - female_mean

standard_error = np.sqrt(
    (male_std ** 2 / male_n) +
    (female_std ** 2 / female_n)
)

# 95% approximate confidence interval
margin_of_error = 1.96 * standard_error

ci_lower = difference - margin_of_error
ci_upper = difference + margin_of_error

print("\n95% Confidence Interval for Mean Difference:")
print("Lower:", round(ci_lower, 2))
print("Upper:", round(ci_upper, 2))

# ---------------------------------------------------------
# CONCLUSION
# ---------------------------------------------------------

alpha = 0.05

if p_value < alpha:
    conclusion = (
        "Reject the null hypothesis. There is a statistically "
        "significant difference between male and female average sales."
    )
else:
    conclusion = (
        "Fail to reject the null hypothesis. There is not enough "
        "statistical evidence to conclude that male and female "
        "average sales are different."
    )

print("\nConclusion:")
print(conclusion)

# ---------------------------------------------------------
# SAVE RESULTS TO EXCEL
# ---------------------------------------------------------

results = pd.DataFrame({
    "Metric": [
        "Business Question",
        "Null Hypothesis",
        "Alternative Hypothesis",
        "Male Orders",
        "Female Orders",
        "Male Average Sales",
        "Female Average Sales",
        "T-Statistic",
        "P-Value",
        "Confidence Level",
        "CI Lower",
        "CI Upper",
        "Significance Level",
        "Conclusion"
    ],
    "Result": [
        "Do male and female customers have significantly different average sales per order?",
        "Male and female customers have the same average sales per order.",
        "Male and female customers have different average sales per order.",
        male_n,
        female_n,
        round(male_mean, 2),
        round(female_mean, 2),
        round(t_stat, 4),
        round(p_value, 6),
        "95%",
        round(ci_lower, 2),
        round(ci_upper, 2),
        alpha,
        conclusion
    ]
})

results.to_excel(
    "Hypothesis_Testing_Summary.xlsx",
    index=False
)

print("\nHypothesis testing summary saved successfully!")
print("File created: Hypothesis_Testing_Summary.xlsx")