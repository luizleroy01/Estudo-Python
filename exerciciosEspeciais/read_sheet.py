import pandas as pd

# Load the spreadsheet into a pandas DataFrame
df = pd.read_excel('your_spreadsheet.xlsx')  # Replace 'your_spreadsheet.xlsx' with the path to your spreadsheet file

# Access columns by name
column1 = df['Column1']  # Replace 'Column1' with the name of the column you want to read
column2 = df['Column2']  # Replace 'Column2' with the name of the column you want to read

# Access columns by index
# column1 = df.iloc[:, 0]  # Replace 0 with the index of the column you want to read (0-indexed)
# column2 = df.iloc[:, 1]  # Replace 1 with the index of the column you want to read (0-indexed)

# Print the columns
print("Column 1:")
print(column1)
print("\nColumn 2:")
print(column2)
