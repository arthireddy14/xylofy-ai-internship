import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Sales Forecasting Dashboard", layout="wide")

# -----------------------------
# Load Data
# -----------------------------
df = pd.read_csv("train.csv")
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)

forecast_df = pd.read_csv("forecast_results.csv")
anomaly_df = pd.read_csv("anomaly_results.csv")
cluster_df = pd.read_csv("cluster_results.csv")

# Convert anomaly dates
if "Order Date" in anomaly_df.columns:
    anomaly_df["Order Date"] = pd.to_datetime(
        anomaly_df["Order Date"],
        errors="coerce"
    )

# -----------------------------
# Sidebar
# -----------------------------
page = st.sidebar.radio(
    "Navigation",
    [
        "Sales Overview",
        "Forecast Explorer",
        "Anomaly Report",
        "Demand Segments"
    ]
)

# ======================================================
# PAGE 1
# ======================================================

if page == "Sales Overview":

    st.title("📊 Sales Overview Dashboard")

    df["Year"] = df["Order Date"].dt.year

    region = st.selectbox(
        "Select Region",
        ["All"] + sorted(df["Region"].unique())
    )

    category = st.selectbox(
        "Select Category",
        ["All"] + sorted(df["Category"].unique())
    )

    filtered = df.copy()

    if region != "All":
        filtered = filtered[
            filtered["Region"] == region
        ]

    if category != "All":
        filtered = filtered[
            filtered["Category"] == category
        ]

    st.subheader("Total Sales by Year")

    yearly = (
        filtered.groupby("Year")["Sales"]
        .sum()
    )

    fig, ax = plt.subplots(figsize=(8,4))
    yearly.plot(kind="bar", ax=ax)
    ax.set_ylabel("Sales")
    st.pyplot(fig)

    st.subheader("Monthly Sales Trend")

    monthly = (
        filtered.groupby(
            pd.Grouper(
                key="Order Date",
                freq="ME"
            )
        )["Sales"]
        .sum()
    )

    fig, ax = plt.subplots(figsize=(10,4))
    monthly.plot(ax=ax)
    ax.set_ylabel("Sales")
    st.pyplot(fig)

# ======================================================
# PAGE 2
# ======================================================

elif page == "Forecast Explorer":

    st.title("📈 Forecast Explorer")

    segment = st.selectbox(
        "Select Category / Region",
        forecast_df["Segment"]
    )

    months = st.slider(
        "Forecast Horizon",
        1,
        3,
        3
    )

    selected = forecast_df[
        forecast_df["Segment"] == segment
    ]

    values = [
        selected["Month 1"].values[0],
        selected["Month 2"].values[0],
        selected["Month 3"].values[0]
    ]

    values = values[:months]

    fig, ax = plt.subplots(figsize=(8,4))

    ax.plot(
        range(1, months+1),
        values,
        marker="o",
        linewidth=2
    )

    ax.set_xlabel("Forecast Month")
    ax.set_ylabel("Sales")

    st.pyplot(fig)

    st.subheader("Forecast Values")

    st.dataframe(selected)

    col1, col2 = st.columns(2)

    with col1:
        st.metric("MAE", "14537.39")

    with col2:
        st.metric("RMSE", "17093.03")

# ======================================================
# PAGE 3
# ======================================================

elif page == "Anomaly Report":

    st.title("🚨 Anomaly Report")

    weekly = (
        df.groupby(
            pd.Grouper(
                key="Order Date",
                freq="W"
            )
        )["Sales"]
        .sum()
        .reset_index()
    )

    fig, ax = plt.subplots(figsize=(12,5))

    ax.plot(
        weekly["Order Date"],
        weekly["Sales"],
        label="Weekly Sales"
    )

    ax.scatter(
        anomaly_df["Order Date"],
        anomaly_df["Sales"],
        color="red",
        s=80,
        label="Anomaly"
    )

    ax.legend()

    st.pyplot(fig)

    st.subheader("Detected Anomalies")

    st.dataframe(
        anomaly_df[
            ["Order Date", "Sales"]
        ]
    )

# ======================================================
# PAGE 4
# ======================================================

elif page == "Demand Segments":

    st.title("📦 Product Demand Segments")

    fig, ax = plt.subplots(figsize=(8,6))

    sns.scatterplot(
        data=cluster_df,
        x="PC1",
        y="PC2",
        hue="Segment",
        s=120,
        ax=ax
    )

    st.pyplot(fig)

    st.subheader("Cluster Table")

    if "Sub-Category" in cluster_df.columns:

        st.dataframe(
            cluster_df[
                ["Sub-Category", "Segment"]
            ]
        )

    else:

        st.dataframe(cluster_df)