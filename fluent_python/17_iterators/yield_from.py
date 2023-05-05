def sub_gen():
    yield 1.1
    yield 1.2

def gen():
    yield 1
    yield from sub_gen()
    yield 2

for _ in gen():
    print(_)

# ->
# 1
# getting data from subgen using yield from
# 1.1 
# 1.2
# 2


# More complicated example - printing exception cls tree:

# def sub_tree(cls):
#     for sub in cls.__subclasses__(): # __subclasses__() is a special method!!!
#         yield sub.__name__, 1
#         for subsub in sub.__subclasses__():
#             yield subsub.__name__, 2
#             for subsubsub in subsub.__subclasses__():
#                 yield subsubsub.__name__, 3

# def sub_tree(cls, lvl):
#     """Cool Recursion example."""
#     for sub in cls.__subclasses__():
#         yield sub.__name__, lvl
#         yield from sub_tree(sub, lvl + 1)


def tree(cls, lvl=1):
    yield cls.__name__, lvl
    for _ in cls.__subclasses__():
        yield from tree(_, lvl+1)

def display(cls):
    for cls_name, level in tree(cls):
        print('    ' * level, cls_name)

if __name__ == '__main__':
    display(BaseException)
