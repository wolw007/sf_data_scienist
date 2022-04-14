
import numpy as np
def secret_number(number:int)->int:
    count = 0
    min_n = 1
    max_n = 101

    while True:
        count += 1
        mid=((min_n + max_n)//2)
    
        if mid > number:
            max_n = mid

        elif mid < number:
            min_n = mid

        else:
            break 
    return(count)
secret_number(np.random.randint(1,101))

def score_game(secret_number) -> int:
    sum_count = []
    np.random.seed(1)
    number_array = np.random.randint(1, 101, size=(1000))
    for number in number_array:
        sum_count.append(secret_number(number))
    score = int(np.mean(sum_count))
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

if __name__ == '__main__':
    score_game(secret_number)