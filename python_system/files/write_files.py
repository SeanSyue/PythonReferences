# https://www.youtube.com/watch?v=Uh2ebFW8OYM

# Use seek() method to set the beginning point of file writing.
with open ('file_to_write.txt', 'w') as f:
    f.write("Test")
    f.seek(0)
    f.write("R")

# Copy a file:
with open('text_file.txt', 'r')as rf, open('text_file_copy.txt', 'w') as wf:
    for line in rf:
        wf.write(line)

# Copy file by chunks:
with open('text_file.txt', 'r')as rf, open('text_file_copy.txt', 'w') as wf:
    chunk_size = 2
    rf_chunk = rf.read(chunk_size)
    while len(rf_chunk)>0:
        wf.write(rf_chunk)
        rf_chunk = rf.read(chunk_size)
