big_list = []
male_ages = []
female_ages = []


with open('C:\Users\Павел\PycharmProjects\new pr\data.csv', 'r') as file:
    next(file)
    for line in file:
        big_list.append(line.split(','))


for line in big_list:
    if line[5] == 'male' and line[6] != '':
        male_ages.append(line[6])
    if line[5] == 'female' and line[6] != '':
        female_ages.append(line[6])

male_ages = list(map(float, male_ages))
female_ages = list(map(float, female_ages))

print(f'Минимальный мужской возраст - {min(male_ages)}, максимальный - {max(male_ages)}')
print(f'Минимальный женский возраст - {min(female_ages)}, максимальный - {max(female_ages)}')