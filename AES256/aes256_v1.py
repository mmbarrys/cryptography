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
    if mode_choice == '2':
        iv = get_random_bytes(16)

    start_time: float = time.perf_counter()
    if mode_choice == '1':  # ECB
        print(f"\n[LOG] Mode: ECB (Electronic Codebook)")    
        cipher = AES.new(key, AES.MODE_ECB)
        ciphertext = cipher.encrypt(padded_data)       
        result_bytes = ciphertext         # Hasil ECB hanya ciphertext
        
    elif mode_choice == '2':  # CBC
        print(f"\n[LOG] Mode: CBC (Cipher Block Chaining)")
        cipher = AES.new(key, AES.MODE_CBC, iv)
        ciphertext = cipher.encrypt(padded_data)
        
        # IV 16 byte + Ciphertext
        result_bytes = iv + ciphertext
    else:
        return "Error: Mode tidak valid."

    base64_result = base64.b64encode(result_bytes).decode('utf-8') #Encode ke Base64 untuk output
    end_time: float = time.perf_counter()
    duration_seconds = end_time - start_time
    duration_ms = duration_seconds * 1000       
    duration_us = duration_seconds * 1_000_000  

    print("-" * 30)
    print(f"[METRICS] Latency: {duration_ms:.4f} ms ({duration_us:.2f} µs)")
    print("-" * 30)
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