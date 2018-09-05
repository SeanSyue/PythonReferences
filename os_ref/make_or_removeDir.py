import os

os.mkdir('dir2')
os.makedirs('dir1/dir1.1')  # Can make


os.chdir('dir1')
print(os.listdir())

# These two methods can only remove empty dir.
os.rmdir('dir1')  # Can only remove top level dir.
os.removedirs('dir2/dir2.1')  # Can work on tree structure.
