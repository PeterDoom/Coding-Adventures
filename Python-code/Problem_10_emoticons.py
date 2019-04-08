import re

happy_pattern = r"(;|:)[)D*}\]]|[(*c\[](;|:)"
sad_pattern = r"(:|;)[(\[{c]|[D{\])](;|:)"
data = input()

happy_matches = re.finditer(happy_pattern,data)
sad_matches = re.finditer(sad_pattern,data)

happy_count = len(list(happy_matches))
sad_count = len(list(sad_matches))
status = None

happiness_index = happy_count/sad_count

if happiness_index >=2:
    status = ":D"
elif happiness_index > 1:
    status = ":)"
elif happiness_index == 1:
    status = ":|"
else:
    status = ":("

print(f"Happiness index: {happiness_index:.2f} {status}")
print(f"[Happy count: {happy_count}, Sad count: {sad_count}]")



