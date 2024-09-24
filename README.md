# customer-banking

## Technology Used 

| Technology Used | Resource URL | 
| ------------- |:-------------:| 
| Python | [https://www.w3schools.com/python/python_reference.asp](https://www.w3schools.com/python/python_reference.asp) | 
| Git | [https://git-scm.com/](https://git-scm.com/) | 

## Description 
In this project I created a(COMPLETE)....

## Code Example 

<---- First we import the necessary modules and classes to ensure that all dependencies are available and we can interact with the Account class and account creation functions. This is crucial as it links various parts of the application together. ----->


      from Account import Account
      from cd_account import create_cd_account
      from savings_account import create_savings_account

<---- In this part of the code we define the structure of the Account class which provides the foundational methods for setting the balance and interest. This encapsulates account-related functionality, allowing reuse across different account types. ----->


     class Account:
         def __init__(self, balance, interest):
              self.balance = balance
              self.interest = interest

         def set_balance(self, balance):
             self.balance = balance

         def set_interest(self, interest):
             self.interest = interest

<---- Next we define functions for creating savings and CD accounts, which calculate interest earned and update the account balances. These functions take user-provided inputs and perform key operations related to interest calculation. ----->


     def create_savings_account(balance, interest_rate, months):
         account = Account(balance, interest_rate)
         interest_earned = (balance * (interest_rate / 100) * (months / 12))
         updated_balance = balance + interest_earned
         account.set_balance(updated_balance)
         account.set_interest(interest_earned)
         return updated_balance, interest_earned

     def create_cd_account(balance, interest_rate, months):
         cd_account = Account(balance, interest_rate)
         interest_earned = (balance * (interest_rate / 100) * (months / 12))
         updated_balance = balance + interest_earned
         cd_account.set_balance(updated_balance)
         cd_account.set_interest(interest_earned)
         return updated_balance, interest_earned

<------ Here we prompt the user for inputs to gather the necessary details like balance, interest rate, and months. This is vital for customizing the account creation process based on user needs. ------>


     savings_balance = float(input("Enter the initial balance for your savings account: "))
     savings_interest = float(input("Enter the annual interest rate (APR) for your savings account (as a percentage): "))
     savings_maturity = int(input("Enter the number of months for which the interest is calculated: "))

     cd_balance = float(input("\nEnter the initial balance for your CD account: "))
     cd_interest = float(input("Enter the annual interest rate (APR) for your CD account (as a percentage): "))
     cd_maturity = int(input("Enter the number of months for which the interest is calculated: "))

<----- Then we call the functions for creating the accounts, passing in the user-provided inputs to perform the necessary calculations. This step is where interest is computed, and balances are updated. ------->


     updated_savings_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)
     updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)
        
<----- User is shown the results including the updated account balances and the interest earned, enhancing transparency and allowing them to verify the success of the process. ------>


     print(f"\nSavings Account Interest Earned: ${savings_interest_earned:.2f}")
     print(f"Updated Savings Account Balance: ${updated_savings_balance:.2f}")

     print(f"\nCD Account Interest Earned: ${cd_interest_earned:.2f}")
     print(f"Updated CD Account Balance: ${updated_cd_balance:.2f}")

<------ Finally, the main method is used to execute the process when the script is run, ensuring the program doesn't execute unintendedly unless it is explicitly invoked as the main module. -------->


     if __name__ == "__main__":
            main()

<---- This checks if the script is run as the main module (i.e., not imported as a library in another module), ensuring the execution flow starts only when desired. ----->









## Challenges
This project presented an interesting new challenge in regards to importing functions from separate files to be used in the main file for the calculations based on the data inputed by the customer. I got the hang of it thanks to W3 and Chat, but it was definitely new. I then messed up at the beginning with the calculation formulas for interest, I didn't realize they were provided in the Module Challenge section under "hints" so I was experiencing miscalculations when I tried to check the data being produced with google. 



## Learning Points 
I've said it before, and I'll say it again, Google google google, some more google, w3 Schools, and ChatGPT. Best... Friends... For Life....


## Author Info
Armand Araujo
Age: 29
Location: Las Vegas, NV

 
* [LinkedIn](https://www.linkedin.com/in/armand-araujo-a82ba2291/) 
* [Github](https://github.com/Armand57araujo) 


## Credits 

W3 Schools, chatgpt, MDN
