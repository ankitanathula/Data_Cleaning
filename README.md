# Cafe Sales Data Cleaning & Analysis

This project is a Python script that demonstrates a practical approach to cleaning, manipulating, and visualizing a "dirty" cafe sales dataset using the **pandas** and **matplotlib** libraries. The primary goal is to transform raw, inconsistent data into a clean, structured format suitable for analysis, and then to derive insights through visualizations.

***

## Dataset

The dataset used in this project is sourced from **Kagglehub**. It is intentionally designed with missing values, inconsistent data types, and erroneous entries to serve as a realistic training ground for data cleaning techniques.

* **Source:** `ahmedmohamed2003/cafe-sales-dirty-data-for-cleaning-training`

***

## Data Cleaning and Manipulation Process

The Python script systematically addresses common data quality issues through the following steps:

1.  **Data Ingestion**: The dataset is downloaded and loaded directly from Kagglehub into a pandas DataFrame.
2.  **Initial Inspection**: The script performs an initial check of the data's structure, including identifying missing values and data types, to inform the cleaning strategy.
3.  **Handling Missing Values**:
    * Rows with missing `Item` or `Transaction Date` are dropped, as these are critical identifiers for each transaction.
    * Missing numerical values in `Quantity` and `Price Per Unit` are imputed by filling them with the rounded mean of their respective columns.
    * Missing `Total Spent` values are calculated based on the imputed `Price Per Unit` and `Quantity`.
4.  **Handling Inconsistent Data**:
    * In the `Payment Method` column, inconsistent entries like `ERROR` and `UNKNOWN` are standardized to `Digital Wallet`. All remaining missing values are filled with the column's mode (the most frequent payment method).
    * Similarly, in the `Location` column, `ERROR` and `UNKNOWN` entries are standardized to `In-store`, with missing values also filled with the column's mode.
5.  **Removing Duplicates**: The script removes any fully duplicated rows to ensure data integrity.

***

## Data Visualization

After the data is cleaned, the script generates a series of plots to visualize key metrics:

* A **bar chart** showing the frequency distribution of different payment methods.
* A **pie chart** illustrating the proportion of orders by location type (e.g., in-store vs. takeaway).
* A **histogram** displaying the distribution of `Total Spent` amounts, which provides insights into customer spending habits.

***

## How to Run the Script

To run this project, ensure you have Python installed, along with the required libraries.

1.  **Install Dependencies**:
    ```bash
    pip install pandas kagglehub matplotlib
    ```
2.  **Run the Script**:
    Navigate to the directory containing the script and run it from your terminal.
    ```bash
    python your_script_name.py
    ```

This will execute the data cleaning process and display the resulting visualizations.