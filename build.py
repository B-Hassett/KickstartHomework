
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

# OPENING BASE PAGE AND PASSING RESULTS TO THE 2 FUNCTIONS BELOW
def main():
    template = open('templates/base.html').read()
    return template

#UPDATING FOOTER MESSAGE
def footer():
  template = main()
  footer = 'Look I updated the footer'
  new_addition = template.replace('{{footer}}', footer)
  open('templates/base.html', 'w+').write(new_addition)

#BUILDING LANDING PAGES
def build():
    template = main()
    for page in pages:
        filename = page['filename']
        title = page['title']
        output = page['output']
        content = open(filename).read()
        finished_page = template.replace('{{content}}', content).replace('{{title}}', title)
        open(output, 'w+').write(finished_page)
    
    
if __name__ == '__main__':
    footer() 
    build()
    
