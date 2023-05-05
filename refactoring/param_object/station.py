from dataclasses import dataclass


station = {
    'name': 'ZB1',
    'readings': [
        {'temp': 47, 'time': '2016-11-10 9:10'},
        {'temp': 53, 'time': '2016-11-10 9:20'},
        {'temp': 57, 'time': '2016-11-10 9:30'},
        {'temp': 52, 'time': '2016-11-10 9:40'},
        {'temp': 49, 'time': '2016-11-10 9:50'},
    ]
}


@dataclass(frozen=True)
class Plan:
    tem_floor: int
    temp_ceiling: int


def readings_outside_range(station: dict,
                           temperature_range: range) -> list[dict[str, str]]:
    return [r for r in station['readings']
            if r['temp'] not in temperature_range]


work_plan = Plan(50, 55)
plan_range = range(work_plan.tem_floor, work_plan.temp_ceiling)
ref = [{'temp': 47, 'time': '2016-11-10 9:10'},
       {'temp': 57, 'time': '2016-11-10 9:30'},
       {'temp': 49, 'time': '2016-11-10 9:50'}]
res = readings_outside_range(station, plan_range)
assert res == ref
print('passed')
