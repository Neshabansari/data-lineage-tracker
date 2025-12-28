#  Data Lineage and Provenance Tracker

A simple and effective **Data Lineage Tracking System** that records how data flows through an ETL pipeline and exposes lineage history through REST APIs.

This project demonstrates how to:
- Track data provenance
- Log each ETL transformation step
- Store lineage metadata in a database
- Query lineage using a REST API
- Deploy the service to the cloud

---

##  Live Deployment

The application is deployed on **Render** and is publicly accessible.

🔗 **Deployment Link**
```
https://data-lineage-tracker.onrender.com
```

---

##  How to Test the Application (IMPORTANT)

### Step 1: Open Swagger UI

Open the following URL in your browser:

```
https://data-lineage-tracker.onrender.com/docs
```

Swagger UI will open automatically.

---

### Step 2: Call the Lineage API

1. Expand the endpoint:
```
GET /lineage/{dataset_id}
```

2. Click **Try it out**

3. Enter **any one** of the following dataset IDs:

```
sales_v1
sales_v2
sales_v3
sales_final
```

4. Click **Execute**

---

### Step 3: View the Response

You will receive a JSON response containing:
- Source dataset
- Transformation operation
- Timestamp of execution

---

##  Example

### Request
```
GET /lineage/sales_final
```

### Response
```json
[
  {
    "source": "sales.csv",
    "operation": "Loaded raw data",
    "timestamp": "2025-12-28T10:57:51.808726"
  },
  {
    "source": "sales.csv",
    "operation": "Saved cleaned dataset",
    "timestamp": "2025-12-28T11:02:15.234112"
  }
]
```

---

## ⚙️ Project Architecture

```
data-lineage-tracker/
│
├── app/
│   ├── main.py          # FastAPI application
│   ├── database.py      # Database configuration
│   ├── models.py        # SQLAlchemy models
│
├── etl/
│   └── etl_script.py    # ETL pipeline with lineage logging
│
├── data/
│   ├── sales.csv
│   └── final_sales.csv
│
├── db/
│   └── lineage.db       # SQLite database
│
├── requirements.txt
└── README.md
```

---

##  ETL Pipeline Flow

1. **Extract**
   - Load raw data from `sales.csv`
   - Log lineage as `sales_v1`

2. **Transform**
   - Remove null values
   - Log lineage as `sales_v2`

3. **Transform**
   - Filter records for year = 2024
   - Log lineage as `sales_v3`

4. **Load**
   - Save cleaned data as `final_sales.csv`
   - Log lineage as `sales_final`

Each ETL step records:
- Dataset ID
- Source file
- Operation performed
- Timestamp

---

##  Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pandas
- Render (Cloud Deployment)

---

##  Key Features

- Tracks complete data lineage across ETL steps
- Stores historical lineage (multiple ETL runs)
- REST API for lineage queries
- Swagger UI for easy testing
- Lightweight and easy to deploy

---

##  Notes for Evaluators

- The application exposes a REST API to query lineage
- Lineage can be tested directly via Swagger UI
- No authentication is required
- The database is pre-populated using an ETL script

---

## 👤 Author

**Neshab Alam Ansari**

---

