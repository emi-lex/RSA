from rsa import *

if __name__ == '__main__':
    # generate prime numbers p and q
    p = rand_prime()
    q = rand_prime()

    # generate public and private keys
    public_key, private_key = generate_keypair(p, q)

    message = "Hello, RSA!"
    print("Message:", message)

    # Encrypt the message
    encrypted_msg = encrypt(public_key, message)
    print("Encrypted:", encrypted_msg)

    # Decrypt the message
    decrypted_msg = decrypt(private_key, encrypted_msg)
    print("Decrypted:", decrypted_msg)
