## 📑 Table of Contents

1. [Project Overview](#postgresql--python-mini-data-engineering-projects)
2. [Project Highlights](#-project-highlights)
   1. [Class Roster Database](#1-class-roster-database)
   2. [Real Estate Data Analysis](#2-real-estate-data-analysis)
3. [Tech Stack](#-tech-stack)
4. [Repository Structure](#-repository-structure)
5. [Getting Started](#-getting-started)
   1. [Install Dependencies](#1-install-dependencies)
   2. [Configure Environment Variables](#2-configure-environment-variables)
   3. [Run a Project](#3-run-a-project)
6. [Learning Path Demonstrated](#-learning-path-demonstrated)
7. [Next Steps & Extensions](#-next-steps--extensions)
8. [Contributing](#-contributing)


# PostgreSQL & Python Mini Data Engineering Projects

A showcase of **end-to-end data workflows** using Python (`psycopg2`) and PostgreSQL. From foundational database operations to advanced CSV ingestion, transformation, and business intelligence queries.

This repository contains **two learning-to-production style projects**:

> **Note:** The CSV dataset used in this project is stored in the `data/` folder.

1. **Class Roster Database** – [link-here](https://github.com/victorcezeh/understanding-psycopg2/tree/main/class-roster-database) A beginner-friendly system for storing and retrieving student data, demonstrating a clear progression from procedural scripts to object-oriented design and an interactive CLI.
2. **Real Estate Data Analysis** – [link-here](https://github.com/victorcezeh/understanding-psycopg2/tree/main/real-estate-data-analysis) An advanced ETL pipeline for importing real estate data from CSV, handling complex data types, and running market analysis queries.

---

## 📌 Project Highlights

### 1. Class Roster Database

* **Progressive Design**: Procedural → OOP → User Interface
* **Secure Queries**: Parameterized SQL to prevent injection
* **Environment Config**: Credentials via `.env` file
* **Error Handling**: psycopg2 exception management & cleanup
* **User Interaction**: Command-line interface for live queries

**Core Skills:** Basic schema design, CRUD operations, connection management, and interactive database applications.

---

### 2. Real Estate Data Analysis

* **CSV → Database Pipeline**: Automated ETL process
* **Data Type Mastery**: Integers, decimals, timestamps with timezones
* **Transformation Layer**: Clean & map raw CSV fields before loading
* **Business Analytics**: Aggregate queries for market insights
* **Performance Aware**: Row-by-row processing with single-transaction commit

**Core Skills:** ETL design, data type conversion, bulk inserts, aggregate analytics, and schema planning for production-like scenarios.

---

## 🤖 Tech Stack

* **Language**: Python 3.x
* **Database**: PostgreSQL
* **Libraries**:

  * `psycopg2-binary` – PostgreSQL connector
  * `python-dotenv` – Environment variable management
  * `python-dateutil` – Advanced date/time parsing (Real Estate project)

---

## 📂 Repository Structure

```
understanding-psycopg2/
├── data/
│   └── data.csv
├── my_env/                   # Virtual environment (ignored in .gitignore)
├── psycopg2-csv-demo/
│   ├── property_analysis.py
│   ├── README.md
│   └── real_estate_import.py
├── psycopg2-demo/
│   ├── __pycache__/           # Python run cache (ignored)
│   ├── class_roster_basic.py
│   ├── db.py
│   ├── README.md
│   └── terminal.py
├── .env                      # Local environment variables (ignored)
├── .env.example              # Template for env configuration
├── .gitignore
├── README.md                 # This combined project README
└── requirements.txt

```

---

## 🚀 Getting Started

### 1. Install Dependencies

```bash
pip install psycopg2-binary python-dotenv python-dateutil
```

### 2. Configure Environment Variables

Create a `.env` file in the root directory based on the template below.

**.env.example**

```env
# ==== Class Roster Database Credentials ====
CLASS_ROASTER_DBNAME=class_roaster
CLASS_ROASTER_HOST=localhost
CLASS_ROASTER_USER=your_username
CLASS_ROASTER_PASSWORD=your_password
CLASS_ROASTER_PORT=5432

# ==== Real Estate Database Credentials ====
REAL_ESTATE_DBNAME=real_estate
REAL_ESTATE_HOST=localhost
REAL_ESTATE_USER=your_username
REAL_ESTATE_PASSWORD=your_password
REAL_ESTATE_PORT=5432

# ==== CSV File Path for Real Estate Project ====
PATH_TO_CSV=/path/to/your/data.csv
```

### 3. Run a Project

* **Class Roster (Procedural)**

  ```bash
  python class_roster_basic.py
  ```
* **Class Roster (Interactive CLI)**

  ```bash
  python terminal.py
  ```
* **Real Estate (ETL Pipeline)**

  ```bash
  python real_estate_import.py
  ```
* **Real Estate (Analytics)**

  ```bash
  python property_analysis.py
  ```

---

## 📖 Learning Path Demonstrated

1. **Database Fundamentals** – Procedural scripting, manual resource control
2. **OOP Abstraction** – Encapsulating DB logic in reusable classes
3. **ETL Pipelines** – Extract, transform, and load from CSV to PostgreSQL
4. **Analytics Layer** – Aggregations, grouping, and insights for decision-making

---

## 🔮 Next Steps & Extensions

* Add UPDATE/DELETE operations in Class Roster
* Integrate PostGIS for geospatial queries in Real Estate
* Create REST API endpoints for both datasets
* Visualize insights with matplotlib or Plotly
* Implement connection pooling for performance scaling

---

## 🤝 Contributing

This repository is intended as both a **learning resource** and a **launchpad** for production-level data workflows.
Feel free to fork, extend, or adapt these patterns for your own projects.

---
