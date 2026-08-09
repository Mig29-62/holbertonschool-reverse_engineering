#!/usr/bin/python3
import struct

def decrypt_flag():
    exponent = 0x0000ffffffffffff
    modulus = 0x0ffffffffffffffb
    base = 2

    # Fast modular exponentiation
    key = pow(base, exponent, modulus)
    print(f"[*] Computed Key: {hex(key)}")

    encrypted_bytes = [
        0x8e82d972b66c836f,
        0xa896da60a7779a69,
        0xbc84db77a0729877,
        0xa582d1758c778461,
        0xa883da69ba70905f,
        0xa498c14fba6da861,
        0x9980c063a763f700
    ]

    decrypted_chars = []

    for block in encrypted_bytes:
        plain_block = block ^ key
        
        # Emulate the assembly loop: 
        # for var_24h from 0 to 7: shr rdx, (var_24h * 3... wait, shl eax, 3 is index * 8)
        for i in range(8):
            shift_amount = i * 8
            b = (plain_block >> shift_amount) & 0xFF
            if b != 0:
                decrypted_chars.append(chr(b))

    flag = "".join(decrypted_chars)
    print(f"\n[+] Decrypted Flag: {flag}")

if __name__ == "__main__":
    decrypt_flag()
