preis_sekt = 0.75
end_preis = 0
total_price = []

while True:
    preis_adult = 5.0
    preis_child = 2.5
    preis_premium = 3.0
    preis_basic = 4.0
    preis_teen = 3.5

    print(" ### Museum XXX Ticket Calculator ### ")
    print(" Would you like a full-day ticket or a half-day ticket?")
    print(" The standard price is for the half-day ticket.")
    print(" For a full-day ticket, please enter '1'; for a half-day ticket, please enter '2'.")

    day_choice = input().lower()
    if day_choice == "1":
        preis_adult *= 2
        preis_child *= 2
        preis_premium *= 2
        preis_basic *= 2
        preis_teen = 6

    print(" Please enter your age.")
    guest_age = int(input())

    if guest_age < 14:
        print(" ### Children's Ticket ### ")
        end_preis = preis_child
        print(" Price: ", end_preis, " Euros ")
    elif guest_age <= 17:
        print(" ### Teen Ticket ### ")
        end_preis = preis_teen
        print(" Price: ", end_preis, " Euros")
    else:
        print(" Are you a member of the Duisburg Museum Club? (Proof required) ")
        print(" If you are a Premium member, enter 'p'.")
        print(" If you are a Basic member, enter 'b'.")
        print(" If you are not a member, press any other key.")
        membership_response = input().lower()

        if membership_response == "p":
            end_preis = preis_premium
            print(" ### Premium Member Ticket ### ")
            print(" Price: ", end_preis, " Euros ")
            if guest_age >= 18:
                print(" Would you like a glass of champagne for an additional", preis_sekt, "€? (yes/no)")
                drink_choice = input().lower()

                if drink_choice == "yes":
                    end_preis += preis_sekt
                    print(" Enjoy your drink! ")
                    print(" Your updated price is", end_preis, "€!")

                elif drink_choice == "no":
                    print(" Your total price is", end_preis, "€!")

        elif membership_response == "b":
            end_preis = preis_basic
            print(" ### Basic Member Ticket ### ")
            print(" Price: ", end_preis, " Euros ")

        else:
            end_preis = preis_adult
            print(" ### Adult Ticket (full price) ### ")
            print(" Price: ", end_preis, " Euros")

    # Add current ticket price to total price list
    total_price.append(end_preis)
    print(" Your current total is", sum(total_price), "Euros.")

    # Ask if the user wants another ticket
    print(" Would you like to purchase another ticket? (yes/no)")
    more_tickets = input().lower()
    if more_tickets != "yes":
        break

# Final total price output
print(" The final total is", sum(total_price), "!")
print(" ### Enjoy your visit! ### ")

# Console Smiley
print("  *****  ")
print(" *     * ")
print("*  O O  *")
print("*   ^   *")
print(" * '-' * ")
print("  *****  ")


y