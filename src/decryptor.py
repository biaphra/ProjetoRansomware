import os
from cryptography.fernet import Fernet
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.banner import banner

# Carregar chave de descriptografia
def load_key():
    key_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "keys", "encryption.key")
    return open(key_path, "rb").read()

# Descriptografar arquivos
def decrypt_files(directory, key):
    fernet = Fernet(key)

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "rb") as target_file:
                    data = target_file.read()
                decrypted_data = fernet.decrypt(data)
                with open(file_path, "wb") as target_file:
                    target_file.write(decrypted_data)
                print(f"[+] Arquivo descriptografado: {file_path}")
            except Exception as e:
                print(f"[!] Erro ao descriptografar {file_path}: {e}")

if __name__ == "__main__":
    banner()
    directory = input("Digite o caminho do diretório para descriptografar: ")
    try:
        key = load_key()
        decrypt_files(directory, key)
    except FileNotFoundError:
        print("[!] Erro: Arquivo de chave não encontrado em 'keys/encryption.key'")
