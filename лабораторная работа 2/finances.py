money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество месяцев, которое можно протянуть без долгов

def calculate_months_to_survive(money_capital, salary, spend, increase_rate):
    months_survived = 0

    while money_capital >= 0:
        # Проверяем, хватает ли бюджета на текущий месяц
        monthly_budget = salary + money_capital
        if monthly_budget < spend:
            break

        # Вычитаем расходы из бюджета и добавляем месяц к счетчику
        money_capital -= (spend - salary)
        months_survived += 1

        # Увеличиваем расходы на следующий месяц
        spend *= (1 + increase_rate)

    return months_survived


print("Количество месяцев, которое можно протянуть без долгов:", calculate_months_to_survive(money_capital, salary, spend, increase))

