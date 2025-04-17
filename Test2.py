def f1():
    try:
        return 777
    except:
        return 888
    finally:
        return 999
print(f1())