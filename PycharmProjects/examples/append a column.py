import csv
import pandas as pd
import numpy as np

# format the input file to remove all the rows at the beginning of the file
with open('Elastase_InputFile.csv', 'rt') as inp:
    with open('Elastase_OutputFile.csv', 'wt') as out:
        writer = csv.writer(out)
        for row in csv.reader(inp):
            if len(row) > 3:
                writer.writerow(row)

# append alternated 1 and 0 and get the "Volume" row
df = pd.read_csv('Elastase_OutputFile.csv')

Elastase = []
for row in df.index:
    Elastase.append(1)
m = np.asarray(Elastase)
df['Elastase'] = m
# df.to_numpy()
# print(df)
print(df)