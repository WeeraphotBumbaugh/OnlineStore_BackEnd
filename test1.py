# #dictionary
# user = {
#     "name": "Will",
#     "last_name": "Bumbaugh",
#     "age": 26
# }
# print(user)
# print(type(user))
# print(user["name"] + " " + user["last_name"])
# #list
# numbers = [1,2,3,4,5]
# #add
# numbers.append(6)
# print(numbers)
# #length
# print(len(numbers)) # of items
# print(len(user["name"])) # of characters
# print(len(user)) # of objects

ages = [32, 74, 20, 69, 52, 26, 31, 77, 43, 73, 51, 57, 19, 79, 40, 34, 27, 23, 21, 44, 53, 55, 24, 36, 41, 47, 78, 46, 68, 75, 49, 83, 61, 60, 29, 56, 67, 17, 70, 81, 87, 38]

# def exc1():
#     #print all the numbers
#     total = 0
#     for age in ages:
#         total = total + age
#         #print(age)
#     print(total)
# exc1()

# def exc2():
#     #print all the numbers greater or equal to 21
#     #count and print how many users are equal or older to 21
#     count = 0
#     for age in ages:
#         if age >= 21:
#             print(age)
#             count += 1
#     print("this is the count:", str(count))
# exc2()

def exc3():
    #count how many users are between 30 & 40 years old
    count = 0
    for age in ages:
        if age > 30 and age < 40:
            count += 1
    print("# of users between 30 & 40:", str(count))
exc3()