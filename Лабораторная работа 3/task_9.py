salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

for _ in range(1, months + 1):
    need_money_for_month = spend - salary
    spend += spend * increase
    need_money += need_money_for_month

print(round(need_money))
