def read_unique_integers():
    try:
        numbers = list(map(int, input(
            "Enter integers separated by spaces: "
        ).split()))

        unique_numbers = []

        for num in numbers:
            if num not in unique_numbers:
                unique_numbers.append(num)

        print("Unique numbers:", unique_numbers)

    except ValueError:
        print("Error: Input must contain integers.")

read_unique_integers()
