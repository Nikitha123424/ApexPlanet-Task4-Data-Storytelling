# ApexPlanet Task 4 – Data Storytelling & Statistical Validation

## Project Overview

This project combines the findings from previous tasks into a clear data story and validates a business question using statistical hypothesis testing.

## Analysis Performed

- Sales and customer behavior analysis
- Customer segmentation
- Business insights and recommendations
- Hypothesis formulation
- Independent two-sample t-test
- P-value analysis
- 95% confidence interval

## Hypothesis

**H₀:** Male and female customers have the same average sales per order.

**H₁:** Male and female customers have different average sales per order.

## Statistical Results

- Male average sales per order: ₹141,807.34
- Female average sales per order: ₹136,883.21
- T-statistic: 0.6826
- P-value: 0.495011
- 95% Confidence Interval: −₹9,214.68 to ₹19,062.94

Since the p-value is greater than 0.05, the null hypothesis is not rejected.

## Conclusion

There is not enough statistical evidence to conclude that male and female customers have different average sales per order.

The analysis also identified four customer segments: High Value, Regular, Occasional, and Low Value Customers. These segments can support targeted customer strategies and business decision-making.

## Tools Used

- Python
- Pandas
- NumPy
- SciPy
- Excel
- PowerPoint
- GitHub

## Files

- `Cleaned_Sales_Dataset.xlsx`
- `Customer_Segmentation.xlsx`
- `Segment_Summary.xlsx`
- `sql_analysis.py`
- `hypothesis_testing.py`
- `Hypothesis_Testing_Summary.xlsx`
- `ApexPlanet_Task4_Final_Data_Storytelling.pptx`