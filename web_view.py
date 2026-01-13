"""
Presentation Layer - Веб-представлення калькулятора
Містить Flask додаток для веб-інтерфейсу
"""

from flask import Flask, render_template, request, jsonify
from calculator import Calculator
import re


class WebCalculatorView:
    """Веб-представлення калькулятора"""
    
    def __init__(self, calculator: Calculator):
        self.calculator = calculator
        self.app = Flask(__name__)
        self._setup_routes()
    
    def _parse_expression(self, expression: str) -> tuple:
        """
        Парсить математичний вираз з пробілами або без них
        
        Args:
            expression: Рядок з виразом (наприклад: "10+5" або "10 + 5")
            
        Returns:
            Tuple (a, operation, b)
            
        Raises:
            ValueError: Якщо вираз не може бути розпарсений
        """
        expression = expression.strip()
        
        # Список операцій у порядку пріоритету (для коректного парсингу)
        operations = ['+', '-', '*', '/', '^']
        
        # Спочатку спробуємо розділити по пробілах (якщо є пробіли)
        parts = expression.split()
        if len(parts) == 3:
            try:
                a = float(parts[0])
                operation = parts[1]
                b = float(parts[2])
                if operation in self.calculator.get_available_operations():
                    return (a, operation, b)
            except ValueError:
                pass
        
        # Якщо не спрацювало, парсимо без пробілів
        for op in operations:
            op_escaped = re.escape(op)
            pattern = rf'^(-?\d+\.?\d*)\s*{op_escaped}\s*(-?\d+\.?\d*)$'
            match = re.match(pattern, expression)
            if match:
                a = float(match.group(1))
                b = float(match.group(2))
                return (a, op, b)
        
        raise ValueError("Невірний формат! Використовуйте: число операція число (з пробілами або без)")
    
    def _setup_routes(self):
        """Налаштовує маршрути Flask"""
        
        @self.app.route('/')
        def index():
            """Головна сторінка"""
            return render_template('calculator.html')
        
        @self.app.route('/calculate', methods=['POST'])
        def calculate():
            """API endpoint для обчислення"""
            try:
                data = request.get_json()
                expression = data.get('expression', '').strip()
                
                if not expression:
                    return jsonify({
                        'success': False,
                        'error': 'Введіть вираз для обчислення'
                    }), 400
                
                # Парсимо вираз
                a, operation, b = self._parse_expression(expression)
                
                # Виконуємо обчислення
                result = self.calculator.calculate(a, operation, b)
                
                return jsonify({
                    'success': True,
                    'result': result,
                    'expression': f"{a} {operation} {b}",
                    'formatted_result': f"{a} {operation} {b} = {result}"
                })
            
            except ValueError as e:
                return jsonify({
                    'success': False,
                    'error': str(e)
                }), 400
            
            except Exception as e:
                return jsonify({
                    'success': False,
                    'error': f'Невідома помилка: {str(e)}'
                }), 500
    
    def run(self, host='127.0.0.1', port=5000, debug=True):
        """Запускає веб-сервер"""
        print(f"\n{'='*60}")
        print("          БАЗОВИЙ КАЛЬКУЛЯТОР - ВЕБ-ВЕРСІЯ")
        print(f"{'='*60}")
        print(f"Сервер запущено на http://{host}:{port}")
        print(f"Відкрийте браузер та перейдіть за адресою: http://{host}:{port}")
        print(f"{'='*60}\n")
        self.app.run(host=host, port=port, debug=debug)
