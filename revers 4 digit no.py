def reverse_number(number):
    number_str = str(number)
    reversed_number_str = number_str[::-1]
    reversed_number = int(reversed_number_str)
    return reversed_number

def main():
    number = int(input("Enter a four-digit number: "))
    if number < 1000 or number > 9999:
        print("Invalid input! Please enter a four-digit number.")
        return
    reversed_number = reverse_number(number)
    if reversed_number == number:
        print("The number is a palindrome.")
    else:
        print("The reverse of the number is:", reversed_number)

if __name__ == "__main__":
    main()
