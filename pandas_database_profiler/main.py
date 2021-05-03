import os

import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from streamlit_pandas_profiling import st_profile_report


def main():
    # Grab the connection string
    connection_string = os.environ["PANDAS_DATABASE_EXPLORER_DB_CONNECTION"]

    # Build a declarative base object and reflect the table metadata
    # so we don't have to build the ORM by hand
    Base = automap_base()
    engine = create_engine(connection_string)

    # Use the repr to hide the password in the database URI
    st.text(f"Connected to: {repr(engine.url)}")
    Base.prepare(engine, reflect=True)

    table_name = st.selectbox(
        "Choose a table to explore", list(Base.metadata.tables.keys())
    )

    # Query the selected table, convert to pandas, run pandas profiler
    session = Session(engine)
    df = pd.read_sql(
        session.query(Base.metadata.tables[table_name]).statement, session.bind
    )
    profile = ProfileReport(df, title=f"{table_name} Profiling Report")
    st_profile_report(profile)


if __name__ == "__main__":
    main()
