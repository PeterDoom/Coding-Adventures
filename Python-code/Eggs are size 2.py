input_for_keyword = input()
input_for_value = input()
number = int(input())
the_dict = {}

for row in range(0,number):
    current_pair = input()
    current_key = current_pair.split(' => ')[0]
    current_list = current_pair.split(' => ')[1:]

    def letter_check(letter):
        if letter in current_key:
            return True
        return False

    def list_check(string):
        if string in current_list:
            return True
        return False


    if letter_check(input_for_keyword) == True:
        if list_check(input_for_value) == True:
            the_dict[current_key] = current_list


print(the_dict)