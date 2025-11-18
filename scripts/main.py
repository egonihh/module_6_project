print ("Welcome to the Cybersecurity Toolkit")
selection = input("Select an option to continue:\n1. Password Strength Checker\n2. hash generator\n3. URL scanner\nEnter 1, 2, or 3: ")
if selection == '1':
    from password_checker import password_checker
    password_checker()
if selection == '2':
    from hash_generator import generate_sha256_hash
    generate_sha256_hash()
if selection == '3':
    from url_scanner import scan_url
    scan_url()
else:
    print("Invalid selection. Please run the program again and select 1, 2, or 3.")