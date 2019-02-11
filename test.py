#ABOUT PAGE
print ("hello world")
abTop_html = open ('hw2_templates/hw2_top.html').read()
abMiddle_html = open ('hw2_content/hw2_about.html').read()
abBottom_html = open ('hw2_templates/hw2_bottom.html').read()
about_Page = abTop_html + abMiddle_html + abBottom_html

#EDUCATION PAGE
edTop_html = open ('hw2_templates/hw2_top.html').read()
edMiddle_html = open ('hw2_content/hw2_education.html').read()
edBottom_html = open ('hw2_templates/hw2_bottom.html').read()
education_Page = edTop_html + edMiddle_html + edBottom_html

#EXPERIENCE PAGE
exTop_html = open ('hw2_templates/hw2_top.html').read()
exMiddle_html = open ('hw2_content/hw2_experience.html').read()
exBottom_html = open ('hw2_templates/hw2_bottom.html').read()
experience_Page = exTop_html + exMiddle_html + exBottom_html

#CONTACT PAGE
coTop_html = open ('hw2_templates/hw2_top.html').read()
coMiddle_html = open ('hw2_content/hw2_contact.html').read()
coBottom_html = open ('hw2_templates/hw2_bottom.html').read()
contact_Page = coTop_html + coMiddle_html + coBottom_html


#COMBINED WEBSITE
combined_html = about_Page + education_Page + experience_Page + contact_Page
open('combined.html', 'w+').write(combined_html)

print ("hello world")
