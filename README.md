
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
