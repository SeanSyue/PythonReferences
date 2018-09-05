import numpy as np
# -1 simply means that it is an unknown dimension and we want numpy to figure it out.

z = np.arange(12)
rs = z.reshape(-1, 4)
print(rs)
