import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus


def get_predictions():
    
    server = "dalserver.database.windows.net"
    database = "DLA_StockPrediction"
    username = "eDerricho"
    password = "iLoveazure@33"

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

    server = "dalserver.database.windows.net"
    database = "DLA_StockPrediction"
    username = "eDerricho"
    password = "iLoveazure@33"

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
    server = "dalserver.database.windows.net"
    database = "DLA_StockPrediction"
    username = "eDerricho"
    password = "iLoveazure@33"

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
    server = "dalserver.database.windows.net"
    database = "DLA_StockPrediction"
    username = "eDerricho"
    password = "iLoveazure@33"

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
   
