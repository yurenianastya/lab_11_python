from iot.lviv.ua.enums.dance_style import BalletStyle
from iot.lviv.ua.enums.tech_instruments import TechInstruments
from iot.lviv.ua.models.ballet import Ballet
from iot.lviv.ua.models.concert_hall_event import ConcertHallEvent
from iot.lviv.ua.models.virtuoso_concert import VirtuosoConcert
from iot.lviv.ua.models.orchestra_concert import OrchestraConcert
from iot.lviv.ua.managers.event_manager import EventManager


class Main:

    @staticmethod
    def main():
        swan_lake = Ballet(0, 3, "Royal Theatre",
                           450, "The Swan Lake", BalletStyle.ROMANTIC)
        print(str(swan_lake))
        raleigh_ringers = OrchestraConcert(20, 2, "The Bellringing Symphony",
                                           500, TechInstruments.LAMP,
                                           "The Raleigh Ringers")
        print(str(raleigh_ringers))

        leif_andsnes = VirtuosoConcert(1, 2, "Leif Andsnes Grand Concert",
                                       300, "Leif Ove Andsnes",
                                       "W.A.Mozart and J.S.Bach")
        print(str(leif_andsnes))

        event_manager = EventManager([swan_lake, raleigh_ringers, leif_andsnes])

        print('\n', "Printing sorting ticket by descending")

        print(*event_manager.sort_by_average_price(True), sep='\n')

        print('\n', "Printing sorting by musicians by descending")

        print(*event_manager.sort_by_musicians_quantity(False), sep='\n')

        print('\n', "Printing events with musicians")

        print(*event_manager.find_with_musicians(), sep='\n')


if __name__ == '__main__':
    Main.main()
