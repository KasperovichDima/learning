"""
Вы открываете собственную авторскую програм-
му на радио и хотите, чтобы вас слушали во всех
50 штатах. Нужно решить, на каких радиостанци-
ях должна транслироваться ваша передача. Каждая
станция стоит денег, поэтому количество станций не-
обходимо свести к минимуму. Имеется список станций.
Каждая станция покрывает определенный набор штатов,
эти наборы перекрываются. Как найти минимальный
набор станций, который бы покрывал все 50 штатов?
"""

#  Satates we want to cover
states_needed = set('mt wa or id nv ut ca az'.split())

#  Awailible stations
stations = dict(
    kone={'id', 'nv', 'ut'},
    ktwo={"wa", "id", "mt"},
    kthree={"or", "nv", "ca"},
    kfour={"nv", "ut"},
    kfive={"ca", "az"}
)
chosen_stations: set[str] = set()

while states_needed:  # Wile all states we need are not covererd
    best_station = ''  # init var as str
    states_covered: set[str] = set()  # tmp result
    for st_name, st_states in stations.items():  # for each station
        # coverage — множество штатов, не входящих в
        # покрытие, которые покрываются текущей станцией
        coverage = states_needed & st_states
        if len(coverage) > len(states_covered):  #  if this station covers more
                                                 #  needed states then previous one:
            best_station = st_name  # update best station name
            states_covered = coverage  # update best coverage

    chosen_stations.add(best_station)  # add best station to chosen lst
    states_needed.difference_update(states_covered)  # remove states, covered by
                                                     # best station from needed lst

print(chosen_stations)
