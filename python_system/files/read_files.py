# https://www.youtube.com/watch?v=Uh2ebFW8OYM
with open('text_file.txt', 'r') as a:
    print(a.readable())
    print(a.readline(), end='')
    print(a.readline(), end='')

print("=============================")
with open ('text_file.txt', 'r') as b:
    print(b.readlines())

print("=============================")
with open('text_file.txt', 'r') as c:
    print(c.read())

print("=============================")
with open('text_file.txt', 'r') as d:
    for lines in d:
        print(lines, end='')

# To specify how many characters to print out.
# To get notified with the characters count read, use tell() method:
print("=============================")
with open('text_file.txt', 'r') as e:
    print(e.read(100))
    print(e.tell())
    print(e.read(100))  # It will return empty string if argument exceed the maximun number of characters in the text.

# The use of a while loop when we want to print out the whole content:
print("=============================")
with open('text_file.txt', 'r') as f:
    size_to_read = 10
    f_content = f.read(size_to_read)
    while len(f_content) >0:
        print(f_content, end='*')
        f_content = f.read(size_to_read)  # Must add this line! Or it will become a infinite loop.
    print("")

# Use seek() method to set the beginning point of file reading.
print("=============================")
with open('text_file.txt', 'r') as g:
    print(g.readline(), end='')
    g.seek(0)
    print(g.readline(), end='')
    g.seek(6)
    print(g.readline(), end='')
