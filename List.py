#Lists
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends[1] = "Mishan"
print(friends[1:3])
#List Functions
lucky_numbers = [4, 78, 25, 16, 63, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.extend(lucky_numbers)
friends.insert(1, "Kelly")
friends.pop()
#friends.clear()
print(friends.index("Kevin"))
lucky_numbers.sort()
print(lucky_numbers)

friends2 = friends.copy()
print(friends2)
#Tuples
coordinates = [(4, 5), (6, 9),(80 ,34)]
print(coordinates[1])





