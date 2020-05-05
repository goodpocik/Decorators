def myDecorator(func):
    def wrapper():
        print('Обертка')
        print(f'Оборачиваем функцию: {func}')
        print('Выполняем функцию:')
        func()
        print('Закончили функцию')
    return wrapper


def speedtest(func):
    import time

    def wrapper():
        start = time.time()
        func()
        finish = time.time()
        print(f'Прошло {finish - start} времени')
    return wrapper()
@speedtest
def seacrhinGoogle():
    import requests
    search = requests.get('https://google.com/')
seacrhinGoogle()









def multiple():
    c = 4 * 5
    print(c)


