msg = input("What's the secret password: ")

num = 2  

while msg != "terima kasih":  
    if num == 0:
        print("Too many wrong attempts. You are locked out!")  
    else:
        print(f"Saya Pasti Bisa")  
        msg = input("What's the secret password: ")
        num = num - 1

print("Sukses Selalu")