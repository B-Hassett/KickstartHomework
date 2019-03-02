
import glob

def create_list():
    import glob
    all_html_files = glob.glob("content/*.html")
    pages = []
    import os
    for entry in all_html_files:
        file_path = entry
        file_name = os.path.basename(file_path)
        name_only, extension = os.path.splitext(file_name)
        pages.append({
         "filename": "content/" + name_only + extension,
         "title": name_only,
         "output": "docs/" + name_only + extension,
         })
    return pages

def main():
    template = open('templates/base.html').read()
    return template

#UPDATING FOOTER MESSAGE
def footer(template):
  footer = 'Look I updated the footer'
  return template.replace('{{footer}}', footer)

def build():
    template = main()
    for page in create_list ():
        filename = page['filename']
        title = page['title']
        output = page['output']
        content = open(filename).read()
        finished_page = template.replace('{{content}}', content).replace('{{title}}', title)
        open(output, 'w+').write(finished_page)
    


if __name__ == '__main__':
    create_list()
    build()
    
    
