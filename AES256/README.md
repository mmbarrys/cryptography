# AES-256 Benchmark Project

Project ini membandingkan performa enkripsi AES-256 antara C++ dan Python.

## Cara Menjalankan
### C++ (MinGW/G++)
1. Compile: `g++ AES_v1.cpp -o aes256`
2. Run: `./aes256`

### Python
1. Install requirements: `pip install pycryptodome`
2. Run: `python aes256_v1.py`

## Hasil Benchmark
- C++ Latency: ~0.006 ms
- Python Latency: ~3.500 ms