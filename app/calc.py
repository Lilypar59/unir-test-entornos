import app
import math

class InvalidPermissions(Exception):
    pass


class Calculator:
    def add(self, x, y):
        self.check_types(x, y)
        return x + y

    def substract(self, x, y):
        self.check_types(x, y)
        return x - y

    def multiply(self, x, y):
        if not app.util.validate_permissions(f"{x} * {y}", "user1"):
            raise InvalidPermissions('Usuario no tiene permiso')

        self.check_types(x, y)
        return x * y

    def divide(self, x, y):
        self.check_types(x, y)
        if y == 0:
            raise TypeError("Division por cero es imposible")

        return x / y

    def power(self, x, y):
        self.check_types(x, y)
        return x ** y

    def check_types(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Los parámetros deben ser números")

        # funciones nuevas

    def sqrt(self, x):
        self.check_types(x, 0)
        if x < 0:
            raise TypeError("No se puede calcular la raíz cuadrada de un número negativo")
        return math.sqrt(x)

    def log10(self, x):
        self.check_types(x, 0)
        if x <= 0:
            raise TypeError("logaritmo indefinido para números no positivos")
        return math.log10(x)

    def mod(self, x, y):
        self.check_types(x, y)
        if y == 0:
            raise TypeError("Modulo by zero is not allowed")
        return x % y

    def abs_value(self, x):
        self.check_types(x, 0)
        return abs(x)

    def avg(self, values):
        if not values or not all(isinstance(v, (int, float)) for v in values):
            raise TypeError("Todos los valores deben ser números")
        return sum(values) / len(values)

    def max_value(self, values):
        if not values or not all(isinstance(v, (int, float)) for v in values):
            raise TypeError("Todos los valores deben ser números")
        return max(values)

    def min_value(self, values):
        if not values or not all(isinstance(v, (int, float)) for v in values):
            raise TypeError("Todos los valores deben ser números")
        return min(values)

    def factorial(self, x):
        self.check_types(x, 0)
        if x < 0 or not float(x).is_integer():
            raise TypeError("El factorial solo está definido para enteros no negativos")
        return math.factorial(int(x))

    def percent(self, x, y):
        self.check_types(x, y)
        if y == 0:
            raise TypeError("El factorial solo está definido para enteros no negativos")
        return (x / y) * 100

    def inverse(self, x):
        self.check_types(x, 0)
        if x == 0:
            raise TypeError("No se puede calcular el inverso de cero")
        return 1 / x

if __name__ == "__main__":  # pragma: no cover
    calc = Calculator()
    result = calc.add(2, 2)
    print(result)
