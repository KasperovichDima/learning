"""Словарные включения"""

dial_codes = [
    (880, 'Bangladesh'),
    (55, 'Brazil'),
    (86, 'China'),
    (91, 'India'),
    (62, 'Indonesia'),
    (81, 'Japan'),
    (234, 'Nigeria'),
    (92, 'Pakistan'),
    (7, 'Russia'),
    (1, 'United States'),
 ]

country_dial = {country: dial for dial, country in dial_codes}
print(country_dial)
# {'Bangladesh': 880, 'Brazil': 55, 'China': 86, 'India': 91, 'Indonesia': 62,
# 'Japan': 81, 'Nigeria': 234, 'Pakistan': 92, 'Russia': 7, 'United States': 1}

# Сортируем country_dial по названию страны, снова инвертируем пары,
# преобразуем значения в верхний регистр и оставляем только элементы, для
# которых code < 70.
sorted_c_dial = {dial: country for country, dial
                 in sorted(country_dial.items()) if dial < 70}
print(sorted_c_dial)
# {55: 'Brazil', 62: 'Indonesia', 7: 'Russia', 1: 'United States'}
