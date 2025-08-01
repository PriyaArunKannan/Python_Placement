# Placement Eligibility & Student Performance Dashboard
A fully interactive Streamlit-based application designed to manage and track student placement readiness using real-time filters, SQL analytics, and object-oriented programming principles.

# ✅ Project Overview

This project helps placement teams and training coordinators:

        1. Filter students based on dynamic eligibility criteria.
        2. Visualize performance in programming and soft skills.
        3. Track placement readiness across batches and graduation years.
        4. Gain data-driven insights using SQL and dashboards.

# 🧠 Concepts Used

**🧱 1. Object-Oriented Programming (OOP) in Python**

        1. Created a DBManager class to handle all database operations.
        2. Promotes code reuse, modularity, and scalability.

**🧪 2. Streamlit for Dashboard UI**

        1.Used st.sidebar, st.selectbox, st.slider, st.dataframe for interactivity.
        2.Sidebar filters dynamically control the student eligibility queries.
        3.Insights are selected via dropdown and rendered in real time.

**🗃️ 3. Relational Databases (SQLite)**

        1.Four normalized tables: Students, Programming, SoftSkills, and Placements.
        2.Relationships managed using student_id as a foreign key.

**🧪 4. Faker Library for Data Generation**

        1.Automatically populates realistic student data.
        2.Simulates enrollments, performance, and placement outcomes.

**📊 5. SQL for Data Analytics**

        1.Over 10 insights using aggregate functions (AVG, COUNT, GROUP BY).
        2.SQL joins used to relate tables and extract insights.
        3.Queries include filters for placement status, internship count, and batch analysis.

**📈 6. Interactive Data Filtering**

        Filters on:
                - Problems Solved
                - Mock Interview Score
                - Assessments Completed
                - Average Soft Skill Score
                - Placement Status
                - Course Batch & Graduation Year

**🔍 Key Features**        

                🎯 Eligibility Filtering - Sidebar controls filter eligible students based on multiple metrics
                📈 Analytics Dashboard - Dropdown-based insight viewer using 10 prebuilt SQL queries
                🧑‍💻 OOP Database Manager	- All DB interactions handled through a reusable class
                🧪 Faker Integration - Generates realistic synthetic data for demonstration
                🔧 Clean UI/UX	- Responsive layout using st.columns and st.sidebar

**📊 SQL Insights Available**

        1.Average Programming Score per Batch
        2.Top 5 Students by Project Score
        3.Students with High Soft Skills (Avg > 85)
        4.Students Ready for Placement
        5.Students Placed and Their Packages
        6.Internship Experience Distribution
        7.Top 5 Students by Mock Interview Score
        8.Top 5 by Leadership Skills
        9.Most Certified Students (Top 5)
        10.Interview Rounds Cleared (Top 5)

# 🛠️ Tech Stack

        Frontend: Streamlit
        Backend: Python 3 (OOP)        
        Database: SQLite        
        Data Generator: Faker        
        Data Processing: Pandas        
        Query Language: SQL (SQLite syntax)

# 🧪 Environment Setup
🔹 **Step 1: Create a Virtual Environment (Recommended)**
 Using venv (built-in Python module):

                        python -m venv myenv
                        
 This creates a folder named myenv/ containing your virtual environment.

🔹 **Step 2: Activate the Virtual Environment**

                ✅ On Windows:

                        myenv\Scripts\activate
                
                ✅ On macOS/Linux:
                
                        source myenv/bin/activate
                        
                Once activated, your terminal prompt will change, indicating you're inside the virtual environment.

                
# 🚀 How to Run Locally

**Step 1: Install required packages**

        pip install streamlit faker sqlite3 pandas

**Step 2: Run the Data generation**

       python src/data_generator.py

**Step 2: Launch the application**

        streamlit run main.py

