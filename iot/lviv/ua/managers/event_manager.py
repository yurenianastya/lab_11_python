from iot.lviv.ua.models.concert_hall_event import ConcertHallEvent


class EventManager:

    def __init__(self, events_list=[]):
        self.events_list = events_list

    def sort_by_musicians_quantity(self, reverse=False):
        return sorted(self.events_list,
                      key=lambda musician: musician.musicians_count,
                      reverse=reverse)

    def sort_by_average_price(self, reverse=False):
        return sorted(self.events_list,
                      key=lambda musician: musician.ticket_price,
                      reverse=reverse)

    def find_with_musicians(self):
        return list(filter(lambda musician:
                           musician.musicians_count > 0,
                           self.events_list))
