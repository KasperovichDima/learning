class Address:
    def __init__(self, state: str) -> None:
        self.state = state


class Customer:
    def __init__(self, address: Address) -> None:
        self.address = address


# def in_New_England(customer: Customer) -> bool:
#     return tmp_in_New_England(customer.address.state)


def in_New_England(state_code: str) -> bool:
    return state_code in 'MA CT ME VT NH RI'.split()


def main():
    customers: list[Customer] = []
    new_englanders = [_ for _ in customers if in_New_England(_.address.state)]

    customer1 = Customer(
        Address('VT')
    )
    customer2 = Customer(
        Address('NY')
    )

    print(in_New_England(customer1.address.state))
    print(in_New_England(customer2.address.state))


if __name__ == '__main__':
    main()
