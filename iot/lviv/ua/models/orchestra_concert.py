from iot.lviv.ua.models.concert_hall_event import ConcertHallEvent
from iot.lviv.ua.enums.tech_instruments import TechInstruments


class OrchestraConcert(ConcertHallEvent):

    def __init__(self, musicians_count=0, event_duration=0,
                 event_name="", ticket_price=0,
                 instruments=TechInstruments, orchestra_name=""):
        super().__init__(musicians_count, event_duration,
                         event_name, ticket_price)
        self.instruments = instruments
        self.orchestra_name = orchestra_name

    def __str__(self):
        return str(super().__str__()) + ", " +\
               self.orchestra_name + ", " + str(self.instruments)
