import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os



if __name__ == '__main__':
    test = pd.read_csv("Salaries.csv")
    print(test.head(5).to_string())

FIXES = {
    "Data Analist": "Data Analyst",
    "Cientista de Dados": "Data Scientist",
    "Data Engineer 4": "Data Engineer",
    "Systems Administrator": "System Administrator",
    "Quant Trader": "Quantitative Trader",
    "Postdoctoral Scholar": "Postdoctoral Researcher",
    "Postdoctoral Research Fellow": "Postdoctoral Researcher",
    "Solution Specialist": "Solutions Specialist",
    "AI Solution Director": "AI Solutions Director",
    "Stage": "Intern",
    "Alternance": "Apprentice",
    "Bear Robotics": "Unknown",
    "Cdd": "Unknown",
}

GROUPS = {
    "Developer": [
        "Head of Data", "AI Architect", "Business Intelligence Developer",
        "AI Solutions Lead", "Artificial Intelligence Engineer",
        "Data Operations Engineer", "Head of Machine Learning", "Data Operations",
        "Director of Artificial Intelligence", "Data Quality Engineer",
        "Data Operations Manager", "Machine Learning Developer",
        "Data Operations Lead", "AI Solution Director", "Data Visualization Developer",
        "AI Lead", "Director of Machine Learning", "Data Visualization Engineer",
        "Machine Learning Lead", "Databricks Engineer", "Data Integrator",
        "Machine Learning Specialist", "Data Integration Specialist",
        "Conversational AI Designer", "Data Engineer 4", "IT Enterprise Data Architect",
        "Creative Technologist", "Big Data Developer", "Tableau Developer",
        "AI Tech Lead", "AI Solutions Specialist", "AI Engineering Lead",
        "Head of Applied AI", "Cloud Architect", "Robotics Engineer", "Big Data Engineer",
    ],
    "Analyst": [
        "Data Scientist", "Data Governance Manager", "Data Quality Specialist",
        "BI Analyst", "Data Visualization Designer", "Decision Scientist",
        "Data Management Lead", "Lead Data Analysis", "Data Archivist",
        "Insight Analyst", "Data Team Lead", "Data Quality Lead",
        "Business Intelligence Lead", "Data Visualization Expert",
        "Data Analytics Lead", "Data and Reporting Professional",
        "Data Visualization Specialist", "Advanced Analytics Manager",
        "Power BI Specialist", "Encounter Data Management Professional",
        "Data Analist", "Data Integrity Specialist", "Data Steward",
        "Data Strategy Lead", "Data Management Officer", "Quantitative Trader",
        "Data Management Professional", "Quantitative Risk Analyst",
        "AI Data Scientist", "Data Management Technician", "Power BI Expert",
        "Data & Analytics Specialist", "Data Visualization Lead",
        "Data Management Associate", "Fraud Data Analyst", "Admin & Data Analyst",
        "AI Governance Lead", "Data Reporter", "Data & Analytics Analyst",
        "Power BI Administrator", "Data Consultant", "Research Analyst",
        "Data Governance Consultant", "Cientista de Dados", "Advanced Data Analyst",
        "Quant Trader", "Data Analytics Business Partner", "Data Quality Expert",
        "BI & Data Analyst", "Risk Analyst", "Data Scientist Manager",
        "Data Management Consultant", "Data and Analytics Consultant",
    ],
    "Software Developer": [
        "Engineer", "SAS Developer", "Application Developer", "Java Developer",
        "Director of Engineering", "DevOps Lead", "Web Developer",
        "Chatbot Developer", "Cloud Developer",
    ],
    "Researcher": [
        "AI Researcher", "Bioinformatician", "Research Specialist",
        "Principal Researcher", "Machine Learning Researcher", "Research Assistant",
        "Postdoctoral Researcher", "Psychometrician", "Research Professional",
        "Postdoctoral Scholar", "Bioinformatics Scientist",
        "Postdoctoral Research Fellow", "Bioinformatics Specialist",
        "AI Research Scientist", "Cheminformatics Scientist",
    ],
    "Other": [
        "Business Development Representative", "Solution Specialist",
        "AI Product Specialist", "Cdd", "Technical Recruiter", "Content Writer",
        "Trainee", "Head of Marketing", "Technical Consultant",
        "Director of Product Management", "Product Specialist",
        "AIRS Solutions Specialist", "QA Tutor Reviewer", "Technical Specialist",
        "Clinical Aide", "Systems Administrator", "Copywriter",
        "Marketing Science Partner", "Sales Development Representative",
        "Data Product Lead", "Data Operator", "Bear Robotics", "AI Content Writer",
        "Technical Support Specialist", "System Administrator", "AI Strategist",
        "Enterprise Account Executive", "Salesforce Administrator",
        "Network Engineer", "Stage", "Alternance",
    ],
}

CATEGORIES = {}
for category, titles in GROUPS.items():
    for title in titles:
        CATEGORIES[title] = category


def wash_job_titles(df):
    out = df.copy()
    out["job_title_clean"] = out["job_title"].replace(FIXES)
    out["job_category"] = out["job_title"].map(CATEGORIES)
    return out

if __name__ == '__main__':
    df = pd.read_csv("Salaries.csv", index_col=0)
    result = wash_job_titles(df)
    print(result.loc[result["job_title"] == "Data Analist", ["job_title", "job_title_clean"]].drop_duplicates())