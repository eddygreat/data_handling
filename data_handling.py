import pandas as pd
import numpy as np
import json
import io

# ==========================================
# 1. DATA LOADING UTILITY
# ==========================================

def load_data(file_path, file_type='csv'):
    """
    Loads data from various formats into a Pandas DataFrame.
    Supports: 'csv', 'json', 'txt'
    """
    try:
        if file_type == 'csv':
            df = pd.read_csv(file_path)
        elif file_type == 'json':
            df = pd.read_json(file_path)
        elif file_type == 'txt':
            # Assuming tab-separated for text files, can be adjusted to ',' or ';'
            df = pd.read_csv(file_path, sep='\t')
        else:
            raise ValueError("Unsupported file type. Use 'csv', 'json', or 'txt'.")
        
        print(f"Successfully loaded {file_type.upper()} data.")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# ==========================================
# 2. DATA CLEANING & NORMALIZATION
# ==========================================

def clean_and_normalize(df):
    """
    Performs standard cleaning operations:
    - Normalizes column names (lower case, snake_case)
    - Handles missing values (simple fill/drop strategy)
    """
    # Normalize Column Names
    # e.g., "First Name" -> "first_name"
    df.columns = (df.columns
                  .str.strip()
                  .str.lower()
                  .str.replace(' ', '_')
                  .str.replace(r'[^\w\s]', '', regex=True))
    
    print("Column names normalized to snake_case.")

    # Handle Missing Values
    # Strategy: Fill numeric with median, categorical with 'unknown'
    for col in df.columns:
        if df[col].dtype in [np.float64, np.int64]:
            df[col] = df[col].fillna(df[col].median())
        else:
            df[col] = df[col].fillna('unknown')
            
    print("Missing values handled (Median for numeric, 'unknown' for object).")
    return df

# ==========================================
# 3. EXPLORATORY DATA ANALYSIS (EDA)
# ==========================================

def perform_simple_eda(df):
    """
    Performs standard Pandas EDA operations
    """
    print("\n--- DATA HEAD ---")
    print(df.head())
    
    print("\n--- DATA DESCRIPTION ---")
    print(df.describe(include='all'))
    
    print("\n--- MISSING VALUES COUNT ---")
    print(df.isnull().sum())
    
    # Value counts for the first object-type column found
    object_cols = df.select_dtypes(include=['object']).columns
    if len(object_cols) > 0:
        print(f"\n--- VALUE COUNTS FOR: {object_cols[0]} ---")
        print(df[object_cols[0]].value_counts().head(10))

# ==========================================
# 4. EXECUTION PIPELINE
# ==========================================

# CREATING DUMMY DATA FOR DEMONSTRATION
# (In a real scenario, you would provide a path to a real file)
raw_data = {
    'First Name': ['Alice', 'Bob', 'Charlie', np.nan],
    'Age ': [25, np.nan, 30, 22],
    'Purchase-Amount': [100.5, 200.0, np.nan, 150.75],
    'City': ['New York', 'London', 'London', 'Paris']
}
demo_df = pd.DataFrame(raw_data)

print("Starting Ingestion Pipeline...")

# Step 1: Normalize and Clean
cleaned_df = clean_and_normalize(demo_df)

# Step 2: Perform EDA
perform_simple_eda(cleaned_df)

# Step 3: Export Cleaned Data
output_file = 'cleaned_data_export.csv'
cleaned_df.to_csv(output_file, index=False)
print(f"\nPipeline Complete. Cleaned data exported to: {output_file}")
