def hello_name(user_name):
    print("Hello " + user_name)

user_name = input("What is your username? ")
hello_name(user_name)


def first_odds():
    for num in range(1, 99 + 1):
        if num % 2 !=0:
            print(num, end=" ")

first_odds()

def max_num_in_list(a_list):
    a_list.sort()
    print(a_list[-1])
    
max_num_in_list([12, 62, 44, 116, 88, 27])

def is_leap_year(a_year):
    if ((a_year%400 ==0) or ((a_year%4 ==0) and (a_year%100 !=0))):
        print(a_year," was/is a leap year.")
    else: 
        print(a_year," was/is not a leap year.")

year = input("What year would you like to check? ")
is_leap_year(int(year))


def is_consecutive(a_list):
    ele = set()
    min_n = max_n = a_list[0]
    for i in a_list:
        if i in ele:
            return False
        min_n = min(i, min_n)
        max_n = max(i, max_n)
        ele.add(i)
    if max_n-min_n+1 == len(a_list):
        return True
    return False

print(is_consecutive([1, 2, 3, 4]))
# https://stackoverflow.com/questions/72215886/how-to-check-if-a-list-is-a-consecutive-number-in-python
# Help taken from this stackoverflow page, I was unsure how to do this without imports


