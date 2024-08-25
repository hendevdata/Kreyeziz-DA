# Social Media Engagement Analysis App

This Streamlit app provides a comprehensive tool for analyzing social media engagement data. The app is designed to load engagement metrics from an Excel file and provide insights through various analyses, including trends over time, daily averages, weekly engagement trends, top-performing content, and monthly comparisons.

## Features

### 1. Data Overview
- **Initial Data Display**: View the first few rows of your dataset to understand its structure and contents.
  
### 2. Trends in Engagement Metrics
- **Trend Analysis**: Visualize trends in video views, profile views, likes, comments, and shares over time. This helps identify patterns and fluctuations in your engagement data.

### 3. Daily Averages
- **Daily Averages Display**: Calculate and display the average daily engagement metrics, giving you insights into the typical daily performance of your content.
- **Bar Chart Visualization**: Visual representation of daily averages for easier comparison across metrics.

### 4. Weekly Engagement Trends
- **Weekly Trends Visualization**: See how your engagement metrics fluctuate on a weekly basis, allowing you to identify high-performing weeks and analyze the factors behind them.

### 5. Top Performing Content
- **Engagement Score Calculation**: Identify the top-performing content by calculating an engagement score based on video views, likes, comments, and shares.
- **Top Content Display**: List and highlight the top 10 pieces of content based on their engagement score.

### 6. Monthly Comparison
- **Monthly Engagement Comparison**: Compare the total engagement metrics between the last month and the previous month to track growth or decline in engagement.
  
### 7. Daily Breakdown of Engagement
- **Daily Breakdown**: Provide a detailed day-by-day comparison of engagement metrics for the last and previous month.

## How to Use the App

1. **Upload the Data**: Place your Excel file (`Overview.xlsx`) in the root folder of the project or upload it directly through the Streamlit interface.
2. **Run the App**:
   - Install the required Python packages:
     ```bash
     pip install streamlit pandas matplotlib openpyxl
     ```
   - Run the Streamlit app:
     ```bash
     streamlit run app.py
     ```
3. **Explore the Insights**:
   - Navigate through the different sections of the app to explore trends, averages, top content, and monthly comparisons.

## File Structure

- **app.py**: The main Streamlit app script.
- **Overview.xlsx**: The Excel file containing the social media engagement data. This should be placed in the root directory.

## Prerequisites

- **Python 3.7+**
- **Streamlit**
- **Pandas**
- **Matplotlib**
- **Openpyxl** (for reading Excel files)

## Installation

Install the necessary Python packages using pip:

```bash
pip install streamlit pandas matplotlib openpyxl
