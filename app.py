import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to load the Excel file from the root folder
def load_data(file_name):
    df = pd.read_excel(file_name, sheet_name='SheetJS')
    df['Date'] = pd.to_datetime(df['Date'].astype(str) + ' 2024', format='%B %d %Y', errors='coerce')
    df.set_index('Date', inplace=True)
    return df

# Function to calculate engagement score
def calculate_engagement_score(df):
    df['Engagement Score'] = (
        df['Video Views'] * 0.5 + 
        df['Likes'] * 0.3 + 
        df['Comments'] * 0.1 + 
        df['Shares'] * 0.1
    )
    return df

# Load data from the root folder
st.title('Social Media Engagement Analysis')
file_name = 'Overview.xlsx'

try:
    df = load_data(file_name)
    
    # Display initial data
    st.subheader('Data Overview')
    st.write(df.head())

    # Trends Analysis
    st.subheader('Trends in Engagement Metrics Over Time')
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['Video Views'], label='Video Views')
    plt.plot(df.index, df['Profile Views'], label='Profile Views')
    plt.plot(df.index, df['Likes'], label='Likes')
    plt.plot(df.index, df['Comments'], label='Comments')
    plt.plot(df.index, df['Shares'], label='Shares')
    plt.xlabel('Date')
    plt.ylabel('Count')
    plt.title('Trends in Engagement Metrics Over Time')
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)

    # Daily Averages
    st.subheader('Daily Averages of Engagement Metrics')
    daily_averages = df.mean()
    st.write(daily_averages)

    # Visualize Daily Averages
    st.bar_chart(daily_averages)

    # Weekly Engagement Trends
    st.subheader('Weekly Engagement Trends')
    weekly_trends = df.resample('W').sum()
    plt.figure(figsize=(12, 6))
    plt.plot(weekly_trends.index, weekly_trends['Video Views'], label='Video Views')
    plt.plot(weekly_trends.index, weekly_trends['Profile Views'], label='Profile Views')
    plt.plot(weekly_trends.index, weekly_trends['Likes'], label='Likes')
    plt.plot(weekly_trends.index, weekly_trends['Comments'], label='Comments')
    plt.plot(weekly_trends.index, weekly_trends['Shares'], label='Shares')
    plt.xlabel('Week')
    plt.ylabel('Total Count')
    plt.title('Weekly Engagement Trends')
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)

    # Calculate and Display Top Content
    df = calculate_engagement_score(df)
    st.subheader('Top Performing Content Based on Engagement Score')
    top_content = df.sort_values(by='Engagement Score', ascending=False).head(10)
    st.write(top_content)

    # Monthly Comparison
    st.subheader('Monthly Engagement Comparison')
    last_month = df.index.max().month
    last_month_data = df[df.index.month == last_month]
    previous_month = last_month - 1 if last_month > 1 else 12
    previous_month_data = df[df.index.month == previous_month]
    last_month_totals = last_month_data.sum()
    previous_month_totals = previous_month_data.sum()
    comparison_df = pd.DataFrame({
        'Last Month (Total)': last_month_totals,
        'Previous Month (Total)': previous_month_totals
    })
    st.write(comparison_df)

    # Daily Breakdown for Last and Previous Month
    st.subheader('Daily Breakdown of Engagement')
    daily_breakdown_last_month = last_month_data.resample('D').sum()
    daily_breakdown_previous_month = previous_month_data.resample('D').sum()
    daily_comparison_df = pd.concat([daily_breakdown_last_month, daily_breakdown_previous_month], axis=1, keys=['Last Month', 'Previous Month'])
    st.write(daily_comparison_df)

except FileNotFoundError:
    st.error(f"The file '{file_name}' was not found in the root folder. Please ensure the file is in the correct location.")
