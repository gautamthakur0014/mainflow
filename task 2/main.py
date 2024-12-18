import pandas as pd

def load_data(file_path):
    
    data = pd.read_csv(file_path)
    print("Data loaded successfully!")
    return data
    

# Handle missing values
def handle_missing_values(df, strategy="drop", fill_value=None):
    if strategy == "drop":
        df = df.dropna()
        print("Missing values dropped.")
    elif strategy == "fill":
        if fill_value is not None:
            df = df.fillna(fill_value)
            print(f"Missing values filled with: {fill_value}")
        else:
            print("Fill value not provided. No changes made.")
    else:
        print("Invalid strategy. Choose 'drop' or 'fill'.")
    return df

# Remove duplicates
def remove_duplicates(df):
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)
    print(f"Removed {before - after} duplicate rows.")
    return df

# Filter data
def filter_data(df, column, condition):
    try:
        filtered_df = df.query(condition)
        print(f"Data filtered on column '{column}' with condition '{condition}'.")
        return filtered_df
    except Exception as e:
        print(f"Error in filtering: {e}")
        return df

# Sort data
def sort_data(df, column, ascending=True):
    try:
        df = df.sort_values(by=column, ascending=ascending)
        print(f"Data sorted by column '{column}', ascending={ascending}.")
        return df
    except Exception as e:
        print(f"Error in sorting: {e}")
        return df


if __name__ == "__main__":
    
    file_path = "data.csv"
    df = load_data(file_path)

    if df is not None:
        print("Initial data preview:")
        print(df.head())

        df = handle_missing_values(df, strategy="fill", fill_value=0)
        df = remove_duplicates(df)
        df = filter_data(df, column="ChipRate", condition="ChipRate > 10")
        df = sort_data(df, column="ChipRate", ascending=False)

        print("Final data preview:")
        print(df.head())
