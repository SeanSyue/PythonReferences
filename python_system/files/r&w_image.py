# https://www.youtube.com/watch?v=Uh2ebFW8OYM
with open("pic.png", 'rb') as rf, open("pic_copy.png", 'wb') as wf:
    for line in rf:
        wf.write(line)
