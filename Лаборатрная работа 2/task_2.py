money_capital = 20000
salary = 5000
spend = 6000
increase = 0.05

months = 0
budget = money_capital

while budget + salary >= spend:
    # Получаем зарплату и тратим
    budget = budget + salary - spend
    months += 1
    # Цены растут на следующий месяц
    spend = spend + spend * increase

print("Количество месяцев, которое можно протянуть без долгов:", months)