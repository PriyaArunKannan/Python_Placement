**#📘 Placement Eligibility & Student Performance Dashboard**
A fully interactive Streamlit-based application designed for EdTech platforms to manage and track student placement readiness using real-time filters, SQL analytics, and object-oriented programming principles.

✅ Project Overview
This project helps placement teams and training coordinators:

Filter students based on dynamic eligibility criteria.

Visualize performance in programming and soft skills.

Track placement readiness across batches and graduation years.

Gain data-driven insights using SQL and dashboards.

**🧠 Concepts Used**
🧱 1. Object-Oriented Programming (OOP) in Python
Created a DBManager class to handle all database operations.

Promotes code reuse, modularity, and scalability.

🧪 2. Streamlit for Dashboard UI
Used st.sidebar, st.selectbox, st.slider, st.dataframe for interactivity.

Sidebar filters dynamically control the student eligibility queries.

Insights are selected via dropdown and rendered in real time.

🗃️ 3. Relational Databases (SQLite)
Four normalized tables: Students, Programming, SoftSkills, and Placements.

Relationships managed using student_id as a foreign key.

🧪 4. Faker Library for Data Generation
Automatically populates realistic student data.

Simulates enrollments, performance, and placement outcomes.

📊 5. SQL for Data Analytics
Over 10 insights using aggregate functions (AVG, COUNT, GROUP BY).

SQL joins used to relate tables and extract insights.

Queries include filters for placement status, internship count, and batch analysis.

📈 6. Interactive Data Filtering
Filters on:

Problems Solved

Mock Interview Score

Assessments Completed

Average Soft Skill Score

Placement Status

Course Batch & Graduation Year

🔍 Key Features
Feature	Description
🎯 Eligibility Filtering	Sidebar controls filter eligible students based on multiple metrics
📈 Analytics Dashboard	Dropdown-based insight viewer using 10 prebuilt SQL queries
🧑‍💻 OOP Database Manager	All DB interactions handled through a reusable class
🧪 Faker Integration	Generates realistic synthetic data for demonstration
🔧 Clean UI/UX	Responsive layout using st.columns and st.sidebar

📊 SQL Insights Available
Average Programming Score per Batch

Top 5 Students by Project Score

Students with High Soft Skills (Avg > 85)

Students Ready for Placement

Students Placed and Their Packages

Internship Experience Distribution

Top 5 Students by Mock Interview Score

Top 5 by Leadership Skills

Most Certified Students (Top 5)

Interview Rounds Cleared (Top 5)

🛠️ Tech Stack
Frontend: Streamlit

Backend: Python 3 (OOP)

Database: SQLite

Data Generator: Faker

Data Processing: Pandas

Query Language: SQL (SQLite syntax)

🚀 How to Run Locally
bash
Copy
Edit
# Step 1: Install required packages
pip install -r requirements.txt

# Step 2: Launch the application
streamlit run main.py
⚠️ Make sure your database.py, main.py, and generated SQLite database are in the same directory.

📁 Project Structure
text
Copy
Edit
📦 placement_eligibility_app/
├── main.py                # Streamlit app code
├── database.py            # DBManager class (OOP-based)
├── generate_data.py       # Creates synthetic data using Faker
├── requirements.txt       # Required libraries
└── README.md              # Project overview and guide
