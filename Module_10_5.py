import time
import multiprocessing as mp

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)

if __name__ == '__main__':

    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    print("Линейное выполнение:")
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    end_time = time.time()
    print(f"Время выполнения (линейно): {end_time - start_time:.6f} секунд")

    print("\nМногопроцессное выполнение:")
    start_time = time.time()
    with mp.Pool() as pool:
        pool.map(read_info, filenames)
    end_time = time.time()
    print(f"Время выполнения (многопроцессно): {end_time - start_time:.6f} секунд")
