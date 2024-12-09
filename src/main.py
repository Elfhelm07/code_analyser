from flask import Flask, render_template, request
from analyzer import CodeAnalyzer
from typing import List, Dict

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    code = request.form.get('code', '')
    analyzer = CodeAnalyzer()
    results = analyzer.analyze(code)
    return render_template('results.html', results=results, code=code)

if __name__ == '__main__':
    app.run(debug=True)