users = [
    {
        'id': 1,
        'name': 'Alice',
        'gender': 'female',
        'age': 25,
        'preferred_color': 'blue'
    },
    {
        'id': 2,
        'name': 'Bob',
        'gender': 'male',
        'age': 35,
        'preferred_color': 'GREEN'
    },
    {
        'id': 3,
        'name': 'Charlie',
        'gender': 'male',
        'age': 45,
        'preferred_color': 'Red'
    },
    {
        'id': 4,
        'name': 'Danielle',
        'gender': 'female',
        'age': 30,
        'preferred_color': 'YelloW'
    },
    {
        'id': 5,
        'name': 'Evelyn',
        'gender': 'female',
        'age': 20,
        'preferred_color': 'PuRplE'
    },
    {
        'id': 6,
        'name': 'Frank',
        'gender': 'male',
        'age': 28,
        'preferred_color': 'purple'
    },
    {
        'id': 7,
        'name': 'Grace',
        'gender': 'female',
        'age': 31,
        'preferred_color': 'GREEN'
    },
    {
        'id': 8,
        'name': 'Henry',
        'gender': 'male',
        'age': 40,
        'preferred_color': 'BLUE'
    },
    {
        'id': 9,
        'name': 'Isabelle',
        'gender': 'female',
        'age': 27,
        'preferred_color': 'red'
    },
    {
        'id': 10,
        'name': 'Jack',
        'gender': 'male',
        'age': 24,
        'preferred_color': 'yellow'
    }
]

# def exec1():
#     #print all the names
#     for user in users:
#         print(user["name"])
# exec1()

# def exc2():
#     male_count = 0
#     female_count = 0
#     for user in users:
#         gender = user["gender"]
#         if gender == "male":
#             male_count += 1
#         elif gender == "female":
#             female_count += 1
#     print("# of males:", male_count)
#     print("There are " + str(female_count) + " females")
#     print(f"There are {female_count} females and {male_count} males")
# exc2()

def find_by_id(id):
    for user in users:
        if user["id"] == id:
            print(user)
find_by_id(3)