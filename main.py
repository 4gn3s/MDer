import traverser

if __name__ == "__main__":
    files = traverser.traverse('.')
    print "all files:", files
    md_files = traverser.filter_md(files)
    print ".md:", md_files
