class PerfomanceCalculator:
    def __init__(self, perfomance, play) -> None:
        self.performance = perfomance
        self.play = play

    @property
    def amount(self) -> int: ...

    @property
    def volume_credits(self) -> int:
        return max(self.performance['audience'] - 30, 0)


class TragedyCalculator(PerfomanceCalculator):

    @property
    def amount(self) -> int:
        result = 40_000
        if self.performance['audience'] > 30:
            result += 1_000 * (self.performance['audience'] - 30)
        return result


class ComedyCalculator(PerfomanceCalculator):

    @property
    def volume_credits(self) -> int:
        return super().volume_credits + round(self.performance['audience'] / 5)

    @property
    def amount(self) -> int:
        result = 30_000
        if self.performance['audience'] > 20:
            result += 10_000 + 500 * (self.performance['audience'] - 20)

        result += 300 * self.performance['audience']

        return result


def get_calculator(perfomance, play) -> PerfomanceCalculator:
    match play['type']:
        case 'tragedy':
            return TragedyCalculator(perfomance, play)
        case 'comedy':
            return ComedyCalculator(perfomance, play)
        case _:
            raise TypeError('unknown play type...')


def create_satement_data(invoice, plays):

    def enrich_performance(performance: dict):

        def play_for(performance: dict[str, str]) -> str:
            play_id = performance['play_id']
            return plays[play_id]

        calculator = get_calculator(
            performance,
            play_for(performance),
        )

        performance['play'] = calculator.play
        performance['amount'] = calculator.amount
        performance['volume_credits'] = calculator.volume_credits
        return performance

    def total_volume_credits():
        return sum((_['volume_credits'] for _ in result['performances']))

    def total_amount():
        return sum((_['amount'] for _ in result['performances']))

    result = {}
    result['customer'] = invoice['customer']
    result['performances'] = [enrich_performance(_)
                              for _ in invoice['performances']]
    result['total_volume_credits'] = total_volume_credits()
    result['total_amount'] = total_amount()
    return result
