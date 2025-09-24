import time

class TokenBucket:
    def __init__(self, rate, burst):
        self.rate = rate
        self.capacity = burst
        self.tokens = burst
        self.t0 = time.time()

    def allow(self, n=1):
        now = time.time()
        elapsed = now - self.t0
        self.tokens = min(self.capacity, self.tokens + elapsed * self.rate)
        self.t0 = now

        if self.tokens >= n:
            self.tokens -= n
            return True
        return False

if __name__ == "__main__":
    tb = TokenBucket(rate=5, burst=10)
    print([tb.allow() for _ in range(12)])
    time.sleep(1.1)
    print(tb.allow())