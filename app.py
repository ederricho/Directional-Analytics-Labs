import streamlit as st
import pandas as pd
from database import get_predictions
from database import get_month
from database import get_graph_data
import plotly.express as px
from datetime import date

# Get Predictions
df = get_predictions()

#st.dataframe(df.head()) # <-------------------------------------- Displays the Predictions Table


st.title("Directional Analytics Labs") # <----------------------- Title Page of URL



#st.subheader("Today's Forecasts") # <---------------------------- Today's Forecasts
# --- Code -----


st.subheader("Ten Day Model Perfomance") # <--------------- Model Performances for the Month
pred_df = get_month()

# Add Correct Column
pred_df["Correct"] = (
    pred_df["ActualDirection"] == pred_df["Prediction"]
).astype(int)

# Compute Acc By Stock
stock_accuracy = (
    pred_df.groupby(["StockID", "ModelName"])["Correct"]
      .mean()
      .reset_index()
)

# Rename the Column
stock_accuracy.rename(
    columns = {"Correct":"Accuracy"},
    inplace = True
)

# Convert IDs to Ticker Symbols
ticker_map = {
    1: "BAC",
    2: "TFC",
    3: "WFC"
}

stock_accuracy["Ticker"] = (
    stock_accuracy["StockID"]
    .map(ticker_map)
)

# Display
accuracy_pivot = stock_accuracy.pivot(
    index="ModelName",
    columns="StockID",
    values="Accuracy"
)

# Rename the Column
accuracy_pivot.rename(
    columns = {1:"BAC", 2:"TFC", 3:"WFC"},
    inplace = True
)


st.dataframe(accuracy_pivot)


# =================================
# ======== 60 Day Graph ===========

import pandas as pd
import plotly.express as px
import streamlit as st

# Section Title
st.title("60 Day Model Performance")

# ==========================================
# ===== Query Data from Database ===========
# ==========================================

graph_df = get_graph_data()

# ==========================================
# ===== Create Accuracy Variable ===========
# ==========================================

# 1 = Correct Prediction
# 0 = Incorrect Prediction
graph_df["Correct"] = (
    graph_df["Prediction"] == graph_df["ActualDirection"]
).astype(int)

# ==========================================
# ===== Prepare Date Field =================
# ==========================================

# Ensure dates are recognized as dates
graph_df["PredDate"] = pd.to_datetime(
    graph_df["PredDate"]
)

# Sort data before calculating rolling metrics
graph_df = graph_df.sort_values(
    ["StockID", "ModelName", "PredDate"]
)

# ==========================================
# ===== Calculate Rolling Accuracy =========
# ==========================================

# Rolling 60-day accuracy for each stock/model combination
graph_df["RollingAccuracy60"] = (
    graph_df.groupby(
        ["StockID", "ModelName"]
    )["Correct"]
    .transform(
        lambda x: x.rolling(
            window=60,
            min_periods=60
        ).mean()
    )
)

# Remove rows where rolling accuracy does not yet exist
graph_df = graph_df.dropna(
    subset=["RollingAccuracy60"]
)

# ==========================================
# ===== Stock Selector =====================
# ==========================================

stock = st.selectbox(
    "Select Stock",
    ["BAC", "TFC", "WFC"]
)

# Map ticker symbol to StockID
stock_map = {
    "BAC": 1,
    "TFC": 2,
    "WFC": 3
}

# Filter dataframe to selected stock
graph_df = graph_df[
    graph_df["StockID"] == stock_map[stock]
]

# ==============================
# ===== Timeframe Selector =====
days = st.selectbox(
    "Display Period",
    [30, 60, 90, 180]
)

latest_date = graph_df["PredDate"].max()

graph_df = graph_df[
    graph_df["PredDate"] >= latest_date - pd.Timedelta(days=days)
]


# ==========================================
# ===== Create Plotly Graph ================
# ==========================================

fig = px.line(
    graph_df,
    x="PredDate",
    y="RollingAccuracy60",
    color="ModelName",
    title=f"60 Day Rolling Accuracy - {stock}"
)

# Optional formatting
fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Accuracy",
    yaxis_tickformat=".0%"
)

# ==========================================
# ===== Display Graph ======================
# ==========================================

st.plotly_chart(
    fig,
    use_container_width=True
)

# Model Selectior
#model = st.selectbox(
#    "Model",
#    graph_df["ModelName"].unique()
#)

# KPI Cards at the Top
#st.metric(
#    label="Current Accuracy",
#    value=f"{latest_accuracy:.1%}"
#)

st.subheader("Overall Accuracy")

# Table Below the Graph
accuracy_table = (
    graph_df.groupby("ModelName")["Correct"]
    .mean()
    .reset_index()
)
st.dataframe(accuracy_table)