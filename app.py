"""
TestPulse — Complex Code Testing Dashboard (Python Edition)
Automated Multi-Tool Software Testing & Quality Assurance Platform
"""

import os
from flask import Flask, render_template, request, jsonify
from analyzer import CodeAnalyzer
from samples import SAMPLE_PROGRAMS

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({
        "status": "healthy",
        "service": "TestPulse — Complex Code Testing Dashboard",
        "version": "2.4.0",
        "tools_integrated": [
            "PyTest",
            "Coverage.py",
            "Flake8 / Pylint",
            "Bandit Security",
            "PEP 8 Standards",
            "McCabe Cyclomatic Defect Predictor"
        ]
    })

@app.route('/api/samples', methods=['GET'])
def get_samples():
    return jsonify({
        key: {
            "title": data["title"],
            "description": data["description"],
            "code": data["code"]
        }
        for key, data in SAMPLE_PROGRAMS.items()
    })

@app.route('/api/analyze', methods=['POST'])
def analyze():
    payload = request.get_json(silent=True) or {}
    code = payload.get('code', '')
    
    if not code or not code.strip():
        return jsonify({
            "success": False,
            "error": "No Python source code supplied. Please type or paste Python code."
        }), 400

    analyzer = CodeAnalyzer(code)
    results = analyzer.analyze_all()
    return jsonify(results)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
