# Monkey patch
from collections.abc import Sequence


class Seq(Sequence):

    data = []

    def __getitem__(self, i):
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError



# PATCH:!!!!!!!!!!
def get_item(s, i):
    return s.data[i]

def get_len(s):
    return len(s.data)

Seq.__getitem__ = get_item
Seq.__len__ = get_len

s = Seq()
s.data.extend(list('LLKKJJ'))
print(s[2])
print(len(s))