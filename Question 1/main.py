
from encryption import encrypted_file
from decryption import decrypted_file
from verification import verification_files


def main() -> None:
    print("=== File Encryption Program ===")

    shift1 = int(input("Enter shift1 value: "))
    shift2 = int(input("Enter shift2 value: "))

    encrypted_file(shift1=shift1, shift2=shift2)
    print("Encryption completed. Encrypted text saved to encrypted_text.txt")

    decrypted_file(shift1=shift1, shift2=shift2)
    print("Decryption completed. Decrypted text saved to decrypted_text.txt")

    if verification_files():
        print("Verification Successful: Decrypted text matches the original.")
    else:
        print("Verification Failed: Decrypted text does NOT match the original.")


if __name__ == "__main__":
    main()