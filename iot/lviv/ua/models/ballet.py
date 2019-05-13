from iot.lviv.ua.models.concert_hall_event import ConcertHallEvent
from iot.lviv.ua.enums.dance_style import BalletStyle


class Ballet(ConcertHallEvent):

    def __init__(self, musicians_count=0, event_duration=0,
                 event_name="", ticket_price=0, ballet_name="",
                 dance_style=BalletStyle):
        super().__init__(musicians_count, event_duration,
                         event_name, ticket_price)
        self.ballet_name = ballet_name
        self.dance_style = dance_style

    def __str__(self):
        return super().__str__() + ", " + self.ballet_name +\
               ", " + str(self.dance_style)
