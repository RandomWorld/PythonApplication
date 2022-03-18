
from bs4 import BeautifulSoup

import numpy as np
import requests

# providing url
url = "https://en.jobs.lu/Jobs.aspx?Keywords=Risk"
  
# creating requests object
html = requests.get(url).content
  
# creating soup object
data = BeautifulSoup(html, 'html.parser')
  
# finding parent <ul> tag
parent = data.find("body")
output_file = open(r'C:\Users\randomizer\IDrive-Sync\Proyectos v2\Python\WebScrap\PythonApplication\filepath.txt','w')
output_file.write(str(data.getText))
output_file.close()
# finding all <li> tags
text = list(parent.descendants)
  
# printing the content in <li> tag
print(text)
for i in range(2, len(text), 2):
    print(text[i], end=" ")