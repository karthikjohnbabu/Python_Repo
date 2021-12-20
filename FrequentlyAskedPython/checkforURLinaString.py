import re

str= " Im blogger at https://learnwithkarthik.com/"

url = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+',str)
print(url)

