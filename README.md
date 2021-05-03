# Pandas Database Profiler

The purpose of this project is to provide a simple GUI for profiling baseline analytics from tables in a database.
Once a database connection has been established a user can select any table in the database, pandas-profiling will be run on that table with the results displayed in the streamlit UI.

This project extends the [streamlit-pandas-profiling module](https://github.com/okld/streamlit-pandas-profiling) by adding a [SQLAlchemy ORM](https://www.sqlalchemy.org/) backend which is then used to populate a table list by using [automap](https://docs.sqlalchemy.org/en/14/orm/extensions/automap.html#basic-use) in the SQLAlchemy Base object.
The streamlit-pandas-profiling project is itself an extension of the [pandas-profiling](https://github.com/pandas-profiling/pandas-profiling) and [streamlit](https://streamlit.io/) libraries.

### Setup Instructions

**Installation**

This project uses [Poetry](https://python-poetry.org/) for dependency management.
Once you have installed Poetry you can setup the project by running `poetry install` in the project directory.
A `requirements.txt` file is included f you prefer to set up your own environment with pip or another tool.

**Database Drivers**

You will have to manually install the Python database driver for your database type if it is not already present in your environment, e.g. `poetry add psycopg2` or `pip install psycopg2`.

**Environment Variables**

Following the practices recommended by the [12-factor app](https://12factor.net/config) this project store the database configuration string in an environment variable called `PANDAS_DATABASE_EXPLORER_DB_CONNECTION`.
This is a string that should match the SQLAlchemy [connection string format](https://docs.sqlalchemy.org/en/14/core/engines.html#database-urls) (Snowflake specific format can be found [here](https://docs.snowflake.com/en/user-guide/sqlalchemy.html#additional-connection-parameters)).

### Execution Instructions

If you are using Poetry you can start the project environment with `poetry shell`.
You can then start the server with `make run-server`.

### Development Instructions

The Poetry development dependencies are installed by default when you run `poetry install`. If you are using pip you can install them from the `requirements_dev.txt` file.
This project uses the pre-commit package to check commits.
You can install this hooks from this project by running `pre-commit install`.
