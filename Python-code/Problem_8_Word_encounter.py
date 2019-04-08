import re

pattern_for_validation = r"^[A-Z].*[!?.]$"

filter_base = input()
filter_letter = filter_base[0]
filter_number = int(filter_base[1])
list_words = []
count = 0

while True:
    data = input()
    if data == 'end':
        break
    validation = re.search(pattern_for_validation,data)
    if validation is not None:
        pattern = r"[,\s.?!]"
        words = re.split(pattern,data)
        for word in words:
            count = 0
            for symbol in word:
                if symbol == filter_letter:
                    count+=1
            if count >= filter_number:
                list_words.append(word)


print(", ".join(list_words),end= " ")