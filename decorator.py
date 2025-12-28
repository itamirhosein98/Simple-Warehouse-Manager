# این دکوریتور ماست (کادوپیچ)
def my_decorator(func):
    def wrapper():
        print("--- start work---")
        func() # اینجا تابع اصلی اجرا می‌شود
        print("--- end work---")
    return wrapper

# حالا با علامت @ از آن استفاده می‌کنیم
@my_decorator
def say_hello():
    print("hello world!")

say_hello()



