(This project is currently in development. Check back soon for updated visualizations and insights.)

## 🔽 Get the data

Raw A&E time-series files are **not stored** in this repo. Download them from the official sources:

- **NHS England — A&E Attendances & Emergency Admissions (monthly/weekly):**  
  https://www.england.nhs.uk/statistics/statistical-work-areas/ae-waiting-times-and-activity/

- **NHS Digital — A&E publications index:**  
  https://digital.nhs.uk/data-and-information/publications/statistical/nhse-ae-attendances-and-emergency-admissions

Save the downloaded Excel/CSV into:

data/raw/

(kept out of Git on purpose). Code reads from `data/raw/` and writes cleaned outputs to `data/processed/`.




# NHS Emergency Data Analysis 🚑📊

This project analyzes over a decade of NHS A&E attendance and emergency admission data in England. It focuses on time trends, COVID-19 impact, and operational performance metrics — built to demonstrate digital and analytical competency to potential employers.

## 🧠 Objective

Create a clear, professional, and analytical project to showcase:
- Data cleaning and wrangling (raw `.xls` to clean DataFrame)
- Exploratory data analysis (EDA) with time series insights
- Data visualization using Matplotlib
- Insightful storytelling around healthcare trends

## 📁 Structure
nhs-emergency-data/
├── 01-data-cleaning.ipynb # Clean & structure raw NHS data
├── data/
│ └── raw/
│ └── Monthly-AE-Time-Series-June-2025-1-1.xls
├── src/
│ └── load_clean.py # Python function for reusable cleaning
├── .gitignore
├── README.md
└── requirements.txt

## 📊 Data Overview

- **Source:** NHS England - A&E Attendances & Emergency Admissions (monthly)
- **Date Range:** August 2010 – Present
- **Granularity:** England-wide monthly counts by department type
- **Format:** `.xls` with metadata and 14+ operational columns

## 🔧 Features

- Skips metadata rows automatically (Excel `skiprows=15`)
- Cleans and standardizes column names
- Converts period columns to datetime
- Handles missing values and drops empty rows/columns
- Visualizes total A&E attendances over time

## 🛠️ Tech Stack

- Python 3.x
- Pandas
- Matplotlib
- Jupyter Notebook
- xlrd (for reading .xls files)

## 📈 Example Visual

![Total A&E Attendances Over Time](./assets/ae_attendance_trend.png)  
*Attendance drop during 2020 COVID-19 lockdowns clearly visible.*

## 🚀 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/Giuseppe552/nhs-emergency-data.git
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Launch the notebook:

bash
Copy
Edit
jupyter notebook

📌 Next Steps
02-trend-analysis.ipynb → deeper statistical analysis

03-patient-waiting-time.ipynb → focus on performance KPIs

Publish a dashboard (e.g., Plotly, Streamlit)

Build PDF slides or GitHub Pages portfolio


💼 Why This Project?
This project is designed to showcase data analysis capabilities using a real-world, public-sector dataset.

Instead of using artificial data or pre-cleaned CSVs, this project demonstrates the ability to handle raw, 
messy .xls spreadsheets like those found in real health or government roles. It covers not just data cleaning, 
but full data pipeline thinking: reusable functions, modular file structure, exploratory visualizations, 
and future planning for deep analysis.

It also speaks to business impact — understanding how patient flow, emergency demand, 
and operational strain manifest in time series data. This is the kind of thinking needed in 
NHS digital roles, analytics consultancies, or any data-driven healthcare setting.

✍️ Author
Giuseppe552
