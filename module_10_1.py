import time
from threading import Thread

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения {func.__name__} с аргументами {args}: {end_time - start_time:.6f} секунд")
        return result
    return wrapper

@measure_time
def write_words(word_count, file_name):
    with open(file_name, 'w') as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            time.sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

# Словарь с параметрами для вызова функций
function_calls = {
    'example1.txt': 10,
    'example2.txt': 30,
    'example3.txt': 200,
    'example4.txt': 100
}

# Измерение времени выполнения функций без потоков
start_time_functions = time.time()

for file_name, word_count in function_calls.items():
    write_words(word_count, file_name)

end_time_functions = time.time()
print(f"Общее время выполнения функций: {end_time_functions - start_time_functions:.6f} секунд")

# Словарь с параметрами для вызова функций в потоках
thread_calls = {
    'example5.txt': 10,
    'example6.txt': 30,
    'example7.txt': 200,
    'example8.txt': 100
}

# Измерение времени выполнения функций с использованием потоков
start_time_threads = time.time()

threads = []
for file_name, word_count in thread_calls.items():
    thread = Thread(target=write_words, args=(word_count, file_name))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time_threads = time.time()
print(f"Общее время выполнения потоков: {end_time_threads - start_time_threads:.6f} секунд")