#-*- coding: utf-8 -*-
import markdown2
import datetime
import jinja2
import distutils.core
import re

import file_manager as fileManager

default_html_dir = ".\..\output"  # change name in gitignore
default_dir = ".\content"
assets_dir = "\\assets"

templates={
        'posts': "posts.html",
        # 'archives': "archives.html",
        # 'category': "category.html",
        'index': "index.html",
        # 'page404': "404.html"
        }

date_format = '%A, %B %d, %Y'

markdowner = markdown2.Markdown()

def date_now(format="%d.m.%Y %H:%M:%S"):
    """ returns the formated datetime """
    return datetime.datetime.now().strftime(format)


def get_title(html):
    html_lowered = html.lower()
    begin = html_lowered.find('<h1>')
    end = html_lowered.find('</h1>')
    if begin == -1 or end == -1:
        return None
    else:
        # Find in the original html
        title = html[begin+len('<h1>'):end].strip()
        html = html.replace(html[begin:end+len('<h1>')+1], "")
        return (title, html)

def md_to_html(md):
    print("generating html of", md)
    with open(md, 'r') as md_file:
        md_content = md_file.read()
        html = markdowner.convert(md_content)
        title, html = get_title(html)
        if not title:
            title = md[:-3]
    return (title, html)


if __name__ == "__main__":
    fileManager.clean_all(default_html_dir)
    if not fileManager.file_exists(assets_dir):
        distutils.dir_util.copy_tree(default_dir + assets_dir, default_html_dir + assets_dir)
        # later check folder size & update
    env= jinja2.Environment(loader=jinja2.FileSystemLoader(default_dir))
    template = env.get_template(templates['posts'])
    htmls = []
    files = fileManager.find_all_files(default_dir)
    md_files = fileManager.filter_extension(files, '.md')
    print(".md files:", md_files)
    for (fullpathmd, md, date) in reversed(list(md_files)):
            html_filename = md[:-2] + 'html'
            full_filename = default_html_dir + "/" + html_filename
            if not fileManager.file_exists(full_filename):
                html = md_to_html(fullpathmd)
                htmls.append({ "content": html[1], "date": date, "author": "4gn3s", "title": html[0] })
                #fileManager.write_to_file(full_filename, htmls[html_filename][1])
            print("changed %x files; new blog posts:" % (len(htmls)))


    html = template.render(meta_description="World", meta_author="4gn3s", page_title="TITLE", posts=htmls)
    fileManager.write_to_file(default_html_dir + "\\" + templates['index'], html)
