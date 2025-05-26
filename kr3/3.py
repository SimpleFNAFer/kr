import random
from faker import Faker


task1 = []
task2 = []
task3 = []

surnames_num = random.randint(1, 10)
fake = Faker()
for _ in range(surnames_num):
    surname = fake.last_name()
    if random.random() < 0.5:
        task1.append(surname)
    if random.random() < 0.5:
        task2.append(surname)
    if random.random() < 0.5:
        task3.append(surname)

print("Первая задача")
print(task1)
print("Вторая задача")
print(task2)
print("Третья задача")
print(task3)

surname_task_count = {}

for surname in task1:
    surname_task_count[surname] = surname_task_count.get(surname, 0) + 1

for surname in task2:
    surname_task_count[surname] = surname_task_count.get(surname, 0) + 1

for surname in task3:
    surname_task_count[surname] = surname_task_count.get(surname, 0) + 1

print(f"Решили хотя бы одну задачу: {[s for s in surname_task_count]}")
print(f"Решили все задачи: {[s for s, n in surname_task_count.items() if n == 3]}")
print(f"Решили ровно 1 задачу: {[s for s, n in surname_task_count.items() if n == 1]}")
print(f"Решили ровно 2 задачи: {[s for s, n in surname_task_count.items() if n == 2]}")
print(f"Решили не более 2 задач: {[s for s, n in surname_task_count.items() if n <= 2]}")
