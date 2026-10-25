# 1. Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Wash_data import wash_data

# 2. Load data
# we want to avoid silent type errors, so we use dtype to fix column data type.
# The data type should reflect the meaning of the column, not just it's appearance. For example, a column of numbers may be an identifyer rather than a quantity.
# dtype, parse_dates, na_values, encoding: arguments mentioned in lecture week 40

# Loading Salaries dataset
salary_df = pd.read_csv(
    "Salaries.csv",
    encoding="utf-8",
    dtype={
        "experience_level": "string",
        "employment_type": "string",
        "job_title": "string",
        "salary_currency": "string",
        "employee_residence": "string",
        "company_location": "string",
        "company_size": "string",
    },
)

# Loading exposure dataset
exposure_df = pd.read_csv(
    "Exposure.csv",
    encoding="utf-8",
    dtype={
        "label4d": "string",
        "label1d": "string",
        "Title": "string",
        "Task_ISCO": "string",
        "potential23": "string",
        "potential25": "string",
    },
)

# Reasoning for dtype choices:
# Job titles and other classifications are labels, not quantities.
# Salary amounts, scores, and years should remain numeric.
# We have not found any na types, so we did not use this argument.

# Inspect the imported data
print(salary_df.shape) #to check nothing was lost
print(salary_df.info()) #to see the types and the missing values together

print(exposure_df.shape)
print(exposure_df.info())

'''
the exposure dataset contains 6 null values
    score_2023: row 2026, 2306
    predicted_score_2025_gpt4o: row 1782, 2103, 2897
    predicted_score_2025_gemini: row 776
    
    To create a separate cleaned DataFrame that drops the rows with missing values:
    
        comparison_df = df.dropna(
        subset=[
            "score_2023",
            "gpt_prediction_2025",
            "gemini_prediction_2025"
        ]
    ).copy()    
'''


# 3. Explore data


# 4. Clean data
if __name__ == '__main__':

    clean_salary_df = wash_data(salary_df)
    print(clean_salary_df.shape)
    print(clean_salary_df["job_category"].value_counts(dropna=False))





# 5. Prepare analysis data
# Select relevant columns and filters (week 40 lecture part 2 on selecting, filtering, masking)
# week 40 lecture part 3 on grouping and joining

# 6. Analyze
# Calculate grouped statistics

# 7. Visualize
# Create charts, plots

# 8. Conclusions
# Summarize the findings in markdown cells