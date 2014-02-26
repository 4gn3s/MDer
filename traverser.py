import os

def traverse(path):
    files = []
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            files.append(f)
    return files

def filter_md(files):
    md_files = filter(lambda name: name[-3:] == '.md', files)
    return md_files