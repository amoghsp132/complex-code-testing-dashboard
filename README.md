# TestPulse — Complex Code Testing Dashboard (Python Edition)

**System Name:** TestPulse  
**Category:** Automated Multi-Tool Software Testing & Code Quality Platform  
**Academic Module:** Software Testing (VII Semester)  

---

## 🚀 Overview

**TestPulse** is an enterprise-grade automated software testing and quality analysis web application developed completely in **Python (Flask)** with a modern **Google Material Design** web interface.

It replaces heavyweight legacy multi-tool setups with native, high-performance Python equivalents across a standardized 25-criteria test matrix:

| Testing Dimension | Legacy Java Tool | Python Testing Equivalent | Verification Objectives Covered |
| :--- | :--- | :--- | :--- |
| **Automated Dynamic Testing** | JUnit 5 | **PyTest / Unittest** | Dynamic compilation, object instantiation, callable probing, boundary conditions, exception handling, and contract assertion (5 Test Cases). |
| **Code Execution Path Coverage** | JaCoCo | **Coverage.py Engine** | Statement coverage threshold ($\ge 75\%$), branch/decision fork tracking, routine reachability, and dead code/unreachable statement isolation (5 Test Cases). |
| **Static Code Analysis** | PMD | **Flake8 / Pylint** | Unused variables, wildcard namespace pollution, variable shadowing, nesting depth limits, and clean code smell audit (5 Test Cases). |
| **Security & Bug Pattern Audit** | SpotBugs | **Bandit Security** | Dangerous execution (`eval`/`exec`), weak cryptographic hashes (`MD5`), hardcoded secrets/API keys, resource leakage, and shell injection (5 Test Cases). |
| **Coding Standard Verification** | Checkstyle | **PEP 8 / Pycodestyle** | 4-space indentation, line length limits ($\le 88$ chars), identifier naming conventions, header import ordering, and whitespace hygiene (5 Test Cases). |
| **Defect Prediction Engine** | Code Metrics | **McCabe Cyclomatic Engine** | Directly implements Curriculum Section 1.9 & Slide 1 requirement: Computes cyclomatic complexity $v(G)$, SLOC, Maintainability Index (MI), and forecasts high-risk defect probability. |

---

## 🎨 Material Design Interface

Designed following **Google Material Design 3 (M3)** specifications:
- **Clean Material Top App Bar:** Branded product header with sticky navigation.
- **Surface Elevation System:** Structured card surfaces with subtle borders and responsive padding.
- **Material Metric Tiles:** Elevated KPI cards for overall Quality Health Score, Test Pass Ratio, and Statement Coverage.
- **Interactive Visualizations:** Chart.js 5-Tool Radar Chart and Test Outcomes Doughnut Chart.
- **Material Filter Chips:** Quick-filter the 25 test cases by tool (PyTest, Coverage, Pylint, Bandit, PEP 8).

---

## 🛠️ Local Installation & Execution

```bash
cd Project_1_Complex_Code_Testing_Dashboard
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
python app.py
```
Open **`http://127.0.0.1:5000`** in your browser.
