import pandas as pd
import sys

csv_input = pd.read_csv(sys.argv[1])

print("Loaded csv file.")
csv_input[sys.argv[2]] = sys.argv[3]
csv_input.to_csv(sys.argv[1] + '_output.csv', index=False)