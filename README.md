# CSV to Postgres Pipeline

A simple pipeline to clean and load TLC trip record data into a PostgreSQL database.

## Features

- Removes duplicate rows
- Filters out NaN values
- Loads cleaned data into PostgreSQL
- Built with FastAPI, Pandas, and Poetry

## Usage

1. **Install dependencies:**
   ```bash
   poetry install
   ```

2. **Run the FastAPI app:**
   ```bash
   poetry run uvicorn main:app --reload
   ```

3. **Upload your CSV via the API** to clean and load it into the database.

## Dataset

This pipeline processes the [TLC Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page).

## Requirements

* Python 3.8+
* PostgreSQL database

## Notes

* Configure your database connection string in the application before running the app.