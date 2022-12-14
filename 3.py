# Преобразовать набора списков 
# users = ['user1','user2','user3','user4','user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111,222,333]
# в другой набор 

# ['user1', 4, 111]
# ['user2', 5, 222]
# ['user3', 9, 333]

users = ['user1','user2','user3','user4','user5']
ids = [4, 5, 9, 14, 7]
salary = [111,222,333]

a = zip(users, ids, salary)
for i in a:
    print(list(i))