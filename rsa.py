from random import randrange
from math import gcd
from sympy import randprime


def get_prime(n_bits: int = 1000) -> int:
    return randprime(2 ** (n_bits - 1), 2 ** n_bits)


def generate_keypair(p: int, q: int) -> tuple[tuple[int, int], tuple[int, int]]:
    n = p * q
    phi = (p - 1) * (q - 1)

    e = randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = randrange(1, phi)
        g = gcd(e, phi)

    d = pow(e, -1, phi)
    return (e, n), (d, n)


def encrypt(public_key: tuple[int, int], plaintext: str) -> list[int]:
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in plaintext]
    return cipher


def decrypt(private_key: tuple[int, int], ciphertext: list[int]) -> str:
    d, n = private_key
    plain = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plain)
