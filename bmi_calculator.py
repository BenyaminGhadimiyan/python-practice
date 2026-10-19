"""BMI calculator: weight in kg, height in meters."""


def read_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
        except ValueError:
            pass
        print("Please enter a number greater than 0.")


def get_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    return "Obese"


def main():
    weight = read_positive_number("Enter your weight (kg): ")
    height = read_positive_number("Enter your height (m, e.g. 1.75): ")

    bmi = weight / (height ** 2)
    print(f"BMI: {bmi:.1f}")
    print("Category:", get_category(bmi))


if __name__ == "__main__":
    main()
