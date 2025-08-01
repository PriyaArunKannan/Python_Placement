# 🎓 Placement Eligibility & Performance Dashboard

A data-driven **Streamlit application** designed for educational institutions and placement cells to:

- **Filter and shortlist students** based on customizable placement criteria
- **Track student performance** across programming, soft skills, and placement metrics
- **Visualize insights** through an interactive dashboard

---

## 📌 Features

### 🏢 Placement Management
- Filter students by:
  - Programming problems solved
  - Soft skills score
  - Mock interview performance
  - Assessment completed
  - Placement status
  - Batch and Year
- View and export eligible candidates for a job profile

### 📊 Student Performance Tracking
- Analyze student readiness across:
  - Assessment scores
  - Soft skills average
  - Mock interview results
- Filter by batch and graduation year

## 📊 Insights Available

The dashboard includes the following SQL-powered insights:

1. **Average Programming Score per Batch**  
2. **Top 5 Students by Project Score**  
3. **Students with High Soft Skills (Avg > 85)**  
4. **Students Ready for Placement**  
5. **Students Placed and Their Packages**  
6. **Internship Experience Distribution**  
7. **Top 5 Students by Mock Interview Score**  
8. **Top 5 by Leadership Skills**  
9. **Most Certified Students (Top 5)**  
10. **Interview Rounds Cleared (Top 5)**  
---

## 🧱 Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend**: Python, SQLite
- **Data Generation**: Faker
- **Database Interaction**: SQL + Pandas
- **Programming Style**: Object-Oriented Programming (OOP)

---

## 🗃️ Folder Structure

placement/
├── main.py                  # Entry point for Streamlit app
├── src/data_manager.py      # Database interaction using OOP
├── src/data_generator.py    # Generate synthetic data using Faker
└── data/students.db         # Database