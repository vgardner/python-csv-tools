import pandas as pd
import sys

filename = sys.argv[1]
xl_file = pd.ExcelFile(filename)
xl = pd.read_excel(xl_file)
xl.to_csv(f"{filename}-{sheet}.csv",index=False)