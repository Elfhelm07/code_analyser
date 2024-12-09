import pytest
from src.analyzer import CodeAnalyzer, AnalysisResult

def test_analyze_syntax_error():
    """Test that syntax errors are correctly identified."""
    code = "def foo(:\n    pass"
    analyzer = CodeAnalyzer()
    results = analyzer.analyze(code)
    assert len(results) == 1
    assert results[0].issue_type == "Syntax Error"
    assert results[0].line_number == 1

def test_analyze_nested_loops():
    """Test that nested loops are detected and flagged."""
    code = """
for i in range(10):
    for j in range(10):
        pass
"""
    analyzer = CodeAnalyzer()
    results = analyzer.analyze(code)
    assert any(result.issue_type == "Nested Loop" for result in results)
    assert any(result.description == "Nested loops detected which might cause performance issues" 
              for result in results)

def test_analyze_list_comprehension():
    """Test that opportunities for list comprehension are identified."""
    code = """
result = []
for i in range(10):
    result.append(i)
"""
    analyzer = CodeAnalyzer()
    results = analyzer.analyze(code)
    assert any(result.issue_type == "List Building" for result in results)
    assert any(result.suggestion == "Consider using list comprehension for better performance" 
              for result in results)

def test_analyze_empty_code():
    """Test handling of empty code input."""
    analyzer = CodeAnalyzer()
    results = analyzer.analyze("")
    assert len(results) == 0

def test_analyze_complex_nested_structure():
    """Test detection of multiple levels of nested loops."""
    code = """
for i in range(10):
    for j in range(10):
        for k in range(10):
            pass
"""
    analyzer = CodeAnalyzer()
    results = analyzer.analyze(code)
    nested_loop_issues = [r for r in results if r.issue_type == "Nested Loop"]
    assert len(nested_loop_issues) >= 1

def test_analyze_valid_syntax():
    """Test that valid code doesn't raise syntax errors."""
    code = """
def calculate_sum(numbers):
    return sum(numbers)
"""
    analyzer = CodeAnalyzer()
    results = analyzer.analyze(code)
    assert not any(result.issue_type == "Syntax Error" for result in results)

def test_multiple_issues():
    """Test that multiple issues in the same code are all detected."""
    code = """
result = []
for i in range(10):
    for j in range(10):
        result.append(i * j)
"""
    analyzer = CodeAnalyzer()
    results = analyzer.analyze(code)
    issue_types = {result.issue_type for result in results}
    assert "Nested Loop" in issue_types
    assert "List Building" in issue_types

@pytest.mark.parametrize("code,expected_issue_type", [
    ("def foo(:\n    pass", "Syntax Error"),
    ("for i in range(10):\n    for j in range(10): pass", "Nested Loop"),
    ("result = []\nfor i in range(10): result.append(i)", "List Building"),
])
def test_different_code_patterns(code: str, expected_issue_type: str):
    """Test various code patterns using parametrize."""
    analyzer = CodeAnalyzer()
    results = analyzer.analyze(code)
    assert any(result.issue_type == expected_issue_type for result in results)