def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        number = float(number_str)
        if number <= 0:
            raise ValueError(f'Value must be > 0: {number_str}')
    except ValueError:
        return True 
    
    return False

prompt("Welcome to the Loan Calculaotor")


prompt("Please enter your loan amount here")
loan_amount = input()  

while invalid_number(loan_amount):
    prompt("Must enter a positive number")
    loan_amount = input()



prompt("Next. What is your interest rate? ")
interest_rate = (input()) 

while invalid_number(interest_rate):
    prompt('Must enter a positive number')
    interest_rate = input()

prompt("Enter your loan duration in years.")
years  = input() 

while invalid_number(years):
    prompt("Must enter a positive number")
    years = input()



annual_interest_rate = float(interest_rate) / 100
monthly_interest_rate = annual_interest_rate / 12 
months = float(years) / 12 
loan_amount = float(loan_amount)

monthly_payment = loan_amount * ( monthly_interest_rate /
            (1 - (1 + monthly_interest_rate) ** (-months))
    )


prompt(f"Your monthly payment is: ${monthly_payment:.2f}")