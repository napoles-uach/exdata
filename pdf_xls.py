import camelot
import pandas as pd

tables = camelot.read_pdf('file.pdf')

# Merge the dataframes into a single dataframe
merged_dataframe = pd.concat([table.df for table in tables], axis=1)

# Select the desired columns from the merged dataframe
selected_columns = [0, 3, 5, 1]
merged_dataframe = merged_dataframe.iloc[:, selected_columns]

# Save the merged dataframe to a CSV file
merged_dataframe.to_csv('output.csv', index=False)
