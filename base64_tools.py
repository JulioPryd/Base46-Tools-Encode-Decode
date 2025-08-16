import base64

def encode_base64(text):
    text_bytes = text.encode("utf-8")
    encoded = base64.b64encode(text_bytes)
    return encoded.decode("utf-8")

def decode_base64(encoded_text):
    try:
        text_bytes = base64.b64decode(encoded_text)
        return text_bytes.decode("utf-8")
    except Exception as e:
        return f"Error: {e}"

def main():
    while True:
        print("\n=== Base64 Tools ===")
        print("1. Encode")
        print("2. Decode")
        print("3. Exit")
        choice = input("Pilih menu (1/2/3): ")

        if choice == "1":
            plain_text = input("Masukkan teks yang ingin di-encode: ")
            print("Hasil Encode:", encode_base64(plain_text))

        elif choice == "2":
            encoded_text = input("Masukkan teks base64 yang ingin di-decode: ")
            print("Hasil Decode:", decode_base64(encoded_text))

        elif choice == "3":
            print("Keluar...")
            break
        else:
            print("Pilihan tidak valid, coba lagi!")

if __name__ == "__main__":
    main()
