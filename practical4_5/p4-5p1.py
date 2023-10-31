amount = input("Amount in USD: ")
if float(amount) <= 0:
    print("Amount must be >= 0. Please try again.")
else:
    exchange_rate = input("Rate: ")

    print("Amount in EU: ", float(amount) * float(exchange_rate))