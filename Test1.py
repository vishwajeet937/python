def f1():
    try:
        return 10
    except:
        print('except')
    finally:
        print('finally')
print(f1())