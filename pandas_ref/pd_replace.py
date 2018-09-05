import pandas as pd

reader = pd.read_csv('C:/bank/data_set/benchmark/for_benchmark.csv')

indicator = reader.replace(to_replace=999, value=0, inplace=False)
print(indicator['pdays'])

reader.replace(to_replace=999, value=0, inplace=True)
print(reader['pdays'])
