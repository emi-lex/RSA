from random import randint


def miller_rabin(p: int, k: int = 100):
    if p == 2:
        return True
    if p % 2 == 0:
        return False

    s = 0
    d = p - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    for _ in range(k):
        a = randint(2, p - 1)
        x = pow(a, d, p)

        if x == 1 or x == p - 1:
            continue

        for _ in range(s - 1):
            if x == p - 1:
                break
            x = (x ** 2) % p
            if x == 1:
                return False

        if x != p - 1:
            return False

    return True


def rand_prime(n_bits: int = 32) -> int:
    a = 2 ** (n_bits - 1)
    b = a * 2
    p = randint(a, b)
    while not miller_rabin(p):
        p = randint(a, b)
    return p


def extended_euclid(a: int, m: int):
    r_, r = a, m
    s_, s = 1, 0
    t_, t = 0, 1

    while r != 0:
        b = r_ // r
        r_, r = r, r_ - b * r
        s_, s = s, s_ - b * s
        t_, t = t, t_ - b * t

    return s_ % m if s_ < 0 else (m + s_) % m, r_ == 1


def generate_keypair(p: int, q: int) -> tuple[tuple[int, int], tuple[int, int]]:
    n = p * q
    phi = (p - 1) * (q - 1)

    e = randint(1, phi)
    d, inv = extended_euclid(e, phi)
    while not inv:
        e = randint(1, phi)
        d, inv = extended_euclid(e, phi)
    return (e, n), (d, n)


def encrypt(public_key: tuple[int, int], plaintext: str) -> list[int]:
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in plaintext]
    return cipher


def decrypt(private_key: tuple[int, int], ciphertext: list[int]) -> str:
    d, n = private_key
    plain = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plain)
