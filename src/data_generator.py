from faker import Faker
import random
import sqlite3

fake = Faker()

class DataGenerator:
    def __init__(self, db_name="data/students.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    # Creating tables - Students, Programming,SoftSkills and Placements
    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Students (
                student_id INTEGER PRIMARY KEY,
                name TEXT, age INTEGER, gender TEXT, email TEXT,
                phone TEXT, enrollment_year INTEGER, course_batch TEXT,
                city TEXT, graduation_year INTEGER
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Programming (
                programming_id INTEGER PRIMARY KEY,
                student_id INTEGER,
                language TEXT, problems_solved INTEGER,
                assessments_completed INTEGER, mini_projects INTEGER,
                certifications_earned INTEGER, latest_project_score INTEGER,
                FOREIGN KEY(student_id) REFERENCES Students(student_id)
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS SoftSkills (
                soft_skill_id INTEGER PRIMARY KEY,
                student_id INTEGER,
                communication INTEGER, teamwork INTEGER,
                presentation INTEGER, leadership INTEGER,
                critical_thinking INTEGER, interpersonal_skills INTEGER,
                FOREIGN KEY(student_id) REFERENCES Students(student_id)
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Placements (
                placement_id INTEGER PRIMARY KEY,
                student_id INTEGER,
                mock_interview_score INTEGER, internships_completed INTEGER,
                placement_status TEXT, company_name TEXT,
                placement_package REAL, interview_rounds_cleared INTEGER,
                placement_date TEXT,
                FOREIGN KEY(student_id) REFERENCES Students(student_id)
            )
        ''')
        self.conn.commit()

    # inserting the data to the tables using faker

    def generate_data(self, num_students=50):
        for _ in range(num_students):
            name = fake.name()
            age = random.randint(20, 40)
            gender = random.choice(["Male", "Female", "Other"])
            email = fake.email()
            phone = fake.phone_number()
            enrollment_year = random.randint(2018, 2025)
            course_batch = f"Batch-{random.randint(1,5)}"
            city = fake.city()
            graduation_year = enrollment_year + 1

            self.cursor.execute('''
                INSERT INTO Students (name, age, gender, email, phone, enrollment_year, course_batch, city, graduation_year)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (name, age, gender, email, phone, enrollment_year, course_batch, city, graduation_year))

            student_id = self.cursor.lastrowid

            # Programming data
            self.cursor.execute('''
                INSERT INTO Programming (student_id, language, problems_solved, assessments_completed, mini_projects, certifications_earned, latest_project_score)
                VALUES (?, "Python", ?, ?, ?, ?, ?)
            ''', (student_id, random.randint(10, 100), random.randint(1, 10), random.randint(0, 5), random.randint(0, 3), random.randint(50, 100)))

            # Soft Skills
            self.cursor.execute('''
                INSERT INTO SoftSkills (student_id, communication, teamwork, presentation, leadership, critical_thinking, interpersonal_skills)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (student_id, *[random.randint(50, 100) for _ in range(6)]))

            # Placements
            status = random.choice(["Ready", "Not Ready", "Placed"])
            company = fake.company() if status == "Placed" else None
            package = round(random.uniform(4, 20), 2) if status == "Placed" else None
            date = fake.date_this_year() if status == "Placed" else None
            self.cursor.execute('''
                INSERT INTO Placements (student_id, mock_interview_score, internships_completed, placement_status, company_name, placement_package, interview_rounds_cleared, placement_date)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (student_id, random.randint(40, 100), random.randint(0, 3), status, company, package, random.randint(0, 5), date))

        self.conn.commit()
        print(f"{num_students} students generated and inserted.")

if __name__ == "__main__":
    generator = DataGenerator()
    generator.create_tables()
    generator.generate_data(500)
