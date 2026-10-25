import pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

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

# --- Ramlah: rows 142-282 ---

role_family_rules = {
    "Other / Unclassified": [
        "other",
        "unclassified",
        "associate",
        "executive",
        "trainee",
        "apprentice",
        "intern",
        "consultant",
        "customer success",
        "account executive",
        "business development",
        "technical writer",
        "content writer",
        "copywriter",
        "recruiter",
        "commercial counsel",
        "product designer",
        "product manager",
        "product owner",
        "project manager",
        "technical project manager",
        "sales engineer",
        "sales representative",
        "clinical aide",
        "data operator",
        "data archivist",
        "data steward",
        "data management",
        "data management specialist",
        "data management coordinator",
        "data management professional",
        "data management officer",
        "data management technician",
        "data management associate",
        "master data management",
        "master data specialist",
        "data governance",
        "data governance specialist",
        "data governance consultant",
        "data governance lead",
        "data governance manager",
        "data governance analyst",
        "data governance architect",
        "data governance engineer",
        "data quality",
        "data integrity",
        "data operations",
        "data operations associate",
        "data operations specialist",
        "data operations analyst",
        "data operations manager",
        "data operations lead",
        "data operations engineer",
        "data product owner",
        "data product manager",
        "data product lead",
        "data product specialist",
        "data strategist",
        "data strategy manager",
        "data strategy lead",
        "data team lead",
        "data lead",
        "data consultant",
        "data and analytics consultant",
        "data analytics business partner",
        "data specialist",
        "data integrity specialist",
        "data quality specialist",
        "data quality expert",
        "data quality manager",
        "data quality lead",
        "safety data management",
        "encounter data management",
        "clinical data operator",
        "principal application delivery consultant",
        "technology integrator",
        "integration specialist",
        "developer advocate",
        "business analyst",
        "business insights manager",
        "business intelligence manager",
        "head of business intelligence",
        "director of business intelligence",
        "head of data",
        "director of data",
        "data analytics manager",
        "analytics manager",
        "analytics engineering manager",
        "marketing analytics manager",
        "advanced analytics manager",
        "data science manager",
        "data strategy manager",
        "director of engineering",
        "engineering manager",
        "director of product management",
        "director",
        "manager",
        "head of marketing",
        "business development manager",
        "business development representative",
        "sales development representative",
        "customer success manager",
        "commercial counsel",
        "product specialist",
        "solution specialist",
        "technical specialist",
        "technical consultant",
        "technical support specialist",
        "technical support engineer",
        "technical recruiter",
        "qa tutor reviewer",
        "stage",
        "alternance",
        "cdd",
        "bear robotics",
    ],

    "Data Analyst": [
        "data analyst",
        "data analist",
        "data analysis specialist",
        "data analysis",
        "data analytics specialist",
        "data analytics associate",
        "data analytics developer",
        "data analytics consultant",
        "data analytics lead",
        "data analytics team lead",
        "data and reporting analyst",
        "data reporting analyst",
        "data reporting specialist",
        "data reporter",
        "data visualization analyst",
        "data visualization specialist",
        "data visualization expert",
        "data visualization developer",
        "data visualization designer",
        "data visualization engineer",
        "data visualization lead",
        "data quality analyst",
        "data integrity analyst",
        "data management analyst",
        "data product analyst",
        "data operations analyst",
        "data analytics business partner",
        "data and reporting professional",
        "admin & data analyst",
        "fraud data analyst",
        "lead data analysis",
        "lead data analyst",
        "staff data analyst",
        "principal data analyst",
        "data analyst lead",
        "lead analyst",
        "insight analyst",
        "analytics analyst",
        "analytics specialist",
        "product analyst",
        "marketing analyst",
        "marketing data analyst",
        "financial data analyst",
        "finance data analyst",
        "sales data analyst",
        "people data analyst",
        "compliance data analyst",
        "pricing analyst",
        "actuarial analyst",
        "actuary",
        "quantitative analyst",
        "quantitative risk analyst",
        "quant options trader",
        "quantitative trader",
        "quant trader",
        "experienced quantitative strategist",
        "risk analyst",
        "economist",
        "statistician",
        "psychometrician",
        "statistical programmer",
        "principal statistical programmer",
        "sas developer",
        "business analyst",
        "business data analyst",
        "advanced data analyst",
        "crm data analyst",
        "bi data analyst",
        "business intelligence data analyst",
        "business intelligence analyst",
        "bi analyst",
        "bi & data analyst",
        "data & analytics analyst",
        "data & analytics specialist",
        "data and analytics",
        "power bi",
        "power bi developer",
        "power bi consultant",
        "power bi specialist",
        "power bi expert",
        "power bi administrator",
        "tableau developer",
        "business intelligence specialist",
        "business intelligence consultant",
        "business intelligence developer",
        "business intelligence lead",
        "business intelligence",
        "bi developer",
        "bi engineer",
        "business intelligence engineer",
        "business intelligence manager",
        "head of business intelligence",
        "director of business intelligence",
        "data visualization",
    ],

    "Data Engineer": [
        "data engineer",
        "data engineering",
        "lead data engineer",
        "principal data engineer",
        "staff data engineer",
        "cloud data engineer",
        "azure data engineer",
        "aws data engineer",
        "big data engineer",
        "platform data engineer",
        "data platform engineer",
        "data infrastructure engineer",
        "data integration engineer",
        "data integration developer",
        "data integration specialist",
        "data integration lead",
        "data integration coordinator",
        "data pipeline engineer",
        "data devops engineer",
        "dataops engineer",
        "data operations engineer",
        "data analytics engineer",
        "analytics engineer",
        "etl engineer",
        "etl developer",
        "scala spark developer",
        "databricks engineer",
        "cloud database engineer",
        "database engineer",
        "data developer",
        "data integrator",
        "software data engineer",
        "bi data engineer",
        "marketing data engineer",
        "ai data engineer",
        "data engineering lead",
        "big data developer",
        "data modeler",
        "data modeller",
        "data integration",
        "data infrastructure",
        "data pipeline",
        "data engineering manager",
    ],

    "Data Scientist": [
        "data scientist",
        "data science",
        "applied data scientist",
        "staff data scientist",
        "principal data scientist",
        "lead data scientist",
        "data scientist expert",
        "data scientist associate",
        "data scientist manager",
        "marketing data scientist",
        "ai data scientist",
        "decision scientist",
        "cientista de dados",
        "advanced analytics scientist",
    ],

    "ML Engineer": [
        "machine learning engineer",
        "ml engineer",
        "machine learning software engineer",
        "machine learning platform engineer",
        "machine learning infrastructure engineer",
        "ml infrastructure engineer",
        "mlops",
        "machine learning ops",
        "machine learning performance engineer",
        "machine learning model engineer",
        "machine learning quality engineer",
        "machine learning developer",
        "machine learning specialist",
        "machine learning tech lead",
        "machine learning lead",
        "machine learning manager",
        "machine learning engineering lead",
        "ai machine learning engineer",
        "applied machine learning engineer",
        "deep learning engineer",
        "machine learning modeler",
        "machine learning model",
        "ml infrastructure",
    ],

    "Research Scientist": [
        "research scientist",
        "ai research scientist",
        "research engineer",
        "machine learning researcher",
        "machine learning research engineer",
        "deep learning researcher",
        "ai researcher",
        "researcher",
        "research fellow",
        "research associate",
        "research assistant",
        "research specialist",
        "research professional",
        "research analyst",
        "research team lead",
        "principal researcher",
        "postdoctoral",
        "post doctoral",
        "post-doctoral",
        "applied research scientist",
        "applied scientist",
        "computational scientist",
        "principal scientist",
        "ml scientist",
        "machine learning scientist",
        "ai scientist",
        "bioinformatics scientist",
        "cheminformatics scientist",
        "computational biologist",
        "bioinformatician",
        "quantitative researcher",
        "quantitative research analyst",
        "marketing science partner",
        "research data manager",
        "postdoctoral researcher",
        "postdoctoral fellow",
        "postdoctoral scholar",
        "postdoctoral research fellow",
    ],

    "AI Engineer": [
        "artificial intelligence engineer",
        "ai engineer",
        "ai software engineer",
        "ai software development engineer",
        "ai developer",
        "ai programmer",
        "ai specialist",
        "ai tech lead",
        "ai lead",
        "lead ai engineer",
        "applied ai ml lead",
        "ai solutions lead",
        "ai solutions consultant",
        "ai solutions specialist",
        "ai product specialist",
        "ai solution director",
        "ai product lead",
        "ai product owner",
        "ai product manager",
        "forward deployed engineer",
        "robotics engineer",
        "robotics software engineer",
        "automation engineer",
        "rpa developer",
        "autonomous vehicle",
        "creative technologist",
        "algorithm developer",
        "conversational ai designer",
        "chatbot developer",
        "prompt engineer",
        "llm engineer",
        "ai research engineer",
        "ai machine learning engineer",
    ],

    "Analytics Manager": [
        "analytics manager",
        "analytics engineering manager",
        "data analytics manager",
        "advanced analytics manager",
        "marketing analytics manager",
        "business intelligence manager",
        "head of business intelligence",
        "director of business intelligence",
        "head of data",
        "director of data",
        "data science manager",
        "data strategy manager",
        "business insights manager",
        "data analytics team lead",
        "data analytics lead",
        "analytics lead",
        "data strategy lead",
        "data lead",
        "data team lead",
    ],

    "AI Architect": [
        "ai architect",
        "genai architect",
        "ml architect",
        "machine learning architect",
        "ai solution architect",
        "ai solutions architect",
        "data governance architect",
        "data architect",
        "cloud data architect",
        "principal data architect",
        "big data architect",
        "it enterprise data architect",
        "aws data architect",
        "cloud architect",
        "solutions architect",
        "solution architect",
        "principal software architect",
        "software architect",
        "technical architect",
        "power bi architect",
        "director of artificial intelligence",
        "head of ai",
        "head of applied ai",
        "head of machine learning",
    ],

    "Computer Vision": [
        "computer vision",
        "machine vision",
        "vision engineer",
    ],

    "NLP": [
        "nlp",
        "natural language",
        "natural language processing",
    ],

    "Software Engineer": [
        "software engineer",
        "software developer",
        "software development engineer",
        "backend engineer",
        "backend developer",
        "backend software engineer",
        "frontend engineer",
        "front end engineer",
        "full stack engineer",
        "full stack developer",
        "fullstack engineer",
        "web developer",
        "web and multimedia developer",
        "java developer",
        "python developer",
        "application developer",
        "applications programmer",
        "application programmer",
        "developer",
        "principal engineer",
        "staff engineer",
        "lead engineer",
        "member of technical staff",
        "application developer",
        "application programmer",
        "integration developer",
        "quantitative developer",
        "cloud developer",
        "software architect",
        "software development",
    ],

    "DevOps & Infrastructure Engineer": [
        "devops engineer",
        "devops lead",
        "site reliability engineer",
        "infrastructure engineer",
        "cloud engineer",
        "cloud developer",
        "platform engineer",
        "systems engineer",
        "system engineer",
        "systems administrator",
        "system administrator",
        "cloud database administrator",
        "elasticsearch administrator",
        "infrastructure",
        "platform infrastructure",
    ],

    "Database & Network Engineer": [
        "database administrator",
        "database engineer",
        "cloud database engineer",
        "cloud database administrator",
        "database designer",
        "database architect",
        "network engineer",
        "network specialist",
        "computer network",
        "database and network",
    ],
}

CATEGORIES = {}
for group in [role_family_rules]:
    for category, titles in group.items():
        for title in titles:
            CATEGORIES[title] = category


def _wash_job_titles(df):
    out = df.copy()

    out["job_title_clean"] = out["job_title"].replace(FIXES)

    normalized_titles = (
        out["job_title_clean"]
        .str.strip()
        .str.lower()
    )

    out["job_category"] = normalized_titles.map(CATEGORIES)

    out["job_category"] = out["job_category"].fillna(
        "Other / Unclassified"
    )
    return out


def _drop_duplicates(df):
    before = len(df)
    df = df.drop_duplicates()
    print(f"Dropped {before - len(df)} exact duplicate rows ({len(df)} remaining)")
    return df


def _decode_abbrevations(df):
    experience_map = {
        "EN": "Entry-level",
        "MI": "Mid-level",
        "SE": "Senior-level",
        "EX": "Executive-level",
    }
    employment_map = {
        "FT": "Full-time",
        "PT": "Part-time",
        "CT": "Contract",
        "FL": "Freelance",
    }
    remote_map = {
        0: "On-site",
        50: "Hybrid",
        100: "Remote",
    }

    if "experience_level" in df.columns:
        df["experience_level_label"] = df["experience_level"].map(experience_map).fillna(df["experience_level"])
    if "employment_type" in df.columns:
        df["employment_type_label"] = df["employment_type"].map(employment_map).fillna(df["employment_type"])
    if "remote_ratio" in df.columns:
        df["work_mode"] = df["remote_ratio"].map(remote_map).fillna(df["remote_ratio"].astype(str))
    return df

def _parse_year_ensure_numeric(df):
    if "work_year" in df.columns:
        df["work_year"] = pd.to_numeric(df["work_year"], errors="coerce").astype("Int64")

    df["salary_in_usd"] = pd.to_numeric(df["salary_in_usd"], errors="coerce")

    before = len(df)
    df = df.dropna(subset=["salary_in_usd"])
    print(f"Dropped {before - len(df)} rows with missing/invalid salary_in_usd")

    return df

def _flag_outliers(df):
    q1, q3 = df["salary_in_usd"].quantile([0.25, 0.75])
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    df["salary_outlier_flag"] = ~df["salary_in_usd"].between(lower_bound, upper_bound)
    print(f"IQR bounds: [{lower_bound:,.0f}, {upper_bound:,.0f}] USD")
    print(
        f"Flagged {df['salary_outlier_flag'].sum()} rows ({df['salary_outlier_flag'].mean():.1%}) as statistical outliers")
    return df

def wash_data(df):
    df = _drop_duplicates(df)
    df = _wash_job_titles(df)
    df = _decode_abbrevations(df)
    df = _parse_year_ensure_numeric(df)
    df = _flag_outliers(df)

    return df



