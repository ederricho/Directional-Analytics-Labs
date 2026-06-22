import pandas as pd
import streamlit as st
from sqlalchemy import create_engine
from urllib.parse import quote_plus

SERVER = st.secrets["SERVER"]
DATABASE = st.secrets["DATABASE"]
USERNAME = st.secrets["USERNAME"]
PASSWORD = st.secrets["PASSWORD"]

def get_predictions():
    
    server = st.secrets["SERVER"]
    database = st.secrets["DATABASE"]
    username = st.secrets["USERNAME"]
    password = st.secrets["PASSWORD"]

    params = quote_plus(
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password};"
    )

    engine = create_engine(
        f"mssql+pyodbc:///?odbc_connect={params}"
    )
    query = """
    SELECT *
    FROM Predictions
    """

    df = pd.read_sql(query, engine)

    return df

# Monthly Performance
def get_month():

    server = st.secrets["SERVER"]
    database = st.secrets["DATABASE"]
    username = st.secrets["USERNAME"]
    password = st.secrets["PASSWORD"]

    params = quote_plus(
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password};"
    )

    engine = create_engine(
        f"mssql+pyodbc:///?odbc_connect={params}"
    )
    query = """
    SELECT *
    FROM Predictions
    WHERE PredDate BETWEEN DATEADD(day, -11, GETDATE()) AND GETDATE();
    """

    df = pd.read_sql(query, engine)



    return df

def ninety_day():
    
    server = st.secrets["SERVER"]
    database = st.secrets["DATABASE"]
    username = st.secrets["USERNAME"]
    password = st.secrets["PASSWORD"]

    params = quote_plus(
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password};"
    )

    engine = create_engine(
        f"mssql+pyodbc:///?odbc_connect={params}"
    )

    query = """
    SELECT *
    FROM Predictions
    WHERE PredDate BETWEEN DATEADD(day, -11, GETDATE()) AND GETDATE();
    """

    df = pd.read_sql(query, engine)

    return df 

def get_graph_data(): # <================================ Get Data for 90 Day Graph

    # =============================
    # ===== Connect to Server =====
    server = st.secrets["SERVER"]
    database = st.secrets["DATABASE"]
    username = st.secrets["USERNAME"]
    password = st.secrets["PASSWORD"]

    params = quote_plus(
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password};"
    )

    engine = create_engine(
        f"mssql+pyodbc:///?odbc_connect={params}"
    )
    # ==========================
    # ===== Query for Data =====
    query = """
    SELECT *
    FROM Predictions
    """

    df = pd.read_sql(query, engine)

    return df 
   
