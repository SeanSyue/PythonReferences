import os

os.chdir('/Users/seansyue/')
print(os.environ)
print(os.environ.get('HOME'))
print(os.environ.get('LOGNAME'))
print(os.environ.get('PATH'))
