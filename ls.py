first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
first_result = [len(i[0]) - len(i[1]) for i in zip(first,second) if len(i[0]) != len(i[1])]
second_result = [True if len(first[x]) == len(second[x]) else False for x in range(len(first))]
print(first_result)
print(second_result)