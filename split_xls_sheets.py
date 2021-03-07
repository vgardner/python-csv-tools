import pandas as pd
import sys

filename = sys.argv[1]
xl_file = pd.ExcelFile(filename)

for sheet in xl_file.sheet_names:
    df = pd.read_excel(xl_file,sheet_name=sheet)
    df.to_csv(f"{filename}-{sheet}.csv",index=False)