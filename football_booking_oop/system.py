from models import Field, Customer, Admin, Booking, User


class BookingSystem:
    def __init__(self):
        self.__fields = []          
        self.__users = []           
        self.__bookings = []        

    def add_field(self, field_id: int, location: str, size: str, rate: float):
        if self.find_field_by_id(field_id) is not None:
            return None
        field = Field(field_id, location, size, rate)
        self.__fields.append(field)
        return field

    def get_all_fields(self):
        return self.__fields.copy()

    def find_field_by_id(self, field_id: int):
        for f in self.__fields:
            if f.id == field_id:
                return f
        return None

    def register_user(self, user: User):
        if self.find_user_by_name(user.name) is None:
            self.__users.append(user)
            return True
        return False

    def find_user_by_name(self, name: str):
        for u in self.__users:
            if u.name == name:
                return u
        return None

    def get_all_users(self):
        return self.__users.copy()

    def create_booking(self, field_id: int, customer_name: str,
                       date_str: str, start_time: str, duration: int) -> Booking or None:
        field = self.find_field_by_id(field_id)
        if not field or not field.available:
            return None

        user = self.find_user_by_name(customer_name)
        if not user or not isinstance(user, Customer):
            return None

        if field.book():
            booking = Booking(field, user, date_str, start_time, duration)
            self.__bookings.append(booking)
            return booking
        return None

    def get_bookings_by_user(self, customer_name: str):
        return [b for b in self.__bookings if b.customer.name == customer_name]

    def get_all_bookings(self):
        return self.__bookings.copy()