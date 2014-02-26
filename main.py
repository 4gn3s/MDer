import os
import markdown2
import traverser

default_html_dir = "./html"
markdowner = markdown2.Markdown()


def no_html(md):
    target = md[:-2] + 'html'
    if not os.path.exists(target):
        return True
    # check if .md file changed in the meantime?
    return False


def md_to_html(md):
    print "generating html of", md
    with open(md, 'r') as md_file:
        md_content = md_file.read()
        html = markdowner.convert(md_content)
    return html


def generate():
    files = traverser.traverse('.')
    md_files = traverser.filter_md(files)
    print ".md files:", md_files
    htmls = {}
    for md in md_files:
        if no_html(md):
            htmls[md[:-3]] = md_to_html(md)
    print htmls


if __name__ == "__main__":
    generate()
