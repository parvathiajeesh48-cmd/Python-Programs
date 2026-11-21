available_window_seats = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
available_Middle_Seats = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
available_Aisle_Seats  = [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]

STANDARD_PRICE = 500.0

while True:
    print("\n-------------BUS TICKET BOOKING SYSTEM-------------")
    print("---------------------------------------------------")
    print("Which service do you need (Enter the number):")
    print("1. Book Ticket\n", 
          "2. View Seat Availability\n", 
          "3. Cancel Ticket\n",
          "4. Exit")
    
   
    option = int(input("Enter the option you need: "))

    if option == 1:
        print("\n===============Booking Ticket Portal===============")
        no_pass = int(input("Enter the number of Passengers: "))
        total_fare = 0.0
        
        for i in range(1, no_pass + 1):
            print(f"\n--- Passenger {i} ---")
            Name = input("Enter the name: ")
            Age = int(input("Enter the age: "))
            
            if Age < 12:
                discount = STANDARD_PRICE * 0.50
                passenger_fare = STANDARD_PRICE - discount
                print(f"** Child Category (Age {Age}): 50% discount applied! **")
            else:
                if Age >= 60:
                    discount = STANDARD_PRICE * 0.20 
                    passenger_fare = STANDARD_PRICE - discount
                    print(f"** Senior Citizen Category (Age {Age}): 20% discount applied! **")
                else:
                    passenger_fare = STANDARD_PRICE
                    print(f"** Adult Regular Fare **")
            
            print(f"Ticket Price: ₹{passenger_fare}")
            total_fare += passenger_fare
            
            print("[Processing Payment Gateway...]")
            pass  

            pref = int(input("Select the seat preference :\n 1. Windows\n 2. Middle\n 3. Aisle\n"))
            
            if pref == 1:
                if available_window_seats:
                    print("Available seats are:", available_window_seats)
                    sel_wseat = int(input("Enter the preferred seat: "))
                    if sel_wseat in available_window_seats:
                        available_window_seats.remove(sel_wseat)
                        print(f"Booking Confirmation: Seat {sel_wseat} successfully booked for {Name}!")
                    else:
                        print("Invalid seat selection or already booked.")
                else:
                    print("Sorry, no Window seats available!")
                    
            elif pref == 2:
                if available_Middle_Seats:
                    print("Available seats are:", available_Middle_Seats)
                    sel_mseat = int(input("Enter the preferred seat: "))
                    if sel_mseat in available_Middle_Seats:
                        available_Middle_Seats.remove(sel_mseat)
                        print(f"Booking Confirmation: Seat {sel_mseat} successfully booked for {Name}!")
                    else:
                        print("Invalid seat selection or already booked.")
                else:
                    print("Sorry, no Middle seats available!")
                    
            elif pref == 3:
                if available_Aisle_Seats:
                    print("Available seats are:", available_Aisle_Seats)
                    sel_aseat = int(input("Enter the preferred seat: "))
                    if sel_aseat in available_Aisle_Seats:
                        available_Aisle_Seats.remove(sel_aseat)
                        print(f"Booking Confirmation: Seat {sel_aseat} successfully booked for {Name}!")
                    else:
                        print("Invalid seat selection or already booked.")
                else:
                    print("Sorry, no Aisle seats available!")
            else:
                print("Invalid seat preference selected!")
                
        print(f"\nTotal Booking Amount for all passengers: ₹{total_fare}")

    elif option == 2:
        print("\n===============Available Seats===============")
        print("Window Seats (1-10):", available_window_seats)
        print("Middle Seats (21-30):", available_Middle_Seats)
        print("Aisle Seats (31-40):", available_Aisle_Seats)

    elif option == 3:
        print("\n===============Cancel Ticket Portal===============")
        cancel_seat = int(input("Enter the seat number you want to cancel: "))
        
        all_seat_ranges = [
            (1, 10, available_window_seats), 
            (21, 30, available_Middle_Seats), 
            (31, 40, available_Aisle_Seats)
        ]
        
        for start, end, seat_list in all_seat_ranges:
            if start <= cancel_seat <= end:
                if cancel_seat not in seat_list:
                    seat_list.append(cancel_seat)
                    seat_list.sort()
                    print(f"Cancellation Status: Seat {cancel_seat} successfully cancelled and added back.")
                else:
                    print(f"Cancellation Status: Seat {cancel_seat} is already available (not booked).")
                break
        else:
            print("Seat not found! Please enter a valid seat number between 1-10, 21-30, or 31-40.")

    elif option == 4:
        print("\nExit Message: Thank you for using the Bus Ticket Booking System. Goodbye!")
        break
        
    else:
        print("Invalid option! Please choose between 1 and 4.")