from calendar import Day
from dataclasses import dataclass, field
from datetime import datetime, date, time
from typing import ClassVar



from app.services.util import generate_unique_id, date_lower_than_today_error, event_not_found_error, \
    reminder_not_found_error, slot_not_available_error


# TODO: Implement Reminder class here


# TODO: Implement Event class here


# TODO: Implement Day class here


# TODO: Implement Calendar class here
@dataclass
class Reminder:
    EMAIL: str = field(init= False, default = "email")
    SYSTEM: str = field(init=False, default= "system")
#hola
    date_time:  datetime
    type: str = ClassVar[EMAIL]

    def __str__(self)-> str:
        return f"Reminder on {self.date_time} of type {self.type}"
@dataclass
class Event:
    title: str
    description: str
    date_: date
    start_at: time
    end_at: time
    reminders: list[Reminder] = field(init=False, default= list)
    id: str = field(default_factory = generate_unique_id)

    def add__reminder(self, date_time: datetime, type: str):
        self.reminders.append(Reminder(date_time, type))
    def deleate_reminder(self, Reminder_index: int):
        Reminder_index: int = Reminder_index
        for reminder in self.reminders:
            pass

class Day:
    date_: date
    slots: dict[time,str | None ]
    def __init__(self, date_: date):
        self.date_ = date_
        self.slots = []


    def _init_slots(self):
        pass
    def add_event(self, event_id: str, start_at: time, end_at: time):
        pass
    def delete_event(self, event_id: str):
        pass
    def update_event(self, event_id: str, start_at: time, end_at: time):
        pass






    class Calendar:
        days: dict[date, Day]
        def __init__(self):
            pass
        def add_event(self, title: str, description: str, date_: date, start_at: time, end_at: time)-> str:
            pass
        def update_event(self,event_id: str, title: str, description: str, date_: date, start_at: time, end_at: time ):
            pass
        def delete_event(self,event_id: str):
            pass
        def fid_events(self,start_at: time, end_at: date)-> dict[date, list["Event"]]:
            pass
        def add_reminder(self, event_id: str,date_time: datetime, type: str):
            pass
        def delete_reminder(self, event_id: str, Reminder_index: int):
            pass
        def list_reminders(self, event_id: str)-> list[Reminder]:
            pass
        def find_available_slots(self,date_: date) -> list[time]:
            pass



















