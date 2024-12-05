import threading
import time
import datetime


def write_words(word_count, file_name):
    # start = time.time()
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            time.sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")
    # end = time.time()
    # print(end - start)


start = time.time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end = time.time()
print('Работа потоков ', datetime.timedelta(seconds=end - start))

start = time.time()

threa_1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
threa_1.start()

threa_2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
threa_2.start()

threa_3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
threa_3.start()

threa_4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
threa_4.start()

threa_1.join()
threa_2.join()
threa_3.join()
threa_4.join()

end = time.time()
print('Работа потоков ', datetime.timedelta(seconds=end - start))
