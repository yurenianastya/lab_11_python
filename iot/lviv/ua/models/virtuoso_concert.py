from iot.lviv.ua.models.concert_hall_event import ConcertHallEvent


class VirtuosoConcert(ConcertHallEvent):

    def __init__(self, musicians_count=0, event_duration=0,
                 event_name="", ticket_price=0, virtuoso_name="",
                 composers_name=""):
        super().__init__(musicians_count, event_duration,
                         event_name, ticket_price)
        self.virtuoso_name = virtuoso_name
        self.composers_name = composers_name

    def __str__(self):
        return super().__str__() + ", " + self.virtuoso_name + ", " +\
            self.composers_name
