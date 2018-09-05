# https://stackoverflow.com/questions/17071871/select-rows-from-a-dataframe-based-on-values-in-a-column-in-pandas
import pandas as pd


df = pd.DataFrame({'foo': [100, 111, 222],
                   'bar': [333, 444, 555]})

df[df.foo == 222]

df[(df.foo == 222) | (df.bar == 444)]

# Recommanded usage:
df.query('foo == 222 | bar == 444')
