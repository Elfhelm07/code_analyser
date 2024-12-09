# Code Performance Analyzer

An AI-powered tool that analyzes Python code snippets for potential performance bottlenecks and provides optimization suggestions.

## Features

- Identifies nested loops and suggests optimizations
- Detects potential list comprehension opportunities
- Provides line-specific suggestions for improvements
- Web interface for easy code submission and analysis

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Elfhelm07/code_analyser.git
   cd code-analyzer
   ```

   

2. **Create a virtual environment and activate it:**

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

   

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```



## Running the Application

1. **Start the Flask server:**
```   bash
   python src/main.py
```

2. **Open your browser and navigate to** `http://localhost:5000`

## Design Choices

- **AST Analysis**: Utilizes Python's abstract syntax tree to analyze code structure for performance issues.
- **Type Hints**: Implements static typing for better code maintainability and readability.
- **Modular Design**: Separates analysis logic from the web interface for cleaner architecture.
- **Dataclass Usage**: Uses dataclasses for structured and easy-to-manage result storage.

## Assumptions and Limitations

- **Python Only**: Currently, the tool only analyzes Python code snippets.
- **Static Analysis**: The analysis is static and may not catch runtime-specific optimizations.
- **Basic Patterns**: Focuses on identifying basic performance patterns like nested loops and list comprehensions.

## Screenshots

![Home Page](screenshots/home_page.png)
![Analysis Results](screenshots/analysis_results.png)

## Running Tests

To run the tests, execute:

```bash
python -m pytest tests/
```
