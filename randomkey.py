import random
import string

length = 16
characters = string.ascii_letters + string.digits

key = ''.join(random.choice(characters) for _ in range(length))
print("Random Key:", key)