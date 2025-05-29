calculation_to_Unit = 24
name_of_unit = "hours"


def days_to_unit(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_Unit} {name_of_unit}."


def validate_value():

    try:

        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_unit(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered zero, please enter a positive number.")
        else:
            print("You entered a negative number, please enter a positive number.")

    except ValueError:
        print("You entered an empty value, please enter a positive number.")


user_input = input("Enter the number of days and i will convert to hours: ")
validate_value()
