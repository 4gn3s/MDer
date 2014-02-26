#-*- coding: utf-8 -*-
import markdown2

import file_manager as fileManager

default_html_dir = "./posts_html"  # change name in gitignore
default_assets_dir = "./assets"

date_format = '%A, %B %d, %Y'

markdowner = markdown2.Markdown()


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


def generate():
    files = fileManager.find_all_files('.')
    md_files = fileManager.filter_extension(files, '.md')
    print ".md files:", md_files

    htmls = {}
    fileManager.create_dir(default_html_dir)

    for md in md_files:
        html_filename = md[:-2] + 'html'
        full_filename = default_html_dir + "/" + html_filename
        if not fileManager.file_exists(full_filename):
            htmls[html_filename] = md_to_html(md)
            fileManager.write_to_file(full_filename, htmls[html_filename][1])
        else:
            print "file already exists"
        print "changed %x files; new blog posts:" % (len(htmls))
        for post in htmls.values():
            print "\t", post[0]


if __name__ == "__main__":
    fileManager.clean_all(default_html_dir)
    generate()