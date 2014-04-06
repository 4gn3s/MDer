import os
import os.path
import shutil
import time

def file_exists(target):
    if os.path.exists(target):
        return True
    return False


def write_to_file(filename, content):
    with open(filename, 'ab') as f:
        f.write(content.encode("UTF-8"))
        print("Saved as", filename)


def find_all_files(path):
    files = []
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            print(dirpath)
            date = time.ctime(os.path.getctime(dirpath + "/" + f,))
            files.append((dirpath + "/" + f, f, date))
    return files


def filter_extension(files, extension):
    ext_files = filter(lambda name: name[1][-3:] == extension, files)
    return ext_files


def clean_all(directory):
    print("Cleaning directory %s ..." % (directory))
    shutil.rmtree(directory)
    # files = os.listdir(directory)
    # files = [directory + "/" + f for f in files]
    # n = len(files)
    # if n:
    #     for f in files:
    #         os.remove(f)
    #     print "Removed %x files" % (n)
    # else:
    #     print "The directory is either clean or non-existent"


def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print("Successfully created %s directory" % (directory))
