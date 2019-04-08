import re

pattern = r"<a\shref=(.*?)>(.*?)<\/a>"

string = ''

while True:
    data = input()
    if data == 'end':
        break
    if '<a' in data:
        string = re.sub(pattern,'URL href=] [/URL]', data)

print(string)