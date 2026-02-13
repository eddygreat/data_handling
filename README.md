Comprehensive Data Ingestion and Cleansing Pipeline with PandasOverview

This project delivers a robust, senior-developer level implementation of a high-efficiency Data Ingestion Pipeline. Engineered for production environments, it is designed to seamlessly automate the transition from raw, disparate, and often messy source files into a unified, clean, and immediately analysis-ready dataset, making it ideal for downstream Machine Learning models and Business Intelligence tools.Core Features
Multi-Format Ingestion: Features a modular and extensible architecture with specialized functions to reliably load data from common formats: Comma-Separated Values (CSV), JavaScript Object Notation (JSON), and Tab-Separated Text (TSV/TXT) files.
Dynamic Column Normalization (Snake_Case Standard): Automatically processes and standardizes all incoming column headers. It resolves common inconsistencies (e.g., "User ID", "user-ID", "USER_id", "UserID") by converting them into a clean, universally compatible snake_case format.
Intelligent Missing Data Imputation: Implements a context-aware strategy for handling nulls (NaN values):
Numeric Columns: Missing values are imputed using the median, a statistically robust measure that minimizes the bias introduced by potential outliers (skewed data).
Categorical Columns: Missing string/factor values are reliably filled with the explicit placeholder 'unknown', ensuring that the missingness is preserved as an informational category without skewing frequency counts.
Automated Exploratory Data Analysis (EDA): A built-in reporting module provides an immediate, high-level overview of data quality, featuring statistical summaries, data type distribution, and categorical frequency counts, accelerating the initial data understanding phase.
Prerequisites

To execute the pipeline, ensure you have a standard Python environment installed, along with the necessary data manipulation libraries:
pip install pandas numpy
Step-by-Step Usage Guide
Load Data: Initiate the process by calling the load_data(file_path, file_type) function, passing the file's location and format.
Cleanse and Normalize: Execute clean_and_normalize(dataframe) to automatically apply header standardization and the intelligent null-value imputation routines.
Analyze Data Quality: Run perform_simple_eda(dataframe) to generate a comprehensive overview of the cleaned dataset's structure and statistical properties.
Export Final Dataset: The script concludes by automatically exporting the fully cleaned and transformed DataFrame into a persistent file named cleaned_data_export.csv, ready for use in any downstream data science application.
Technical Implementation Details
Header Normalization Strategy: The process employs a specific Regular Expression, [^\\w\\s], to effectively strip special characters and non-alphanumeric symbols from the column headers. This ensures compliance with most relational database standards (SQL) and allows for reliable object attribute access in Python (dot-notation).
Handling of Null Values: The deliberate choice of median over the mean for numeric imputation is a best practice. It maintains data integrity by preventing data skew, which is a common problem when using the mean in the presence of extreme outliers.
License

This project is released under the MIT License. It is freely available for use, modification, and integration into personal engineering projects and professional data science portfolios.
