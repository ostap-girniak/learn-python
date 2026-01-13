"""
Presentation Layer - Представлення для терміналу
Містить клас CalculatorView для інтерфейсу користувача
"""

from typing import Union
import re
from calculator import Calculator


class CalculatorView:
    """Представлення калькулятора для терміналу"""
    
    def __init__(self, calculator: Calculator):
        self.calculator = calculator
    
    def display_welcome(self):
        """Відображає привітальне повідомлення"""
        print("=" * 50)
        print("          БАЗОВИЙ КАЛЬКУЛЯТОР")
        print("=" * 50)
        print(f"Доступні операції: {', '.join(self.calculator.get_available_operations())}")
        print("Можна вводити з пробілами (10 + 5) або без (10+5)")
        print("Для виходу введіть 'q' або 'quit'")
        print("=" * 50)
    
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
        # Використовуємо екранування для спеціальних символів regex
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
        # Шукаємо оператор у виразі
        for op in operations:
            # Екрануємо спеціальні символи для regex
            op_escaped = re.escape(op)
            # Шукаємо паттерн: число оператор число
            pattern = rf'^(-?\d+\.?\d*)\s*{op_escaped}\s*(-?\d+\.?\d*)$'
            match = re.match(pattern, expression)
            if match:
                a = float(match.group(1))
                b = float(match.group(2))
                return (a, op, b)
        
        raise ValueError("Невірний формат! Використовуйте: число операція число (з пробілами або без)")
    
    def get_input(self) -> Union[tuple, None]:
        """
        Отримує введення від користувача
        
        Returns:
            Tuple (a, operation, b) або None якщо вихід
        """
        try:
            user_input = input("\nВведіть вираз (наприклад: 10+5 або 10 + 5): ").strip()
            
            if user_input.lower() in ['q', 'quit', 'exit']:
                return None
            
            return self._parse_expression(user_input)
        
        except ValueError as e:
            print(f"Помилка введення: {e}")
            return self.get_input()
        except KeyboardInterrupt:
            print("\n\nДо побачення!")
            return None
    
    def display_result(self, a: float, operation: str, b: float, result: float):
        """Відображає результат обчислення"""
        print(f"\nРезультат: {a} {operation} {b} = {result}")
    
    def display_error(self, error: str):
        """Відображає повідомлення про помилку"""
        print(f"❌ Помилка: {error}")
    
    def run(self):
        """Запускає інтерактивний режим калькулятора"""
        self.display_welcome()
        
        while True:
            try:
                user_input = self.get_input()
                
                if user_input is None:
                    print("\nДякуємо за використання калькулятора!")
                    break
                
                a, operation, b = user_input
                result = self.calculator.calculate(a, operation, b)
                self.display_result(a, operation, b, result)
            
            except ValueError as e:
                self.display_error(str(e))
            except Exception as e:
                self.display_error(f"Невідома помилка: {e}")
