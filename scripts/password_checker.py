# password_checker.py
pw = input("Enter password: ")
score = 0
if len(pw) >= 8: score += 1
if any(c.islower() for c in pw) and any(c.isupper() for c in pw): score += 1
if any(c.isdigit() for c in pw): score += 1
if any(c in "!@#$%^&*()-_+=" for c in pw): score += 1

print(["Weak","Medium","Strong"][min(score-1,2)] if score>0 else "Weak")
