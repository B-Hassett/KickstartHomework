
#ABOUT PAGE - CONFIRMED WORKS
print ("hello world")
Top_html = open ('templates/top.html').read()
abMiddle_html = open ('content/about.html').read()
Bottom_html = open ('templates/bottom.html').read()

about_html = Top_html + abMiddle_html + Bottom_html
open('about.html', 'w+').write(about_html)


#EXPERIENCE PAGE
Top_html = open ('templates/top.html').read()
exMiddle_html = open ('content/experience.html').read()
Bottom_html = open ('templates/bottom.html').read()

experience_html = Top_html + exMiddle_html + Bottom_html
open('experience.html', 'w+').write(experience_html)



#EDUCATION PAGE
Top_html = open ('templates/top.html').read()
edMiddle_html = open ('content/education.html').read()
Bottom_html = open ('templates/bottom.html').read()

education_html = Top_html + edMiddle_html + Bottom_html
open('education.html', 'w+').write(education_html)

#CONTACT PAGE
Top_html = open ('templates/top.html').read()
coMiddle_html = open ('content/contact.html').read()
Bottom_html = open ('templates/bottom.html').read()

contact_html = Top_html + coMiddle_html + Bottom_html
open('contact.html', 'w+').write(contact_html)
