import re


data = input()
pattern = r"([2-9JQKA]|10)[SHDC]"

matches = re.finditer(pattern,data)

for match in matches:
    print(match.group(),end =" ")