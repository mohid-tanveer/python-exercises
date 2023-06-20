# Exercise: APR calculator

# Description: 
# This APR caculator prompts the user to choose from two scenarios and when prompted will further prompt 
# for the user to input given values that apply to the scenario they choose. It will then run these values 
# through the APR calculator algorithm to correctly calculate the APR for the certain scenario. When calculated 
# it will output this value in a print function that reflects accurately what scenario and values the user inputed.

DAYS_PER_YEAR = 365 #declares how many days in a year
MONTHS_PER_YEAR = 12 #declares how many months in a year

# This function prints off the intro sequence for the APR calculator.
# Parameters: n/a
# Returns: n/a
def intro_sequence():
    print("Welcome to the payday loan APR calculator.")
    print("Please have the proposed terms of your payday loan handy so we can calculate the APR.\n")
    print("Select which one best fits your situation.")
    print("  (1) I know the total loan amount, the finance charge, and the repayment period (in days or months).")
    print("  (2) I know the fee in dollars for every 100 dollars borrowed and the repayment period (in days or months).\n")

# This function determines the amount of money loaned for scenario 1. In the case of scenario 2 it sets this value to 1 to keep the equation later seen in the apr_calculator() function clean
# Parameters: user_input, user's choice of scenario.
# Returns: the amount of money that is loaned out for scenario 1 or just returns 1 for scenario 2.
def loan_amt(user_input): 
    if user_input == '1':
        loan_amt = float(input("What is the total loan amount? "))
        return loan_amt
    else:
        loan_amt = 1 #sets loan amount to 1 since scenario 2's formula has a fee but no loan amount 
        return loan_amt
    
# This function determines the finanace charge of the loan.
# Parameters: user_input, user's choice of scenario.
# Returns: the finance charge of the loan.
def finance_chg(user_input):
    if user_input == '1':
        finance_chg = float(input("What is the finance charge for the loan? "))
        finance_chg = finance_chg * 100 #multiplies finance charge by 100 to account for the times 100 in the scenario 1 formula
        return finance_chg
    else:          
        finance_chg = float(input("What is the fee for each $100 borrowed? "))
        return finance_chg
    
# This function determines the amount of days or months for the repayment period.
# Parameters: day_month, user's choice of days or months.
# Returns: the repayment period in days or months.
def day_or_month(day_month):
    if day_month == 'd' or day_month == 'D': 
        repayment_period = int(input("How many days is the repayment period? "))                 
        return repayment_period 
    elif day_month == 'm' or day_month == 'M':
        repayment_period = int(input("How many months is the repayment period? "))                       
        return repayment_period
            
# This function computes the APR of the loan.
# Parameters: loan_amt, the amount that was loaned; finance_chg, the finance charge; repayment_period, the repayment period;                     day_month, user's choice of days or month.
# Returns: the APR of the loan.
def apr_calculator(loan_amt, finance_chg, repayment_period, day_month):
    if day_month == 'd' or day_month == 'D': 
        fee_amt = (finance_chg / loan_amt)
        repayment_period = DAYS_PER_YEAR / repayment_period #divides 365 by repayment period for 'day' selection
        apr_calculated = fee_amt * repayment_period
        return apr_calculated
    elif day_month == 'm' or day_month == 'M':
        fee_amt = (finance_chg / loan_amt)
        repayment_period = MONTHS_PER_YEAR / repayment_period #divides 12 by repayment period for 'month' selection
        apr_calculated = fee_amt * repayment_period
        return apr_calculated
     
# This function prints off the APR along with the repayment period in either days or months.
# Parameters: repayment_period, the repayment period; apr_calculated, the APR of the loan; day_month, user's choice of days or                   month.
# Returns: n/a
def outro_sequence(repayment_period, apr_calculated, day_month):
    if day_month == 'd' or day_month == 'D': 
        length_period = 'day'
    elif day_month == 'm' or day_month == 'M':
        length_period = 'month'
    print("\nYour ", repayment_period, ' ', length_period, " loan has an APR of {:.2f}".format(apr_calculated), "%.", sep='')         #formats calculated apr value to only display up until 2 rounded decimal points
       
# This function runs the program.
# Parameters: n/a
# Returns: n/a
def main():
    intro_sequence()
    scenario_choice = input("How was the information given to you? Choose (1) or (2): ")
    loan_amount = loan_amt(scenario_choice)
    finance_charge = finance_chg(scenario_choice)
    day_month = input("Is the length of the repayment period in days or months? Enter d or m: ")
    length_choice = day_or_month(day_month)
    apr_calculated = apr_calculator(loan_amount, finance_charge, length_choice, day_month)
    outro_sequence(length_choice, apr_calculated, day_month)

main()    
       
    
         
                        
                     
                         