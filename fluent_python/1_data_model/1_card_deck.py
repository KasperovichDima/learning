""""Card deck example with __len__ and __getitem__."""
from collections import namedtuple
from random import choice

# Named tuples are used for simple classes without methods
Card = namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    """Card deck clss."""
    #  Getting all card ranks in nice way.
    ranks = [str(_) for _ in range(2, 11)] + list('JQKA')
    #  Getting suits.
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self) -> None:
        self.__cards = [Card(rank, suit) for rank in self.ranks
                        for suit in self.suits]

    def __len__(self):
        return len(self.__cards)

    def __getitem__(self, position: int):
        return self.__cards[position]


deck = FrenchDeck()

print('\nLEN DEMONSTARTION:')
print(len(deck))  # len demonsration

print('\n__getitem__ DEMONSTARTION:')
print(deck[0])  # getitem demonstration
print(deck[-1])  # getitem demonstration
print(choice(deck))  # random choice demonstration

print('\nSLICES DEMONSTARTION:')
print(deck[::4])  # get all spades
print(deck[:4])  # get all '2'
print(deck[36:44])  # get all 'J' and 'Q'

print('\nITERATION DEMONSTARTION:')
for card in deck:
    print(card)

print('\nREVERSE ITERATION DEMONSTARTION:')
for card in reversed(deck):
    print(card)

"""Если в коллекции отсутствует метод __contains__ ,
то оператор in производит последовательный просмотр"""
print('\nIN DEMONSTARTION:')
print(Card('6', 'hearts') in deck)
print(Card('6', 'some_shit') in deck)

"""Sorting. Приведенная ниже функция ранжирует карты, следуя
этому правилу: 0 означает двойку треф, a 51 - туз пик"""
# cool way to create dicts
suite_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card: Card) -> int:
    """
    1. get the index of the card rank
    2. get start index of this rank in the deck
    3. add suite value of the card and add it to start index (2)
    """
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suite_values) + suite_values[card.suit]


print('\nSORTING DEMONSTARTION:')
# just use a function name as a key
for card in sorted(deck, key=spades_high):
    print(card)

"""
Как правило, специальный метод вызывается неявно. Например, предложе-
ние for i in x: подразумевает вызов функции iter(x) , которая, в свою очередь,
может вызывать метод x.__iter__() , если он реализован, или использовать x.__
getitem__() , как в примере класса FrenchDeck .
"""
