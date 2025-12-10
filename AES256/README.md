# AES-256 Benchmark Project

## Cara Menjalankan
### C++ (MinGW/G++)
1. Compile: `g++ AES_v1.cpp -o aes256`
2. Run: `./aes256`

### Python
1. Install requirements: `pip install pycryptodome`
2. Run: `python aes256_v1.py`

## Hasil Benchmark
- aes.py v1 (ECB): 0.4887 ms
- aes.py v1 (CBC): 0.5381 ms
- aes.py v2 (ECB): 0.0420 ms
- aes.py v2 (ECB): 0.0414 ms
---------------------
- aes c++ v1 (ECB): 0.0030 ms
- aes c++ v1 (CBC): 0.0030 ms
- aes c++ v2 (ECB): 0.0030 ms
- aes c++ v2 (CBC): 0.0030 ms

- Python Latency dengan hitung key exp: ~0.5134 ms
- Python Latency tanpa hitung key exp : ~0.04 ms
- C++ Latency dengan atau tanpa hitung key exp: ~0.003 ms
