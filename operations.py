"""
Domain Layer - Операції калькулятора
Містить абстрактний клас та конкретні реалізації операцій
"""

from abc import ABC, abstractmethod


class Operation(ABC):
    """Абстрактний базовий клас для операцій"""
    
    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        """Виконує операцію над двома числами"""
        pass
    
    @abstractmethod
    def get_symbol(self) -> str:
        """Повертає символ операції"""
        pass


class Addition(Operation):
    """Операція додавання"""
    
    def execute(self, a: float, b: float) -> float:
        return a + b
    
    def get_symbol(self) -> str:
        return "+"


class Subtraction(Operation):
    """Операція віднімання"""
    
    def execute(self, a: float, b: float) -> float:
        return a - b
    
    def get_symbol(self) -> str:
        return "-"


class Multiplication(Operation):
    """Операція множення"""
    
    def execute(self, a: float, b: float) -> float:
        return a * b
    
    def get_symbol(self) -> str:
        return "*"


class Division(Operation):
    """Операція ділення"""
    
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Ділення на нуль неможливе!")
        return a / b
    
    def get_symbol(self) -> str:
        return "/"


class Power(Operation):
    """Операція піднесення до степеня"""
    
    def execute(self, a: float, b: float) -> float:
        return a ** b
    
    def get_symbol(self) -> str:
        return "^"
