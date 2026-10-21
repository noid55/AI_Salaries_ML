import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

if __name__ == '__main__':
    df = pd.read_csv("Salaries.csv")

    print(df["job_title"].unique())
    unique_titles = df["job_title"].unique()




