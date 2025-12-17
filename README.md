# Enterprise Data Pipeline & Analytics Dashboard

This project implements a modular **ETL (Extract–Transform–Load) pipeline** in Python to simulate a real-world enterprise data workflow.  
It ingests data from multiple sources (CSV, REST API, and simulated streaming), cleans & transforms it, and loads it into a **PostgreSQL** database.  
The data can then be visualized in **PowerBI** or **Streamlit** dashboards for business insights.

---

## 🚀 Features
- Ingest data from:
    - CSV files (e.g., sales data)
    - REST APIs (Fake Store API)
    - Simulated streaming transactions
- Data cleaning & transformation with **Pandas**
- Relational storage in **PostgreSQL**
- Modular design with separate `ingest`, `transform`, `load` steps
- Configurable database connection via `config.py`
- Ready for orchestration (can be extended with **Apache Airflow**)

---

## 📂 Project Structure
etl_project/
│── src/
│ └── etl/
│ ├── init.py
│ ├── config.py
│ ├── ingest.py
│ ├── transform.py
│ ├── load.py
│ └── pipeline.py
│
│── data/
│ └── sales.csv # sample CSV data
│
│── requirements.txt # dependencies
│── README.md # documentation



---

##  Tech Stack
- **Python** (Pandas, Requests, Faker)
- **PostgreSQL**
- **PowerBI** / **Streamlit** (for dashboards)
- **pgAdmin** (for DB management)

---

##  Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/etl_project.git
cd etl_project

### 2. Install dependencies

Create a virtual environment and install required packages:

python -m venv venv
venv\Scripts\activate      # on Windows
source venv/bin/activate   # on Linux/Mac

pip install -r requirements.txt

3. Setup PostgreSQL
Option A: Install Locally

Install PostgreSQL from official site
.

Create user & database:

CREATE USER etl_user WITH PASSWORD 'etl_pass';
CREATE DATABASE etl_db OWNER etl_user;

Option B: Docker (if available)
docker compose up -d

▶️ Running the Pipeline

From project root, run:

python -m src.etl.pipeline



