import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


if __name__ == '__main__':

    pd.set_option("display.max_columns", 100)
    sns.set_style("whitegrid")

    SALARIES_URL = "https://raw.githubusercontent.com/foorilla/ai-jobs-net-salaries/main/salaries.csv"
    salaries_raw = pd.read_csv(SALARIES_URL)

    print("Shape:", salaries_raw.shape)
    salaries_raw.to_csv('Salaries.csv')