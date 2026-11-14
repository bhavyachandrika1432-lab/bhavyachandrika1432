import random
from datetime import datetime

# --------------------- TRAIN CLASS ---------------------

class Train:
    def __init__(self, train_num, source, destination, seats):
        self.train_num = train_num
        self.source = source
        self.destination = destination

        # Available seats in each travel class
        self.seats = {
            "SL": seats,
            "3AC": max(1, seats // 2),
            "2AC": max(1, seats // 3),
            "1AC": max(1, seats // 4)
        }

        self.waiting_list = {
            "SL": 0,
            "3AC": 0,
            "2AC": 0,
            "1AC": 0
        }

        self.berths = ["L", "U", "M", "SU", "SL"]
        self.berth_count = 0

    def display_info(self):
        print(f"\nTrain Number: {self.train_num}")
        print(f"Source: {self.source}")
        print(f"Destination: {self.destination}")
        print("Available seats:")
        for travel_class, count in self.seats.items():
            print(f"{travel_class}: {count}")

    def book_seat(self, travel_class):
        if self.seats[travel_class] > 0:
            self.seats[travel_class] -= 1
            berth = self.berths[self.berth_count % len(self.berths)]
            self.berth_count += 1
            return "Confirmed", berth

        self.waiting_list[travel_class] += 1
        return "Waiting List", "Not allocated"


# --------------------- PASSENGER CLASS ---------------------

class Passenger:
    def __init__(self, name, age, gender, phone):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Phone Number: {self.phone}")


# --------------------- TICKET CLASS ---------------------

class Ticket:
    def __init__(self, train, passenger, pnr, journey_date,
                 journey_time, travel_class, status, berth):
        self.train = train
        self.passenger = passenger
        self.pnr = pnr
        self.journey_date = journey_date
        self.journey_time = journey_time
        self.travel_class = travel_class
        self.status = status
        self.berth = berth

    def display_info(self):
        print("\n------------- TICKET DETAILS -------------")
        print(f"Train Number: {self.train.train_num}")
        print(f"Source: {self.train.source}")
        print(f"Destination: {self.train.destination}")
        print(f"Journey Date: {self.journey_date}")
        print(f"Journey Time: {self.journey_time}")
        print(f"Travel Class: {self.travel_class}")
        print(f"PNR Number: {self.pnr}")
        print(f"Booking Status: {self.status}")
        print(f"Berth: {self.berth}")
        self.passenger.display_info()
        print("------------------------------------------")


# --------------------- ACCOUNT CLASS ---------------------

class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_password(self, password):
        return self.password == password


# --------------------- ACCOUNT CREATION AND LOGIN ---------------------

accounts = [
    Account("user1", "password1"),
    Account("user2", "password2")
]

logged_in_account = None

while logged_in_account is None:
    print("\n1. Create an account")
    print("2. Login")
    choice = input("Enter choice: ")

    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")

        if any(account.username == username for account in accounts):
            print("Username already exists.")
        else:
            accounts.append(Account(username, password))
            print("Account created successfully!")

    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")

        for account in accounts:
            if account.username == username and account.check_password(password):
                logged_in_account = account
                break

        if logged_in_account is None:
            print("Invalid username or password.")
        else:
            print(f"\nLogged in as {logged_in_account.username}")

    else:
        print("Invalid choice.")


# --------------------- TRAIN DETAILS ---------------------

trains = [
    Train("12737", "Tadepalligudem", "Secunderabad", 40),
    Train("12728", "Tadepalligudem", "Visakhapatnam", 50),
    Train("22863", "Vijayawada", "Bangalore", 20)
]

print("\n--------- AVAILABLE TRAIN DETAILS ---------")
for train in trains:
    train.display_info()


# --------------------- TRAIN SELECTION ---------------------

selected_train = None

while selected_train is None:
    train_num = input("\nEnter Train Number: ")

    for train in trains:
        if train.train_num == train_num:
            selected_train = train
            break

    if selected_train is None:
        print("Invalid Train Number. Please try again.")


# --------------------- DATE AND TIME ---------------------

while True:
    try:
        date_input = input("Enter Journey Date (DD-MM-YYYY): ")
        journey_date = datetime.strptime(date_input, "%d-%m-%Y").date()

        if journey_date < datetime.now().date():
            print("Journey date cannot be in the past.")
            continue

        break
    except ValueError:
        print("Invalid date. Please enter in DD-MM-YYYY format.")

while True:
    try:
        time_input = input("Enter Journey Time (HH:MM in 24-hour format): ")
        journey_time = datetime.strptime(time_input, "%H:%M").time()
        break
    except ValueError:
        print("Invalid time. Please enter in HH:MM format.")


# --------------------- TRAVEL CLASS SELECTION ---------------------

print("\nAvailable Travel Classes:")
print("1. SL  - Sleeper")
print("2. 3AC - Third AC")
print("3. 2AC - Second AC")
print("4. 1AC - First AC")

class_options = {
    "1": "SL",
    "2": "3AC",
    "3": "2AC",
    "4": "1AC"
}

while True:
    class_choice = input("Select Travel Class (1-4): ")
    if class_choice in class_options:
        travel_class = class_options[class_choice]
        break
    print("Invalid class selection. Please try again.")


# --------------------- NUMBER OF TICKETS ---------------------

while True:
    try:
        num_tickets = int(input("Enter Number of Tickets: "))
        if num_tickets <= 0:
            print("Number of tickets must be greater than 0.")
        else:
            break
    except ValueError:
        print("Please enter a valid number.")


# --------------------- PASSENGER DETAILS AND BOOKING ---------------------

tickets = []

for i in range(num_tickets):
    print(f"\nEnter details for Passenger {i + 1}")

    while True:
        name = input("Name: ").strip()
        if name:
            break
        print("Name cannot be empty.")

    while True:
        try:
            age = int(input("Age: "))
            if 0 < age <= 120:
                break
            print("Enter a valid age.")
        except ValueError:
            print("Age must be a number.")

    gender = input("Gender: ").strip()

    while True:
        phone = input("Phone Number: ").strip()
        if len(phone) == 10 and phone.isdigit():
            break
        print("Enter a valid 10-digit phone number.")

    passenger = Passenger(name, age, gender, phone)

    status, berth = selected_train.book_seat(travel_class)
    pnr = random.randint(100000, 999999)

    ticket = Ticket(
        selected_train,
        passenger,
        pnr,
        journey_date,
        journey_time,
        travel_class,
        status,
        berth
    )

    tickets.append(ticket)


# --------------------- DISPLAY TICKETS ---------------------

print("\n========== BOOKING SUMMARY ==========")

for ticket in tickets:
    ticket.display_info()

print("\nRemaining seats in selected class:",
      selected_train.seats[travel_class])
print("Waiting list count in selected class:",
      selected_train.waiting_list[travel_class])

print("\nThank you for booking.")
print("Have a safe journey!")