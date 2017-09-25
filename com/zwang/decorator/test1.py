# encoding:UTF-8
def decorate(func):
    print('running decorate', func)

    def decorate_inner():
        print('running decorate_inner function')
        func()

    return decorate_inner


@decorate
def func_1():
    print('running func_1')


if __name__ == '__main__':
    # print(func_1)
    func_1()
