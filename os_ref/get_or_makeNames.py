import os

os.chdir('/Users/seansyue/')
print(os.environ)
print(os.environ.get('HOME'))
print(os.environ.get('LOGNAME'))
print(os.environ.get('PATH'))


filepath = os.path.join('Users/seansyue', 'test.txt')
print(filepath)

print(os.path.dirname(filepath))
print(os.path.basename(filepath))
print(os.path.split(filepath))

print(os.path.splitext(filepath))
print(os.path.splitdrive('c:/'+filepath))
