salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

def calculate_required_capital(salary, spend, months, increase_rate):
    total_extra_needed = 0

    for month in range(months):
        if month > 0:
            spend *= (1 + increase_rate)

        monthly_difference = spend - salary
        if monthly_difference > 0:
            total_extra_needed += monthly_difference

    return round(total_extra_needed, 2)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", calculate_required_capital(salary, spend, months, increase))
