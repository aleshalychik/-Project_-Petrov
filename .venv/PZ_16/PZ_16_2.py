# Базовый (родительский) класс
class Animal:
    def breathe(self):
        print("Животное дышит...")

    def eat(self):
        print("Животное питается...")

# Класс-наследник
class Dog(Animal):
    def bark(self):
        print("Собака: Гав-гав!")

# Класс-наследник
class Cat(Animal):
    def purr(self):
        print("Кошка: Мур-мур...")

# --- Пример использования ---
dog = Dog()
cat = Cat()

print("--- Действия собаки ---")
dog.breathe()  # Метод унаследован от Animal
dog.eat()      # Метод унаследован от Animal
dog.bark()     # Уникальный метод класса Dog

print("\n--- Действия кошки ---")
cat.breathe()  # Метод унаследован от Animal
cat.eat()      # Метод унаследован от Animal
cat.purr()     # Уникальный метод класса Cat
