from collections import namedtuple, abc


Card = namedtuple('Card', ['rank', 'suit'])


class FrenchDeck2(abc.MutableSequence):

    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, position, value):
        """Метод __setitem__ - все, что нам
        нужно для поддержки тасования…"""
        self._cards[position] = value

    def __delitem__(self, position):
        """… но чтобы создать подкласс MutableSequence , нам придется реализовать так-
        же __delitem__ - абстрактный метод, определенный в этом ABC."""
        del self._cards[position]

    def insert(self, position, value):
        """
        Еще необходимо реализовать insert,
        третий абстрактный метод MutableSequence .
        """
        self._cards.insert(position, value)

fd = FrenchDeck2()

print(fd.pop())