"""
Головна точка входу калькулятора
Запускає веб-версію калькулятора на localhost або production
"""

import os
from calculator import Calculator
from web_view import WebCalculatorView


def main():
    """Головна функція для запуску веб-калькулятора"""
    calculator = Calculator()
    web_view = WebCalculatorView(calculator)
    
    # Отримуємо налаштування з змінних середовища для production
    host = os.environ.get('HOST', '127.0.0.1')
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
    
    web_view.run(host=host, port=port, debug=debug)


if __name__ == "__main__":
    main()
