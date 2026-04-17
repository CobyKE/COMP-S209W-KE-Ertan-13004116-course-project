from models import Customer, Admin
from system import BookingSystem


def display_fields(system):
    fields = system.get_all_fields()
    if not fields:
        print("\nNo fields available.")
    else:
        print("\n--- Football Fields ---")
        for f in fields:
            print(f)


def register_customer(system):
    print("\n--- Customer Registration ---")
    name = input("Full name: ").strip()
    phone = input("Phone number: ").strip()
    customer = Customer(name, phone)
    if system.register_user(customer):
        print(f"Registration successful! Welcome, {name}.")
    else:
        print("User already exists.")


def book_field(system):
    display_fields(system)
    if not system.get_all_fields():
        return
    try:
        field_id = int(input("\nEnter field ID to book: "))
        customer_name = input("Enter your registered name: ").strip()
        date_str = input("Booking date (YYYY-MM-DD): ").strip()
        start_time = input("Start time (HH:MM): ").strip()
        duration = int(input("Duration (hours): "))
    except ValueError:
        print("Invalid input format.")
        return

    booking = system.create_booking(field_id, customer_name, date_str, start_time, duration)
    if booking:
        print("\nBooking Successful!")
        print(booking.summary())
    else:
        print("\nBooking failed. Check field availability or user registration.")


def view_my_bookings(system):
    name = input("Enter your name: ").strip()
    bookings = system.get_bookings_by_user(name)
    if not bookings:
        print("\nNo bookings found.")
    else:
        print(f"\n--- Bookings for {name} ---")
        for i, b in enumerate(bookings, 1):
            print(f"{i}. {b.summary()} (Booked at {b.timestamp})")


def admin_add_field(system):
    print("\n--- Admin: Add New Field ---")
    try:
        field_id = int(input("Enter new field ID (integer): "))
    except ValueError:
        print("Invalid ID. Must be an integer.")
        return

    if system.find_field_by_id(field_id) is not None:
        print(f"Field ID {field_id} already exists. Cannot add duplicate ID.")
        return

    location = input("Location: ").strip()
    size = input("Size (5-a-side/7-a-side/11-a-side): ").strip()
    try:
        rate = float(input("Hourly rate (HKD): "))
    except ValueError:
        print("Invalid rate.")
        return

    field = system.add_field(field_id, location, size, rate)
    if field:
        print(f"Field added successfully! {field}")
    else:
        print("Failed to add field.")


def main():
    system = BookingSystem()
    admin = Admin("Admin", "00000000")
    system.register_user(admin)

    while True:
        print("\n===== Football Field Booking System (OOP) =====")
        print("1. Admin: Add new field")
        print("2. View all fields")
        print("3. Register as customer")
        print("4. Book a field")
        print("5. View my bookings")
        print("6. Exit")
        choice = input("Select option: ").strip()

        if choice == '1':
            admin_add_field(system)
        elif choice == '2':
            display_fields(system)
        elif choice == '3':
            register_customer(system)
        elif choice == '4':
            book_field(system)
        elif choice == '5':
            view_my_bookings(system)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()