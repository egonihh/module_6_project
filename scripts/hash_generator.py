# hash_generator.py
def generate_sha256_hash():
    import hashlib
    text = input("Enter text to hash: ")
    print("SHA256:", hashlib.sha256(text.encode()).hexdigest()'oldu')
