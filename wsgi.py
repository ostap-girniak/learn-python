"""
WSGI entry point for production servers (gunicorn)
"""

import os
from calculator import Calculator
from web_view import WebCalculatorView

# Створюємо екземпляри
calculator = Calculator()
web_view = WebCalculatorView(calculator)

# Експортуємо Flask app для gunicorn
app = web_view.get_app()

if __name__ == "__main__":
    # Для локального запуску
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
