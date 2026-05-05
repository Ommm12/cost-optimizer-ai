import streamlit as st
import boto3
import pandas as pd
import re
from datetime import datetime
import plotly.express as px

# ------------------------
# AWS SETUP
# ------------------------
s3 = boto3.client('s3')
BUCKET_NAME = "cost-optimizer-reports-omdoifode"

# ------------------------
# PAGE CONFIG
# ------------------------
st.set_page_config(layout="wide", page_title="AWS Dashboard", page_icon="💸")

# ------------------------
# SIDEBAR (LIKE YOUR IMAGE)
# ------------------------
with st.sidebar:
    st.title("☁️ AWS DevOps")
    st.markdown("### Navigation")
    st.write("🏠 Home")
    st.write("📊 Dashboard")
    st.write("📁 Reports")
    st.write("⚙️ Settings")

# ------------------------
# HEADER
# ------------------------
st.markdown("## 💸 AWS Cost Dashboard")
st.markdown("---")

# ------------------------
# FETCH DATA FROM S3
# ------------------------
response = s3.list_objects_v2(Bucket=BUCKET_NAME)

dates, costs = [], []

if 'Contents' in response:
    for obj in response['Contents']:
        file = s3.get_object(Bucket=BUCKET_NAME, Key=obj['Key'])
        content = file['Body'].read().decode('utf-8')

        match = re.search(r"\$([0-9\.\-]+)", content)
        cost = float(match.group(1)) if match else 0

        date_str = obj['Key'].replace("report-", "").replace(".txt", "")
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d")
        except:
            continue

        dates.append(date)
        costs.append(cost)

df = pd.DataFrame({
    "Date": dates,
    "Cost": costs
}).sort_values("Date")

# ------------------------
# KPI CARDS (LIKE IMAGE TOP)
# ------------------------
col1, col2, col3, col4 = st.columns(4)

if not df.empty:
    latest = df.iloc[-1]["Cost"]
    avg = df["Cost"].mean()
    max_cost = df["Cost"].max()
    total = df["Cost"].sum()

    col1.metric("💰 Total Cost", f"${total:.2f}")
    col2.metric("📊 Avg Cost", f"${avg:.2f}")
    col3.metric("🚨 Max Cost", f"${max_cost:.2f}")
    col4.metric("📅 Latest Cost", f"${latest:.2f}")

# ------------------------
# MAIN CHART
# ------------------------
st.markdown("### 📈 Cost Overview")

fig = px.line(
    df,
    x="Date",
    y="Cost",
    markers=True,
    template="plotly_dark"
)

st.plotly_chart(fig, use_container_width=True)

# ------------------------
# SECOND ROW (LIKE IMAGE)
# ------------------------
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📊 Cost Distribution")
    pie = px.pie(df, values="Cost", names="Date", template="plotly_dark")
    st.plotly_chart(pie, use_container_width=True)

with col2:
    st.subheader("🤖 AI Insights")

if not df.empty:
    # Existing logic
    if latest > avg:
        st.error("⚠️ Cost is above average")
    else:
        st.success("✅ Cost is optimized")

    # 🔥 NEW: Trend-based AI logic
    if len(df) > 3:
        trend = df["Cost"].diff().mean()

        if trend > 5:
            st.error("🚨 Increasing cost trend detected")
        else:
            st.info("📊 Cost trend is stable")

# ------------------------
# TABLE
# ------------------------
st.markdown("### 📑 Full Reports")
st.dataframe(df, use_container_width=True)
st.write("CI/CD is working 🚀")
