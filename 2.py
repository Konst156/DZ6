# Дан список, вывести отдельно буквы и цифры.

# a = ( "a", 'b', '2', '3' ,'c')
# b = ( 'a' , 'b' , 'c')
# c = ( '1', '2', '3')

a = [i for i in input('Введите список из букв и цифр: ').split()]

b = [a[i] for i in range(len(a)) if a[i].isalpha()]
c = [a[i] for i in range(len(a)) if a[i].isdigit()]

print(b)
print(c)