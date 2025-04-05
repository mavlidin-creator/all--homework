class Computer:
    def __init__(self, cpu, memory):
        self.__cpu =  cpu
        self.__memory = memory
    def get_cpu (self):
        return self.__cpu
    def set_cpu(self, cpu):
        self.__cpu = cpu
    def get_memory(self):
        return self.__memory
    def set_memory(self, memory):
        self.__memory = memory
    def make_computations(self):
        return {
            "sum": self.__cpu + self.__memory,
            "difference": self.__cpu - self.__memory,
            "product": self.__cpu * self.__memory,
            "quotient": self.__cpu / self.__memory
            if self.__memory != 0 else "Division by zero"
        }
    def __str__(self):
        return f"Computer(cpu={self.__cpu}, memory={self.__memory})"
    def __eq__(self, other):
        return self.__memory == other.__memory
    def __ne__(self, other):
        return self.__memory != other.__memory
    def __lt__(self, other):
        return self.__memory < other.__memory
    def __le__(self, other):
        return self.__memory <= other.__memory
    def __gt__(self, other):
        return self.__memory > other.__memory
    def __ge__(self, other):
        return self.__memory >= other.__memory
class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list
    def get_sim_cards_list(self):
        return self.__sim_cards_list

    def set_sim_cards_list(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    def call(self, sim_card_number, call_to_number):
        if 1 <= sim_card_number <= len(self.__sim_cards_list):
            sim_name = self.__sim_cards_list[sim_card_number - 1]
            print(f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - {sim_name}")
        else:
            print("Неверный номер сим-карты")
    def __str__(self):
        return f"Phone(sim_cards_list={self.__sim_cards_list})"
class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)
    def use_gps (self, location):
        print(f"Построение маршрута до {location}...")

    def __str__(self):
        return f"SmartPhone(cpu={self.get_cpu()}, memory={self.get_memory()}, sim_cards_list={self.get_sim_cards_list()})"
computer1 = Computer(4, 8)
phone1 = Phone(["Beeline", "O!"])
smartphone1 = SmartPhone(8, 16, ["MegaCom", "O!"])
smartphone2 = SmartPhone(6, 12, ["Beeline"])

print(computer1)
print(phone1)
print(smartphone1)
print(smartphone2)

print("\n--- Демонстрация методов ---")
computer1.make_computations()
computer1.set_cpu(6)

print(f"Новый CPU компьютера: {computer1.get_cpu()}")
computer2 = Computer(2, 8)
computer3 = Computer(4, 16)

print(f"\nСравнение компьютеров (по памяти):")
print(f"computer1 == computer2: {computer1 == computer2}")
print(f"computer1 != computer3: {computer1 != computer3}")
print(f"computer1 < computer3: {computer1 < computer3}")
print(f"computer1 <= computer2: {computer1 <= computer2}")
print(f"computer1 > computer2: {computer1 > computer2}")
print(f"computer1 >= computer2: {computer1 >= computer2}")

phone1.call(1, "+996 555 11 22 33")
phone1.set_sim_cards_list(["Nurtelecom"])
print(f"Новый список сим-карт телефона: {phone1.get_sim_cards_list()}")

smartphone1.make_computations()
smartphone1.call(2, "+996 700 44 55 66")
smartphone1.use_gps("Бишкек, площадь Ала-Тоо")
smartphone1.set_memory(32)
print(f"Новая память смартфона: {smartphone1.get_memory()}")
