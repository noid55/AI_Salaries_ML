
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import openpyxl
if __name__ == '__main__':

    # 1b. ILO Generative AI occupational exposure scores (CC BY - Gmyrek et al. 2025)
    EXPOSURE_URL = "https://github.com/pgmyrek/2025_GenAI_scores_ISCO08/raw/main/Final_Scores_ISCO08_Gmyrek_et_al_2025.xlsx"

    try:
        exposure_raw = pd.read_excel(EXPOSURE_URL)
        print("Shape:", exposure_raw.shape)
        print(exposure_raw.head())
        exposure_raw.to_csv("Exposure.csv")
    except Exception as e:
        print("Could not fetch exposure file directly (source may have moved / renamed the file).")
        print("Error:", e)
        print("-> Check https://github.com/pgmyrek/2025_GenAI_scores_ISCO08 for the current filename")
        exposure_raw = None