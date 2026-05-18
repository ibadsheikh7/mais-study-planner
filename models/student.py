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
        self.__password = password  # private = Encapsulation
        self.semester = semester

    # Getter (encapsulation)
    def get_password(self):
        return self.__password

    def save_to_db(self, db_path):
        try:
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute("INSERT INTO students (name, email, password, semester) VALUES (?, ?, ?, ?)",
                      (self.name, self.email, self.__password, self.semester))
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print("Error:", e)
            return False

    @staticmethod
    def login(db_path, email, password):
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute("SELECT id, name FROM students WHERE email=? AND password=?", (email, password))
        row = c.fetchone()
        conn.close()
        if row:
            return {"id": row[0], "name": row[1]}
        return None
