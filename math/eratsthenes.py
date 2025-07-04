class SieveOfEratosthenes:
    def __init__(self, n):
        self.n = n
        self.primes = []

    def generate_primes(self):
        is_prime = [True] * (self.n + 1)
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(self.n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, self.n + 1, i):
                    is_prime[j] = False

        self.primes = [i for i, prime in enumerate(is_prime) if prime]

    def display_primes(self):
        print(f"2から{self.n}までの素数たち:")
        print(self.primes)


# 使い方
sieve = SieveOfEratosthenes(50)  # 範囲指定：ここでは50まで
sieve.generate_primes()
sieve.display_primes()