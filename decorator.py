# # این دکوریتور ماست (کادوپیچ)
# def my_decorator(func):
#     def wrapper():
#         print("--- start work---")
#         func() # اینجا تابع اصلی اجرا می‌شود
#         print("--- end work---")
#     return wrapper

# # حالا با علامت @ از آن استفاده می‌کنیم
# @my_decorator
# def say_hello():
#     print("hello world!")

# say_hello()


# این خودِ دکوریتور یا همون کادو هست
# def my_template(func):
#     def wrapper():
#         print("--------------------") # کار اضافه قبل از تابع
#         func()                       # اجرای تابع اصلی
#         print("--------------------") # کار اضافه بعد از تابع
#     return wrapper

# # حالا از دکوریتور استفاده می‌کنیم
# @my_template
# def show_name():
#     print("  AMIR MOHSENI  ")

# # اجرا
# # show_name()
# # def star_decorator(func):
# #     def wrapper():
# #         print("*****")
# #         func()
# #         print("*****")
# #     return wrapper
# # @star_decorator
# # def greet():
# #     print("Learing Python Decorators!")
# # greet()

# def star_decorator(func):
#     # این ستاره‌ها یعنی هر چی ورودی اومد رو قبول کن
#     def wrapper(*args, **kwargs):
#         print("**********")
#         func(*args, **kwargs) # ورودی‌ها رو بده به تابع اصلی
#         print("**********")
#     return wrapper

# @star_decorator
# def greet_user(name, age):
#     print(f"سلام {name}! تو {age} سالته و داری پایتون یاد می‌گیری.")

# greet_user("امیر", 25)
import time
def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper
@timer_decorator
def heavy_task():
    print("Starting heavy task...")
    time.sleep(2)  # شبیه‌سازی یک کار سنگین با تاخیر ۲ ثانیه
    print("Heavy task completed!")
heavy_task()



