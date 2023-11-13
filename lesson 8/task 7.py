class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        real_sum = self.real + other.real
        imag_sum = self.imag + other.imag
        return ComplexNumber(real_sum, imag_sum)

    def __mul__(self, other):
        real_prod = self.real * other.real - self.imag * other.imag
        imag_prod = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_prod, imag_prod)

    def __str__(self):
        if self.real != 0 and self.imag != 0:
            return f"{self.real} + {self.imag}i"
        elif self.real != 0:
            return f"{self.real}"
        elif self.imag != 0:
            return f"{self.imag}i"
        else:
            return "0"

# Создание комплексных чисел
c1 = ComplexNumber(6, 8)
c2 = ComplexNumber(-1, 4)

# Сложение комплексных чисел
sum_result = c1 + c2
print("Sum:", sum_result)

# Умножение комплексных чисел
prod_result = c1 * c2
print("Product:", prod_result)
