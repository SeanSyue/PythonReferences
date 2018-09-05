import os
from datetime import datetime


print(os.listdir())


stat = os.stat('test.txt')
print(stat)

size = stat.st_size
print(size)

mode_time = stat.st_mtime
print(mode_time)
print(datetime.fromtimestamp(mode_time))\


for dirpath, dirnames, filenames in os.walk('/Users/seansyue/PycharmProjects'):
    print("Current path: ", dirpath)
    print("Directories: ", dirnames)
    print(f"Files: {filenames}\n", filenames)


