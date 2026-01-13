"""
Application Layer - Логіка калькулятора
Містить клас Calculator, який використовує операції
"""

from operations import Addition, Subtraction, Multiplication, Division, Power


class Calculator:
    """Калькулятор, який використовує операції"""
    
    def __init__(self):
        self.operations = {
            '+': Addition(),
            '-': Subtraction(),
            '*': Multiplication(),
            '/': Division(),
            '^': Power(),
        }
    
    def calculate(self, a: float, operation: str, b: float) -> float:
        """
        Виконує обчислення
        
        Args:
            a: Перше число
            operation: Символ операції (+, -, *, /, ^)
            b: Друге число
            
        Returns:
            Результат обчислення
            
        Raises:
            ValueError: Якщо операція не підтримується або виникла помилка
        """
        if operation not in self.operations:
            raise ValueError(f"Операція '{operation}' не підтримується!")
        
        op = self.operations[operation]
        return op.execute(a, b)
    
    def get_available_operations(self) -> list:
        """Повертає список доступних операцій"""
        return list(self.operations.keys())
