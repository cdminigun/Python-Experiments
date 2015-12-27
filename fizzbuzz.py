def fizzbuzz():
    a = "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17"
    split_string = a.split(" ")
    split_string_list = []
    for number in split_string:
        this_num = int(number)
        mod_three = this_num % 3 == 0
        mod_five = this_num % 5 == 0
    
        if mod_three and mod_five:
            split_string_list.append("Fizz Buzz")
        elif mod_three :
            split_string_list.append("Fizz")
        elif mod_five :
            split_string_list.append("Buzz")

    print split_string_list

if __name__ == "__main__":
    fizzbuzz()

