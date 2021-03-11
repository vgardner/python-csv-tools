import pandas as pd
import sys

filename = sys.argv[1]
xl_file = pd.ExcelFile(filename)
number_of_lines = sys.argv[2]

suffix = 1
for i in range(len(xl_file)):
    if i % number_of_lines == 0:
        xl_file[i:i+number_of_lines].to_csv(f"{filename}_{suffix}.csv", sep ='|', index=False, index_label=False)
        suffix += 1