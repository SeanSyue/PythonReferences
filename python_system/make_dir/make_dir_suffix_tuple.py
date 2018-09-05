import os
import errno


class MakeDirectory:

    def __init__(self, prefix, suffix):
        self.prefix = prefix
        self.suffix = suffix
        self.folder_out = None

    def get_dir_name(self, print_dir):

        if type(self.suffix) == tuple and len(self.suffix) > 1:
            for i in range(0, len(self.suffix)):
                self.prefix += "_" + str(self.suffix[i])
                print("if")
        else:
            self.prefix = "_" + str(self.suffix)
            print("else", self.prefix)
        folder_out = self.prefix + "/"

        if print_dir is True:
            print("============folder out:============\n{}"
                  "\n===================================".format(folder_out))
        self.folder_out = folder_out
        return folder_out

    def make_dir(self):
        try:
            os.makedirs(self.folder_out)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise


PARENT_PATH = 'D:/OH YEAH/'
LAYERS = 54
dir_manager = MakeDirectory(prefix=PARENT_PATH+'hw3_q2_taxi', suffix=LAYERS)
FOLDER_OUT = dir_manager.get_dir_name(print_dir=True)
dir_manager.make_dir()
