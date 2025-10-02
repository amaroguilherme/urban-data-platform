# Urban Data Platform

This project implements a data backbone for a **simulation** of a city, a continuously updated virtual replica of real-world urban systems. It ingests, processes, and transforms mobility, energy, environmental, and citizen interaction data, enabling city planners to simulate and predict scenarios such as traffic rerouting, energy load balancing, or pollution control.

---

## 🔹 Data Sources

The system integrates multiple types of data (all synthetic):

### IoT & Sensor Networks
- **Smart meters:** Energy usage.
- **Air quality sensors:** CO₂, PM2.5, NO₂.
- **Noise sensors.**
- **Smart parking sensors.**

### Mobility Systems
- Bike-share trips.
- EV charging station logs.
- Ride-hailing platform data.

### Infrastructure Telemetry
- Building energy efficiency reports.
- Water usage logs.

### External Data
- Weather forecasts.

---

## 🔹 Workflow Architecture

### 1. Raw Ingestion
- **Tool:** Airflow → BigQuery
- **Details:** All raw data lands in BigQuery for centralized storage.

### 2. Transformations
- **Tools:** dbt + BigQuery
- **Layers:**
  - **Staging:** Standardized schemas for energy, mobility, and environment datasets.

### 3. Orchestration
- **Tool:** Airflow
- **Function:** Schedules dbt transformations according to source data frequency.
  
---

## 🔹 Project Goals
- Enable city planners to simulate urban scenarios in near real-time.
- Provide actionable insights into traffic, energy, and environmental patterns.
- Support sustainability initiatives through measurable KPIs.
- Facilitate predictive analytics for urban management.

---

## 🔹 Getting Started

1. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Airflow**
   ```bash
   airflow standalone
   ```

4. Access the Airflow UI at `http://localhost:8080` to trigger DAGs.
