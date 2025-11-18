# hash_generator.py
import hashlib
text = input("Enter text to hash: ")
print("SHA256:", hashlib.sha256(text.encode()).hexdigest())
