"""Read 5 students' grades, compute the class average, save to a file."""

STUDENT_COUNT = 5
OUTPUT_FILE = "students.txt"


def calculate_average(students):
    return sum(students.values()) / len(students)


def save_to_file(students, filename=OUTPUT_FILE):
    with open(filename, "w", encoding="utf-8") as file:
        for name, score in students.items():
            file.write(f"{name} : {score}\n")


def read_name(prompt, students):
    """Keep asking until the name is not empty and not already used."""
    while True:
        name = input(prompt).strip()
        if not name:
            print("Error! The name cannot be empty.")
        elif name in students:
            print("Error! This name has already been entered.")
        else:
            return name


def read_score():
    """Keep asking until the score is a number between 0 and 20."""
    while True:
        try:
            score = float(input("Grade: "))
            if 0 <= score <= 20:
                return score
        except ValueError:
            pass
        print("Error! The grade must be a number between 0 and 20.")


def main():
    students = {}
    for i in range(1, STUDENT_COUNT + 1):
        name = read_name(f"Student {i} name: ", students)
        students[name] = read_score()

    average = calculate_average(students)
    save_to_file(students)

    print("Students:")
    for name, score in students.items():
        print(f"  {name} : {score}")
    print("Class average:", round(average, 2))


if __name__ == "__main__":
    main()
