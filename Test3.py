def f1():
    try:
        print('try-1')
        print('try-2')
        print('try-3')
        try:
            print('try-4')
            print('try-5')
            print('try-6')
        except:
            print(10/0)
        finally:
            print('finally-8')
        print('stmt-9')
    except:
        print('catch-10')
    finally:
        print('finally-11')
    print('stmt-12')
print(f1())

