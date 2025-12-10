import base64
import hashlib
import time
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

def generate_key(password):
    return hashlib.sha256(password.encode('utf-8')).digest()

def encrypt_aes(mode_choice, password, plaintext):
    #input kunci 256bit
    key = generate_key(password)
    
    # Padding PKCS7 128 bit)
    padded_data = pad(plaintext.encode('utf-8'), AES.block_size)  
    result_bytes = b''
    iv = None
    cipher = None
    if mode_choice == '1':  # ECB
        cipher = AES.new(key, AES.MODE_ECB)
    elif mode_choice == '2':  # CBC
        iv = get_random_bytes(16)                
        cipher = AES.new(key, AES.MODE_CBC, iv)
    else:
        return "Error: Mode tidak valid."

    start_time: float = time.perf_counter()
    ciphertext = cipher.encrypt(padded_data)       
    end_time: float = time.perf_counter()

    if mode_choice == '1':
        print(f"\n[LOG] Mode: ECB (Electronic Codebook)")
        result_bytes = ciphertext
    elif mode_choice == '2':
        print(f"\n[LOG] Mode: CBC (Cipher Block Chaining)")
        print(f"[LOG] IV (Random Hex): {iv.hex()}")
        result_bytes = iv + ciphertext

    duration_ms = (end_time - start_time) * 1000
    duration_us = (end_time - start_time) * 1_000_000

    print("-" * 30)
    print(f"Latency: {duration_ms:.4f} ms ({duration_us:.2f} µs)")
    print("-" * 30)

    base64_result = base64.b64encode(result_bytes).decode('utf-8') #Encode ke Base64 untuk output
    return base64_result

def main():
    print("=== AES-256 ===")
    # Input User
    print("Pilih Mode:")
    print("1. ECB")
    print("2. CBC")
    mode = input("Pilihan (1/2): ").strip()
    
    if mode not in ['1', '2']:
        print("Pilihan mode salah!")
        return

    password = input("Masukkan Kunci (Password): ")
    message = input("Masukkan Pesan: ")

    # Proses Enkripsi
    try:
        encrypted_text = encrypt_aes(mode, password, message)
        
        print("\n=== HASIL ENKRIPSI (BASE64) ===")
        print(encrypted_text)
        print("===============================")
        
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    main()