grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

#Преобразуем множество students в отсортированный список
students_sorted = sorted(students)

#Создаём пустой словарь для хранения среднего балла
average_grades = {}

#Формируем словарь, связывая студентов с их оценками, вычисляем средний бал
for name, grades_list in zip(students_sorted, grades):
    average_grades[name] = sum(grades_list) / len(grades_list)

#Вывод
print(average_grades)