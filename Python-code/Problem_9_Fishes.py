import re
class Fish:
    def __init__(self,lenght_of_tail,lenght_of_body,status_quo):
        self.tail = len(lenght_of_tail)
        self.body = len(lenght_of_body)
        self.status = status_quo


list_of_fishes = []
data = input()


pattern = r"(?P<tail>>*)<(?P<body>\(+)(?P<eye>(x|'|-))>"

fish_matches = list(re.finditer(pattern,data))
counter =1

if not any(fish_matches):
    print("No fish found.")

for match in fish_matches:
    fishie = Fish(match.groupdict()['tail'],match.groupdict()['body'],match.groupdict()['eye'])
    list_of_fishes.append(fishie)


for fish in list_of_fishes:
    print(f"Fish {counter}: {str(fish_matches[counter-1].group())}")
    if fish.tail >5:
        print(f"  Tail type: Long ({fish.tail*2} cm)")
    elif fish.tail > 1:
        print(f"  Tail type: Medium ({fish.tail*2} cm)")
    elif fish.tail ==1:
        print(f"  Tail type: Short ({fish.tail*2} cm)")
    else:
        print(f'  Tail type: None')
    if fish.body > 10:
        print(f"  Body type: Long ({fish.body*2} cm)")
    elif fish.body > 5:
        print(f"  Body type: Medium ({fish.body*2} cm)")
    else:
        print(f"  Body type: Short ({fish.body*2} cm)")
    if fish.status == "'":
        print(f"  Status: Awake")
    elif fish.status == "x":
        print(f"  Status: Dead")
    else:
        print(f"  Status: Asleep")
    counter +=1
