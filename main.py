#-*- coding: utf-8 -*-
import os
import markdown2

import traverser

default_html_dir = "./posts_html"  # change name in gitignore
default_assets_dir = "./assets"

date_format = '%A, %B %d, %Y'

markdowner = markdown2.Markdown()


def no_html(target):
    if not os.path.exists(target):
        return True
    # check if .md file changed in the meantime?
    return False


def md_to_html(md):
    print "generating html of", md
    with open(md, 'r') as md_file:
        md_content = md_file.read()
        html = markdowner.convert(md_content)
        md_content = md_content.split('\n')
        title = filter(lambda line: line[:2] == '# ', md_content)
        if title:
            title = title[0].replace('# ', '')
        else:
            title = md[:-3]
    return (title, html)


def write_html(filename, html):
    with open(filename, 'a') as t:
        t.write(html)
    print "saved as", filename


def generate():
    files = traverser.traverse('.')
    md_files = traverser.filter_md(files)
    print ".md files:", md_files
    htmls = {}
    if not os.path.exists(default_html_dir):
        os.makedirs(default_html_dir)
    for md in md_files:
        html_filename = md[:-2] + 'html'
        full_filename = default_html_dir + "/" + html_filename
        if no_html(full_filename):
            htmls[html_filename] = md_to_html(md)
            write_html(full_filename, htmls[html_filename][1])
        else:
            print "file already exists"
        print "changed %x files; new blog posts:" % (len(htmls))
        for post in htmls.values():
            print "\t", post[0]


def clean_all():
    print "cleaning directory", default_html_dir
    files = os.listdir(default_html_dir)
    files = [default_html_dir + "/" + f for f in files]
    n = len(files)
    if n:
        for f in files:
            os.remove(f)
        print "removed %x files" % (n)
    else:
        print "the directory is clean"


if __name__ == "__main__":
    clean_all()
    generate()
