import pandas as pd

# Load the CSV file
file_path = 'student.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
print(df.head())
