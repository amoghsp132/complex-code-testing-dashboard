# Complex Code Testing Dashboard (Python Edition)

**Institution:** S D M College of Engineering & Technology, Dharwad (SDMCET)  
**Department:** Department of Computer Science & Engineering  
**Course:** Software Testing (22UCSES731) - VII Semester  
**Student Name:** Amogh S Patil  
**USN:** 2SDS23CS011  
**Academic Year:** 2026-27  

---

## 🚀 Overview

The **Complex Code Testing Dashboard** is a full-stack automated software testing and quality analysis web application developed completely in **Python** (Flask framework) designed for seamless cloud deployment on **Render**.

It supersedes traditional multi-tool Java setups (JUnit, JaCoCo, PMD, SpotBugs, Checkstyle) by integrating the leading industry-standard Python equivalents into a unified 25-criteria test matrix:

| Tool Category | Legacy Java Tool | Python Testing Equivalent | Test Objectives Covered |
| :--- | :--- | :--- | :--- |
| **Automated Unit Testing** | JUnit 5 | **PyTest / Unittest** | Dynamic compilation, object instantiation, boundary values, exception recovery, and contract assertion (5 Test Cases). |
| **Code Coverage Analysis** | JaCoCo | **Coverage.py** | Statement coverage threshold (>= 75%), branch logic, function coverage ratio, dead/unreachable code detection (5 Test Cases). |
| **Static Code Analysis** | PMD | **Flake8 / Pylint** | Unused variables, wildcard namespace pollution, variable shadowing, nesting depth, clean code smell audit (5 Test Cases). |
| **Bug Pattern & Security** | SpotBugs | **Bandit Security** | Dangerous execution (`eval`/`exec`), weak cryptographic hashes (`MD5`), hardcoded secrets/API keys, resource leakage, shell injection (5 Test Cases). |
| **Coding Standards** | Checkstyle | **PEP 8 / Pycodestyle** | 4-space indentation, line length limits (<= 88 chars), identifier naming conventions, import ordering, whitespace hygiene (5 Test Cases). |
| **Defect Prediction** | Code Metrics | **McCabe Cyclomatic Engine** | Direct implementation of Slide 1.9 & Slide 1 requirement: Computes cyclomatic complexity $v(G)$, SLOC, Maintainability Index (MI), and forecasts high-risk defect probability. |

---

## 📦 Features

- **25 Comprehensive Automated Test Cases:** 5 test cases per tool providing instant PASS / WARNING / FAILED diagnostics.
- **One-Click Preloaded Complex Programs:** Test Calculator, Banking Ledger, E-Commerce Cart, and Vulnerable Code antipatterns.
- **Interactive Visualizations:** Chart.js Radar Chart comparing tool health, Doughnut Chart of pass/fail ratios, and metric gauges.
- **Defect Prediction Rationale:** Analyzes branch count and code volume to warn developers of high-risk modules before production deployment.
- **Zero-Setup Cloud Ready:** Pre-configured with `Procfile`, `runtime.txt`, `render.yaml`, and `requirements.txt` for 1-click Render hosting.

---

## 🛠️ Local Installation & Execution

### Prerequisites
- Python 3.10+ installed.

### Steps
1. Navigate to the project directory:
   ```bash
   cd Project_1_Complex_Code_Testing_Dashboard
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask application:
   ```bash
   python app.py
   ```
5. Open your web browser and visit:
   ```
   http://127.0.0.1:5000
   ```

---

## 🌐 Cloud Deployment on Render

This application is configured for deployment on [Render](https://render.com):
1. Push this project folder to a GitHub repository.
2. Sign in to your Render dashboard and click **New + > Web Service**.
3. Select your repository.
4. Render will automatically detect the Python environment:
   - **Environment:** `Python`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
5. Click **Create Web Service**. Your live dashboard URL will be available in minutes!
