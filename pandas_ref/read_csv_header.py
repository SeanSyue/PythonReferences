import pandas as pd

file1 = 'C:/Users/Sean/PycharmProjects/tensorflow/MachineLearning/hw3_q2_taxi/Descriptive_Hour.csv'
df_hour = pd.read_csv(file1, header=0)
print(df_hour)

df_hour1 = pd.read_csv(file1, header=None)
print(df_hour1)
