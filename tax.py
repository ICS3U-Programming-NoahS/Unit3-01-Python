#!/usr/bin/env python3

# Created by: Noah Smith
# Created on: Oct. 10th, 2023
# This program asks the user for the subtotal ($). It then calculates and displays
# the total and the tax.
import constants


def main():
    # Get the subtotal
    subtotal = float(input("Enter the subtotal ($): "))

    # Calculate the tax and total
    tax = constants.HST * subtotal
    total = subtotal + tax

    # Display the total and the tax back to the user
    print("")
    print("The total is = ${:.2f}".format(total))
    print("The tax is = ${:.2f}".format(tax))


if __name__ == "__main__":
    main()
