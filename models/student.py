 # Student class - shows OOP: Class, Object, Constructor, Encapsulation

import sqlite3


class Person:
    """Base class - shows Inheritance (parent class)."""

    def __init__(self, name, email):
        # Constructor
        self.name = name
        self.email = email

    def show_info(self):
        return f"Name: {self.name}, Email: {self.email}"


class Student(Person):
    """Student inherits from Person - Single Inheritance."""

    def __init__(self, name, email, password, semester):
        # Calling parent constructor
        super().__init__(name, email)

        # Private variable = Encapsulation
        self.__password = password
        self.semester = semester

    # Getter method
    def get_password(self):
        return self.__password

    # Save student in database
    def save_to_db(self, db_path):

        conn = sqlite3.connect(db_path)
        c = conn.cursor()

        try:
            c.execute(
                "INSERT INTO students (name, email, password, semester) VALUES (?, ?, ?, ?)",
                (self.name, self.email, self.__password, self.semester)
            )

            conn.commit()
            return True

        except Exception as e:
            print("Database Error:", e)
            return False

        finally:
            conn.close()

    # Login method
    @staticmethod
    def login(db_path, email, password):

        conn = sqlite3.connect(db_path)
        c = conn.cursor()

        c.execute(
            "SELECT id, name, email FROM students WHERE email=? AND password=?",
            (email, password)
        )

        row = c.fetchone()

        conn.close()

        if row:
            return {
                "id": row[0],
                "name": row[1],
                "email": row[2]
            }

        return None