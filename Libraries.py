# import math
# import random
# print(math.sqrt(16))
# print(random.randint(1, 100))
# import requests
# response = requests.get('https://api.github.com')
# if response.status_code == 200:
#     print('Success:', response.json())
# else:
#     print('Error:', response.status_code)
import pyjokes
joke = pyjokes.get_joke()
print(joke)