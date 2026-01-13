"""
Головна точка входу калькулятора
Запускає веб-версію калькулятора на localhost
"""

from calculator import Calculator
from web_view import WebCalculatorView


def main():
    """Головна функція для запуску веб-калькулятора"""
    calculator = Calculator()
    web_view = WebCalculatorView(calculator)
    web_view.run(host='127.0.0.1', port=5000, debug=True)


if __name__ == "__main__":
    main()
