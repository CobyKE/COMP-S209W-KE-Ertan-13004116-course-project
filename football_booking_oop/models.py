from abc import ABC, abstractmethod
from datetime import datetime

# FIELD CLASS
# Access is controlled via @property getters and methods like book()
class Field:
    def __init__(self, field_id: int, location: str, size: str, rate: float):
        self.__id = field_id
        self.__location = location
        self.__size = size          
        self.__rate = rate
        self.__available = True     
    @property
    def id(self):
        return self.__id

    @property
    def location(self):
        return self.__location

    @property
    def size(self):
        return self.__size

    @property
    def rate(self):
        return self.__rate

    @property
    def available(self):
        return self.__available

    def book(self):
        if self.__available:
            self.__available = False
            return True
        return False

    def release(self):
        self.__available = True

    def __str__(self):
        status = "Available" if self.__available else "Booked"
        return f"ID: {self.__id} | {self.__location} | {self.__size} | ${self.__rate}/hr | {status}"


# USER ABSTRACT BASE CLASS
class User(ABC):
    def __init__(self, name: str, phone: str):
        self._name = name
        self._phone = phone

    @property
    def name(self):
        return self._name

    @property
    def phone(self):
        return self._phone

    @abstractmethod
    def get_role(self) -> str:
        pass

    def __str__(self):
        return f"{self.get_role()}: {self._name} ({self._phone})"

# CUSTOMER CLASS
class Customer(User):
    def get_role(self):
        return "Customer"

    def view_my_bookings(self, booking_system):
        return booking_system.get_bookings_by_user(self._name)

# ADMIN CLASS
class Admin(User):
    def get_role(self):
        return "Administrator"

    def add_field(self, booking_system, field_id, location, size, rate):
        return booking_system.add_field(field_id, location, size, rate)

# BOOKING CLASS
class Booking:
    def __init__(self, field: Field, customer: Customer, date_str: str,
                 start_time: str, duration: int):
        self.__field = field
        self.__customer = customer
        self.__date = date_str
        self.__start_time = start_time
        self.__duration = duration
        self.__total_cost = field.rate * duration
        self.__timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    @property
    def field(self):
        return self.__field

    @property
    def customer(self):
        return self.__customer

    @property
    def date(self):
        return self.__date

    @property
    def start_time(self):
        return self.__start_time

    @property
    def duration(self):
        return self.__duration

    @property
    def total_cost(self):
        return self.__total_cost

    @property
    def timestamp(self):
        return self.__timestamp

    def summary(self):
        return (f"Field: {self.__field.location} ({self.__field.size}) | "
                f"Date: {self.__date} {self.__start_time} | "
                f"{self.__duration} hrs | Cost: ${self.__total_cost:.2f}")