# Notes Management System

FILE_NAME = "notes.txt"

def add_note():
    note = input("Enter your note: ")

    with open(FILE_NAME, "a") as file:
        file.write(note + "\n")

    print("Note saved successfully!\n")


def view_notes():
    try:
        with open(FILE_NAME, "r") as file:
            notes = file.read()

        if notes:
            print("\n--- Your Notes ---")
            print(notes)
        else:
            print("No notes found.")

    except FileNotFoundError:
        print("No notes file exists yet.")


def main():
    while True:
        print("\n===== Notes Manager =====")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")


main()