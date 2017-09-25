# encoding:UTF-8
# 装饰器模式
def outer(func):
    print('enter outer', func)

    def wrapper():
        print('running outer')
        func()

    return wrapper


def inner(func):
    print('enter inner', func)

    def wrapper():
        print('running inner')
        func()

    return wrapper


@outer
@inner
def main():
    print('running main')


if __name__ == '__main__':
    main()
