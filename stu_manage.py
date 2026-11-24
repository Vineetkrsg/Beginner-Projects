class Student:
    def __init__(self, name, course, year, roll_no):
        self.name = name
        self.course = course
        self.year = year
        self.roll_no = roll_no
        self.subjects = {}

    def menu(self):
        while True:
            print('''
            1. View Student Details
            2. Update Student Details
            3. Enter Subject and respective marks
            4. View Subject and respective marks
            5. Total and Average marks
            6. Update Subject Marks
            7. Delete Subject
            8. Highest Scoring Subject
            9. Exit''')

            choice = input("Enter your choice: ")

            if choice == '1':
                self.view_details()
            elif choice == '2':
                self.update_details()
            elif choice == '3':
                self.enter_subjects()
            elif choice == '4':
                self.view_subjects()
            elif choice == '5':
                self.total_average()
            elif choice == '6':
                self.update_subjects()
            elif choice == '7':
                self.delete_subject()
            elif choice == '8':
                self.highest_subject()
            elif choice == '9':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

    def view_details(self):
        print(f"Name: {self.name}")
        print(f"Course: {self.course}")
        print(f"Year: {self.year}")
        print(f"Roll No: {self.roll_no}")

    def update_details(self):
        self.name = input("Enter new name: ")
        self.course = input("Enter new course: ")
        self.year = input("Enter new year: ")
        print("Details updated successfully.")

    def enter_subjects(self):
        nof = int(input("Enter the no. of subjects: "))

        if nof <= 0:
            print("Please enter a positive number.")
            return

        for i in range(nof):
            subject = input("Enter the subject name: ")

            if subject in self.subjects:
                print("Subject already exists.")
                continue

            marks = float(input("Enter the marks: "))

            if marks < 0 or marks > 100:
                print("Marks must be between 0 and 100.")
                continue

            self.subjects[subject] = marks

        print("Subjects and marks entered successfully.")

    def view_subjects(self):
        if not self.subjects:
            print("No subjects entered yet.")
        else:
            for subject, marks in self.subjects.items():
                print(f"Subject: {subject}, Marks: {marks}")

    def total_average(self):
        if not self.subjects:
            print("No subjects entered yet.")
        else:
            total = sum(self.subjects.values())
            average = total / len(self.subjects)

            print(f"Total Marks: {total}")
            print(f"Average Marks: {average:.2f}")

    def update_subjects(self):
        if not self.subjects:
            print("No subjects available to update.")
            return

        subject = input("Enter the subject name you want to update: ")

        if subject in self.subjects:
            marks = float(input("Enter the new marks: "))

            if marks < 0 or marks > 100:
                print("Marks must be between 0 and 100.")
            else:
                self.subjects[subject] = marks
                print("Marks updated successfully.")
        else:
            print("Subject not found.")

    def delete_subject(self):
        if not self.subjects:
            print("No subjects available to delete.")
            return

        subject = input("Enter the subject name you want to delete: ")

        if subject in self.subjects:
            del self.subjects[subject]
            print("Subject deleted successfully.")
        else:
            print("Subject not found.")

    def highest_subject(self):
        if not self.subjects:
            print("No subjects entered yet.")
        else:
            subject = max(self.subjects, key=self.subjects.get)
            marks = self.subjects[subject]

            print(f"Highest Scoring Subject: {subject}")
            print(f"Marks: {marks}")


student1 = Student("Alex", "Computer Science", 1, 101)
student1.menu()
