pages = [

	{
	
		"filename" : "content/about.html" ,
		"output" : "docs/index.html" ,
		"title" : "about me" ,	
	} ,
	{
		"filename" : "content/experience.html" ,
		"output" : "docs/experience.html" ,
		"title" : "experience" ,	
	} ,
	{
		"filename" : "content/education.html" ,
		"output" : "docs/education.html" ,
		"title" : "education" ,	
	} ,
	{
		"filename" : "content/contact.html" ,
		"output" : "docs/contact.html" ,
		"title" : "contact" ,	
	} ,
]


def footer():
  template = open('templates/base.html').read()
  footer = '<p>Look I updated the footer</p>'
  new_addition = template.replace('{{footer}}', footer)
  open('templates/base.html', 'w+').write(new_addition)

def create_page():
    template = open('templates/base.html').read()
    def build():
        for page in pages:
            filename = page['filename']
            title = page['title']
            output = page['output']
            content = open(filename).read()
            finished_page = template.replace('{{content}}', content).replace('{{title}}', title)
            open(output, 'w+').write(finished_page)
    build()
    


if __name__ == '__main__':
    footer()
    create_page()
    
