"""
Концертний зал Реалізуйте ієрархію вистав , які можуть відбуватися
в концертному залі ( наприклад - циркове шоу, концерт симф оркестру, і т.д.)
Реалізуйте пошук вистав, в яких участь беруть музиканти, та виведіть результат,
відсортований за кількістю залучених музикантів. Реалізувати можливість
сортування вистав за середньою ціною квитків. Реалізація сортування
має передбачати можливість сортувати як за спаданням так і за зростанням
"""


class ConcertHallEvent:

    def __init__(self, musicians_count=0, event_duration=0,
                 event_name="", ticket_price=0):
        self.musicians_count = musicians_count
        self.event_duration = event_duration
        self.event_name = event_name
        self.ticket_price = ticket_price

    def __del__(self):
        print('\n', "May the force be with you: " + self.event_name)

    def __str__(self):
        return self.event_name + ", " + str(self.musicians_count) + ", " +\
              str(self.event_duration) + ", " + str(self.ticket_price)






