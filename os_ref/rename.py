import os
os.rename('test.txt', 'demo.txt')

# Check whether we successfully rename the file.
print(os.listdir())
