'''Converts user input fahrenheit degree to celsius'''  
def convert_to_celsius(temperature_in_fahrenheit):

    try:
        # try will attempt do the risky task and encompasses almost the entire function logic
        temperature_in_fahrenheit = float(temperature_in_fahrenheit)
        celsius = round((temperature_in_fahrenheit - 32) * 5/9, 2)
        return celsius
    except (TypeError, ValueError):

        print("Enter a valid temperature")
        return None #Return None for error cases, this will be used for comparison in the main code
    
    
while True:
    # the user will continue to be asked for valid input
    fahrenheit = input("Enter a temperature in Fahrenheit: ")
    result = convert_to_celsius(fahrenheit)
    if result is not None:
        print(f"The temperature is {result}ºC")
        break