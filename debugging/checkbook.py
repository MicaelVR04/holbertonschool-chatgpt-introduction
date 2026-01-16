#!/usr/bin/env python3

class Checkbook:
    def __init__(self):
        """
        Initializes a new Checkbook object.

        Parameters:
            None

        Returns:
            None
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Adds money to the checkbook balance.

        Parameters:
            amount (float): The amount of money to deposit.

        Returns:
            None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Removes money from the checkbook balance if funds are available.

        Parameters:
            amount (float): The amount of money to withdraw.

        Returns:
            None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Displays the current checkbook balance.

        Parameters:
            None

        Returns:
            None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Runs the main checkbook program loop.

    Parameters:
        None

    Returns:
        None
    """
    cb = Checkbook()

    while True:
        action = input(
            "What would you like to do? (deposit, withdraw, balance, exit): "
        ).lower()

        if action == 'exit':
            break

        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")

        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")

        elif action == 'balance':
            cb.get_balance()

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
