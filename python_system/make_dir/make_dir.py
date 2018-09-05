# https://stackoverflow.com/questions/273192/how-can-i-create-a-directory-if-it-does-not-exist
import os
import errno

# Not recommend this one:
# if not os.path.exists(directory):
#     os.makedirs(directory)

try:
    os.makedirs("D:/tim")
except OSError as e:
    if e.errno != errno.EEXIST:
        raise


# https://www.programcreek.com/python/example/444/errno.EEXIST
def make_dir(path):
    """
    Creates 'path' if it does not exist

    If creation fails, an exception will be thrown

    errno.EEXIST: file exists

    :param logger:  the logger
    :param path:    the path to ensure it exists
    """
    try:
        os.makedirs(path)
    except OSError as ex:
        if ex.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            print('An error happened trying to create ' + path)
            raise
