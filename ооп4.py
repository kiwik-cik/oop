class Counter:
    def start_from(self, value = 0):
        self.value = value
    def increment(self):
        self.value+=1
    def display(self):
        print(f'Текущее значение счетчика: {self.value}')
    def reset(self):
        self.value = 0

counter = Counter()
counter.start_from(5)#Задаем начальное значение счетчика
counter.increment()#Увеличиваем счетчик на 1

counter.display()  # Текущее значение счетчика = 6
counter.reset()# Обнуляем счетчик

counter.display()  # Текущее значение счетчика = 0