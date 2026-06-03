
def f3():
    print('3')
    return


def f2():
    f3()
    print('2')

def  f1():
    f2()
    print('1')

def main():
    f1()
    print('main')

if __name__=='__main__':
    main()