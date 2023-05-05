def create_title():
    """Variable incapsulation."""
    tpHd = "untitled"

    def wrapper(arg: str | None = None):
        nonlocal tpHd
        if arg:
            tpHd = arg
            return
        return tpHd

    return wrapper


title = create_title()


result = ''
result += f'<h1>{title()}</h1>'
print(result)
