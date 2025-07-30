import pandas as pd
import os


def generate_excel(df, filename):
    """
    Export a pandas DataFrame to an Excel file.
    
    This function takes a pandas DataFrame and exports it to an Excel file
    in the current directory. If the filename doesn't end with '.xlsx',
    it will be automatically appended.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        The DataFrame to export to Excel
    filename : str
        The desired filename for the Excel file (with or without .xlsx extension)
        
    Returns:
    --------
    str
        Success message with the full file path of the created Excel file
        
    Raises:
    -------
    ValueError
        If df is not a pandas DataFrame
    IOError
        If there's an error writing the file
    """
    # Validate input
    if not isinstance(df, pd.DataFrame):
        raise ValueError("The first parameter must be a pandas DataFrame")
    
    if not isinstance(filename, str) or not filename.strip():
        raise ValueError("The filename must be a non-empty string")
    
    # Add .xlsx extension if missing
    if not filename.endswith('.xlsx'):
        filename = filename + '.xlsx'
    
    try:
        # Get the full path for the file in current directory
        file_path = os.path.join(os.getcwd(), filename)
        
        # Export DataFrame to Excel
        df.to_excel(file_path, index=False, engine='openpyxl')
        
        # Return success message with file path
        return f"Excel file successfully created at: {file_path}"
        
    except PermissionError:
        raise IOError(f"Permission denied: Unable to write to '{file_path}'")
    except Exception as e:
        raise IOError(f"Error writing Excel file: {str(e)}")


# Example usage
if __name__ == "__main__":
    # Create a sample DataFrame
    sample_data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
        'Salary': [70000, 85000, 92000, 76000]
    }
    
    df_example = pd.DataFrame(sample_data)
    
    # Export to Excel without .xlsx extension
    result1 = generate_excel(df_example, "employee_data")
    print(result1)
    
    # Export to Excel with .xlsx extension
    result2 = generate_excel(df_example, "employee_report.xlsx")
    print(result2)