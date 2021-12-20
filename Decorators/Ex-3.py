#How to call Same function with decorator and without decorator?
def decor(func):
    def inner(name):
        if name=='MSD':
            print('#'*50)
            print('Hello MSD, you are very important to us')
            print('Very good morning')
            print('#'*50)
        else:
            func(name)
    return inner
def wish(name):
    print('Good morning:',name)
decorated_wish=decor(wish)
wish('Karthik')
wish('MSD')
decorated_wish('MSD')
