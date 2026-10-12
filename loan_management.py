# loan_management.py
# Library Management System - Loan Management Module

loans = []
loan_id = 1


def issue_loan():
    global loan_id

    book_name = input("Enter book name: ")
    student_name = input("Enter student name: ")

    loan = {
        "loan_id": loan_id,
        "book_name": book_name,
        "student_name": student_name,
        "status": "Issued"
    }

    loans.append(loan)

    print("Book loan issued successfully!")
    print("Loan ID:", loan_id)

    loan_id = loan_id + 1


def return_loan():
    loan_number = int(input("Enter loan ID to return: "))

    for loan in loans:
        if loan["loan_id"] == loan_number:
            if loan["status"] == "Issued":
                loan["status"] = "Returned"
                print("Book returned successfully!")
            else:
                print("This book has already been returned.")
            return

    print("Loan ID not found.")


def view_loans():
    if len(loans) == 0:
        print("No loan records found.")
        return

    print("\nLoan Records")
    print("-" * 50)

    for loan in loans:
        print("Loan ID:", loan["loan_id"])
        print("Book Name:", loan["book_name"])
        print("Student Name:", loan["student_name"])
        print("Status:", loan["status"])
        print("-" * 50)


def main():
    while True:
        print("\n--- Loan Management System ---")
        print("1. Issue Loan")
        print("2. Return Loan")
        print("3. View Loans")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            issue_loan()
        elif choice == "2":
            return_loan()
        elif choice == "3":
            view_loans()
        elif choice == "4":
            print("Exiting Loan Management System.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()