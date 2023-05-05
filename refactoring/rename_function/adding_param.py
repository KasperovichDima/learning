class Book:

    def __init__(self) -> None:
        self.reservation_queue = []

    def add_reservation(self, customer) -> None:
        self.tmp_add_reservation(customer, False)

    def tmp_add_reservation(self, customer, is_priority: bool) -> None:
        self.reservation_queue.append(customer)
