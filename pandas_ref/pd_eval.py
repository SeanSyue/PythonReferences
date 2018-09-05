import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 2), columns=list('ab'))

df.eval('a + b')
df.eval('c = a + b')

print(df)
print(df.eval('a + b'))
print(df.eval('c = a + b'))

