import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os



if __name__ == '__main__':
    test = pd.read_csv("Salaries.csv")
    print(test.head(5).to_string())

