import os
import os.path
def get_cur_dir_name(file_path):
    print(fie_path)
    print(os.path.abspath(os.path.join(file_path, os.pardir)))
    parent_path = os.path.abspath(os.path.join(file_path, os.pardir))
    parent_name = file_path.replace(parent_path + "\\", "")
    return parent_name

def get_parent_path_name():
    parent_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    print(parent_path)
    return parent_path

def createFolder(directory):
   try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' + directory)

def make_corpus_dir():
    make_dir_name = get_cur_dir_name(os.getcwd())
    # print(make_dir_name)
    createFolder("corpus_"+ make_dir_name)
    return "curpus_" + make_dir_name

def get_corpus_dir_name():
    make_dir_name = get_cur_dir_name(os.getcwd())
    # print(make_dir_name)
    return "curpus_" + make_dir_name