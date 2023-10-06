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
counter.start_from(0)#Задаем начальное значение счетчика
counter.increment()#Увеличиваем счетчик на 1

counter.display()#Текущее значение счетчика
counter.reset()#Обнуляем счетчик

counter.display()#Текущее значение счетчика = 0
counter2 = Counter()#Создаем новый экземпляр класса Counter
counter2.start_from(2)#Задаем начальное значение счетчика для counter2
counter2.increment()#Увеличиваем счетчик на 1 для counter2
counter2.display() #Текущее значение счетчика






