import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        warriors = 100
        day = 0
        print(f'{self.name}, на нас напали!')
        while warriors > 0:
            day += 1
            warriors -= self.power
            print(f"{self.name} сражается {day} день(дня)..., осталось {warriors} воинов.")
            time.sleep(1)
        print(f"{self.name} одержал победу спустя {day} дней(дня)!")


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')
# Вывод строки об окончании сражения
