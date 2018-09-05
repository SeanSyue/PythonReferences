conf_writer = open('Output.txt', mode='a', encoding='utf-8')
conf_writer.write("something to write")
conf_writer.flush()
conf_writer.close()

# -- Alternative expression: --
with open('Output.txt', mode='a', encoding='utf-8') as conf_writer:
    print("something to write", file=conf_writer, flush=True)

