import sqlite3
import pandas as pd

class DBManager:
    def __init__(self, db_path='data/students.db'):
        self.conn = sqlite3.connect(db_path)
        self.cur = self.conn.cursor()
    
    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cur = self.conn.cursor()

    def close(self):
        self.conn.commit()
        self.conn.close()
    
    def get_eligible_students2(
        self,
        min_problems=50,
        min_soft_skills=75,
        min_mock_score=60,
        min_assessment=1,
        placement_status="Any",
        batch_filter="All",
        grad_year="All"
    ):
        query = """
        SELECT s.student_id as ID, s.name as Name, s.course_batch as Batch, s.graduation_year as Year,
            p.problems_solved as 'Problem Solved', p.assessments_completed as 'Assessment Completed',
            ROUND((ss.communication + ss.teamwork + ss.presentation + ss.leadership + ss.critical_thinking + ss.interpersonal_skills) / 6.0, 2) AS avg_soft_skills,
            pl.mock_interview_score as 'Mock Score', pl.placement_status as 'Status'
        FROM Students s
        JOIN Programming p ON s.student_id = p.student_id
        JOIN SoftSkills ss ON s.student_id = ss.student_id
        JOIN Placements pl ON s.student_id = pl.student_id
        WHERE p.problems_solved >= ?
        AND avg_soft_skills >= ?
        AND pl.mock_interview_score >= ?
        AND p.assessments_completed >= ?
        """

        # Dynamic filters
        params = [min_problems,  min_soft_skills, min_mock_score, min_assessment]

        if placement_status != "Any":
            query += " AND pl.placement_status = ?"
            params.append(placement_status)

        if batch_filter != "All":
            query += " AND s.course_batch = ?"
            params.append(batch_filter)

        if grad_year != "All":
            query += " AND s.graduation_year = ?"
            params.append(grad_year)

        query += " ORDER BY pl.mock_interview_score DESC"

        return pd.read_sql_query(query, self.conn, params=params)

    def execute_query(self, query):
        return pd.read_sql(query, self.conn)
    
    def get_insights(self):
        queries = {
            "1. Average Programming Score per Batch": """
                SELECT course_batch, AVG(problems_solved) as avg_problems
                FROM Students s
                JOIN Programming p ON s.student_id = p.student_id
                GROUP BY course_batch
            """,
            "2. Top 5 Students by Project Score": """
                SELECT s.name, p.latest_project_score
                FROM Students s
                JOIN Programming p ON s.student_id = p.student_id
                ORDER BY p.latest_project_score DESC LIMIT 5
            """,
            "3. Students with High Soft Skills (Avg > 85)": """
                SELECT s.name,
                    ROUND((ss.communication + ss.teamwork + ss.presentation + ss.leadership + ss.critical_thinking + ss.interpersonal_skills) / 6.0, 2) AS avg_soft_skills
                    FROM Students s
                    JOIN SoftSkills ss ON s.student_id = ss.student_id
                    WHERE (ss.communication + ss.teamwork + ss.presentation + ss.leadership + ss.critical_thinking + ss.interpersonal_skills) / 6.0 > 85
                    ORDER BY avg_soft_skills DESC
            """,
            "4. Students Ready for Placement": """
                SELECT name, placement_status
                FROM Students s
                JOIN Placements p ON s.student_id = p.student_id
                WHERE placement_status = 'Ready'
            """,
            "5. Students Placed": """
                SELECT name, company_name, placement_package
                FROM Students s
                JOIN Placements p ON s.student_id = p.student_id
                WHERE placement_status = 'Placed'
            """,
            "6. Internship Experience Distribution": """
                SELECT internships_completed, COUNT(*) as student_count
                FROM Placements
                GROUP BY internships_completed
            """,
            # 🔁 Replaced: Average Mock Interview Score
            "7. Top 5 Students by Mock Interview Score": """
                SELECT s.name, p.mock_interview_score
                FROM Students s
                JOIN Placements p ON s.student_id = p.student_id
                ORDER BY p.mock_interview_score DESC LIMIT 5
            """,
            "8. Leadership Skill Top 5": """
                SELECT s.name, ss.leadership
                FROM Students s
                JOIN SoftSkills ss ON s.student_id = ss.student_id
                ORDER BY ss.leadership DESC LIMIT 5
            """,
            # 🔁 Replaced: Certification Distribution
            "9. Most Certified Students (Top 5)": """
                SELECT s.name, p.certifications_earned
                FROM Students s
                JOIN Programming p ON s.student_id = p.student_id
                ORDER BY p.certifications_earned DESC LIMIT 5
            """,
            "10. Interview Rounds Cleared (Top 5)": """
                SELECT s.name, pl.interview_rounds_cleared
                FROM Students s
                JOIN Placements pl ON s.student_id = pl.student_id
                ORDER BY pl.interview_rounds_cleared DESC LIMIT 5
            """
        }

        return queries
    
    def run_query(self, query: str):
        """Executes and returns result of SQL query as DataFrame."""
        import pandas as pd
        return pd.read_sql_query(query, self.conn)
    
    def get_all_batches(self):
        query = "SELECT DISTINCT course_batch FROM Students ORDER BY course_batch"
        result = pd.read_sql_query(query, self.conn)
        return result['course_batch'].tolist()
    
    def get_all_graduation_years(self):
        query = "SELECT DISTINCT graduation_year FROM Students ORDER BY graduation_year"
        result = pd.read_sql_query(query, self.conn)
        return result['graduation_year'].tolist()