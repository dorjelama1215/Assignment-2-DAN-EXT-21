
def encrypt_messsage(shift1, shift2):
    pass
def decrypt_message(shift1, shift2):
    pass
def verify_decryption():
    pass
def main():
    print("=== Question 1: Encryption/Decryption ===")
    shift1 = int(input("Enter shift1 value: "))
    shift2 = int(input("Enter shift2 value: "))
    
    encrypt_text(shift1, shift2)
    decrypt_text(shift1, shift2)
    verify_decryption()

if __name__ == "__main__":
    main()
