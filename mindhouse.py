import random
import csv
import time


def display_intro():
    title = "Hello Welcome to Math Practice Program"
    print("*" * len(title))
    print(title)
    print("*" * len(title))


def display_separator():
    print("-" * 24)


def get_user_name():
    user_input = input("What's your name?. - ")
    
    return user_input


def get_user_input():
    user_input = input("What to play more?. Y/N - ")
    
    return user_input


def get_user_solution(problem):
    print("What is the answer of " + problem)
    print("Enter Answer", end="")
    start = time.time()
    inp_user = input(" - ")
    try:
        result = int(inp_user)
    except ValueError:
        end = time.time()
        t=round((end-start),2)
        t_f = str(t) + " seconds"
        print("Please enter a valid integer!")
        return inp_user, t_f
    end = time.time()
    t = round((end-start),2)
    t_f = str(t) + " seconds"
    return result, t_f


def check_solution(user_solution, solution, count):
    if user_solution == solution:
        count = count + 1
        print("Correct Answer")
        return count
    else:
        print("Oops That's wrong.")
        return count


def menu_option(count):
    number_one = random.randrange(1, 21)
    number_two = random.randrange(1, 21)
    
    problem = str(number_one) + " * " + str(number_two)
    solution = number_one * number_two
    
    user_solution = get_user_solution(problem)
    answer = "No"
    if user_solution[0] == solution:
        answer = "Yes"
    time_taken = user_solution[1]
    count = check_solution(user_solution[0], solution, count)
    return [count, problem, user_solution[0], answer, time_taken]


def display_result(name, total, correct, files_list):
    if total > 0:
        result = correct / total
        percentage = round((result * 100), 2)
    if total == 0:
        percentage = 0
    with open(name + '.csv', 'w', newline='') as file:
        writer=csv.writer(file)
        writer.writerow(["Question","Answer","Correct","Time taken to answer"])
        for item in files_list:
            writer.writerow(item)

    print("You answered", total, "questions with", correct, "correct.")
    print("Your score is ", percentage, "%. Thank you.", sep = "")


def main():
    display_intro()
    name = get_user_name()
    display_separator()
	
    files_list = []
    total = 0
    correct = 0
    total = total + 1
    new = menu_option(correct)
    files_list.append(new[1:])
    correct = int(new[0])
    option = get_user_input()
    while option.lower() != "n":
        total = total + 1
        new1 = menu_option(correct)
        files_list.append(new1[1:])
        correct = int(new1[0])
        option = get_user_input()

    print("Good Bye " + name)
    display_separator()
    display_result(name, total, correct, files_list)

main()

