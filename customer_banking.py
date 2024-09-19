# Import the necessary functions
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and CD account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account
    savings_balance = float(input("Enter the initial balance for your savings account: "))
    savings_interest = float(input("Enter the annual interest rate (APR) for your savings account (as a percentage): "))
    savings_maturity = int(input("Enter the number of months for which the interest is calculated: "))

    # Call the create_savings_account function and pass the variables from the user
    updated_savings_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months
    print(f"\nSavings Account Interest Earned: ${savings_interest_earned:.2f}")
    print(f"Updated Savings Account Balance: ${updated_savings_balance:.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account
    cd_balance = float(input("\nEnter the initial balance for your CD account: "))
    cd_interest = float(input("Enter the annual interest rate (APR) for your CD account (as a percentage): "))
    cd_maturity = int(input("Enter the number of months for which the interest is calculated: "))

    # Call the create_cd_account function and pass the variables from the user
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months
    print(f"\nCD Account Interest Earned: ${cd_interest_earned:.2f}")
    print(f"Updated CD Account Balance: ${updated_cd_balance:.2f}")

if __name__ == "__main__":
    # Call the main function
    main()
