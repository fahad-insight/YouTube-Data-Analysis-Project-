# YouTube-Data-Analysis-Project-
YouTube API data extraction + Saving in Excel with further Analysis in Power BI

# 📊 YouTube Data Engineering Pipeline (API → Python → Excel → Power BI)

## 🚀 Project Overview

This project is an end-to-end **data pipeline** that extracts YouTube video data using the YouTube Data API v3, processes it using Python, and prepares it for analysis in Power BI.

The focus of this project is not just visualization, but building a complete workflow for **data extraction, transformation, and analysis (ETL-style pipeline)**.

---

## ⚙️ Pipeline Architecture

YouTube API v3 → Python Script → Data Cleaning & Structuring → Excel Dataset → Power BI Analysis

---

## 🧠 Key Objectives

- Extract real-time YouTube video data using API
- Automate data collection using Python
- Transform raw JSON data into structured tabular format
- Store cleaned data in Excel for analysis
- Enable downstream analytics using Power BI

---

## 🛠️ Tools & Technologies

- Python
- YouTube Data API v3
- Pandas
- OpenPyXL
- Excel
- Power BI
- Google API Client Library

---

## 📂 Project Structure

```
YouTube-Data-Pipeline/
│
├── data/
│   └── Python Script.py
│   └── youtube_data.xlsx
|
├── powerbi/
│   └── report.pbix
│
├── images/
    └── pipeline_diagram.png

---

## ⚙️ How the Pipeline Works

### 1. Data Extraction
- Connects to YouTube Data API v3
- Fetches video-level metadata such as:
  - Video Title
  - Views
  - Likes
  - Comments
  - Publish Date

### 2. Data Processing (Python)
- Converts raw API response into structured format
- Cleans missing or inconsistent values
- Organizes data into a tabular dataset

### 3. Data Storage
- Stores processed data into an Excel file
- Acts as a staging layer for analytics

### 4. Data Analysis (Power BI)
- Dataset is imported into Power BI
- Used for exploratory and trend analysis

## 📊 Key Insights Enabled by This Pipeline

- Identification of top-performing videos
- Relationship between views and engagement
- Detection of high-traffic but low-engagement content
- Content performance trends over time
- Channel performance evaluation
  
## 🎯 What This Project Demonstrates

- Real-world **data pipeline design**
- API integration and automation
- Data cleaning and transformation skills
- Structured data engineering workflow
- Basic analytics readiness for BI tools

## 📌 Future Improvements

- Automate pipeline using scheduled runs (cron / task scheduler)
- Store data in a database instead of Excel
- Add streaming support for real-time analytics
- Build a cloud-based version (AWS / GCP)

## 📜 License

This project is licensed under the MIT License.
