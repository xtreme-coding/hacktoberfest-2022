
def encrypt_decrypt(input_text):
    text = input_text.lower()
    result_text = ''
    
    i = len(text)-1

    while i >= 0:
        result_text += text[i]
        i -= 1

    return result_text

def main():
    message_text = "Hello World"
    encrypt_text = encrypt_decrypt(message_text)
    decrypt_text = encrypt_decrypt(encrypt_text)

    print("Encrypt Text = ",encrypt_text)
    print("Decrypt Text = ",decrypt_text)

if __name__ == "__main__":
    main()