"""
Web-Based Complex Code Testing Dashboard (Python Edition)
SDM College of Engineering & Technology, Dharwad
Department of Computer Science & Engineering
Course: Software Testing (22UCSES731)
Author: Amogh S Patil (2SDS23CS011)
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
        "service": "Complex Code Testing Dashboard (Python)",
        "author": "Amogh S Patil (2SDS23CS011)",
        "institution": "SDMCET Dharwad",
        "version": "1.0.0"
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
