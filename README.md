
# 📋 Population Management App (SQLite - Local - 10M Citizens)

A lightweight population management system that runs locally using **SQLite** and **Streamlit**. It supports full **CRUD** (Create, Read, Update, Delete) operations on a dataset of **up to 10 million citizens**, generated using fake data.

---

## 🚀 Features

- ✅ Manage citizen data: `name`, `dob`, `sex`, `perID`
- ✅ Full CRUD: insert, update, delete, search
- ✅ Local-only: no server required
- ✅ Fast and efficient with SQLite indexing
- ✅ Streamlit UI + CLI interface
- ✅ Faker-based data generation (demo-friendly)
- ✅ Designed for scalability, runs with millions of records

---

## 🗂️ Project Structure

```
population_app/
│
├── main.py                  # Command-line interface (CLI)
├── database/
│   └── citizen.db           # SQLite database file (auto-created)
├── scripts/
│   └── generate_data.py     # Generate fake citizen data
├── services/
│   ├── db_handler.py        # Core DB operations (insert/update/delete/search)
│   └── logic.py             # (Optional) Business logic layer
├── utils/
│   └── common.py            # Helpers (UUID, validation)
├── streamlit_app.py         # UI built with Streamlit
├── environment.yaml         # Conda environment setup
└── project_overview.txt     # Plain-text project summary
```

---

## ⚙️ Setup Instructions

### 1. Create Conda Environment

```bash
conda env create -f environment.yaml
conda activate population_app
```

### 2. Generate Data (Demo Mode)

```bash
python scripts/generate_data.py  # Adjust NUM_RECORDS for demo (e.g., 10000)
```

> 💡 The database will be saved as `database/citizen.db`

---

## 💻 Run the Application

### ▶️ Option 1: CLI App

```bash
python main.py
```

### ▶️ Option 2: Streamlit UI

```bash
streamlit run streamlit_app.py
```

---

## 🛠️ Customization

- You can change the number of generated records in `generate_data.py`
- You can ignore pushing large databases by using `.gitignore`

---

## 🧪 Example Use Cases

- Offline population registry
- Government or local region citizen management demo
- Educational purposes (database, CRUD, UI)

---

## 📦 Demo DB (optional)

You can create a small demo DB (e.g., 10,000 rows) for GitHub testing:
```bash
# Inside generate_data.py, change:
NUM_RECORDS = 10000
```

---

## 📄 License

MIT License. Use freely with attribution.

---

## 🧱 Database Architecture

This project uses **SQLite** as the local embedded database engine.

- **Type**: Relational DBMS (file-based)
- **Structure**:
  - Table: `citizen(perID PRIMARY KEY, name, dob, sex)`
  - Indexes: created on `name` and `dob` for faster filtering
- **Storage**: All data is stored in a single file `citizen.db`
- **Performance**: Optimized for read-heavy operations with over 10 million records
- **ACID-compliant**: Supports transactions and rollback
- **Ideal for**: Local apps, personal projects, and demos (no server required)

> If scaling up for multiple concurrent users, consider upgrading to PostgreSQL or MySQL.

---

## 🔍 Search Algorithms & Strategies

### ✅ `perID` Lookup (Primary Key Search)
- Uses built-in B-Tree index on the `perID` column
- **Time complexity**: `O(log n)`
- **Query**:
  ```sql
  SELECT * FROM citizen WHERE perID = ?
  ```
- **Very fast**, even with 10M+ records

### ✅ `name` Search (LIKE Operator)
- Uses:
  ```sql
  SELECT * FROM citizen WHERE name LIKE '%keyword%' LIMIT 100;
  ```
- Partial matching using `LIKE '%text%'`
- **Time complexity**: `O(n)` if no leading match (SQLite can't optimize `%text%`)
- Index on `name` helps marginally but not for fuzzy matches

---

### 🔮 Future Search Enhancements (Optional)
To support more powerful search features:

| Feature         | Tool/Strategy            | Benefit                        |
|----------------|--------------------------|--------------------------------|
| Fuzzy search    | SQLite FTS5 / ElasticSearch | Typo-tolerant search          |
| Full-text search| SQLite virtual tables    | Faster and richer text queries|
| Autocomplete    | Trie or external engine  | UI-friendly suggestion        |
| Ranking results | ElasticSearch scoring    | Smart ordering of results     |

> For now, `LIKE` is sufficient for demos and small-scale testing. Full-text or fuzzy enhancements can be modularly added.


---

## ⚙️ Alternative Setup (Without Conda)

If you don't use Conda, you can still run this project using `pip` and Python virtual environments.

### 🔧 1. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 📥 2. Install Requirements

```bash
pip install -r requirements.txt
```

### ▶️ 3. Run the App

```bash
python scripts/generate_data.py        # Generate fake data
python main.py                         # Run CLI
streamlit run streamlit_app.py         # Run Streamlit UI
```

> Make sure Python 3.10+ is installed on your system.

---

