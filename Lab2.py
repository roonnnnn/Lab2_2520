

def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5, 67,32)")

def get_user_input():
    arraylist = []
    print("get_user_input")
    inputstr = input()
    numlist = inputstr.split(",")
    print(numlist)
    
    for eachnum in numlist:
        arraylist.append(float(eachnum))
    print(arraylist)
    return arraylist
def calc_average(numlist):
    print("calc_average")
    total = sum
def find_min_max(numlist):
    print("find_min_max")

def sort_temperature(numlist):
    print("sort_temperature")

def calc_median_temperature(numlist):
    print("calc_median_temperature")

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    arraylist = get_user_input()

if __name__ == "__main__":
    main()