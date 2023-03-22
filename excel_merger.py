import pandas as pd
from datetime import datetime
import sys

# Get the Excel file names from command line arguments
file1 = sys.argv[1]
file2 = sys.argv[2]

# Read the first Excel document into a pandas DataFrame
df1 = pd.read_excel(file1).drop(['Footprint'], axis=1)

# Read the second Excel document into a pandas DataFrame
df2 = pd.read_excel(file2).drop(['Name'], axis=1)

# Merge the two DataFrames on the 'Reference' column, keeping all columns from the second DataFrame except for
# 'Footprint' and 'Name'
merged_df = pd.merge(df1, df2, on='Reference', how='right')

print(merged_df)

# Get the current date and time
now = datetime.now()

# Format the current date and time as a string
date_time_str = now.strftime("%Y-%m-%d-%H-%M-%S")

# Add the current date and time to the filename of the merged Excel document
diff_result = f"merged_doc_{date_time_str}.xlsx"

# Save the merged DataFrame to the new Excel document
merged_df.to_excel(diff_result, index=False)
