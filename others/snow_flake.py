import time

class Snowflake:
    def __init__(self, epoch_ms=1609459200000, worker_id=1):
        self.E=epoch_ms; self.w=worker_id & 0x3FF; self.seq=0; self.last=0
    def next(self):
        now=int(time.time()*1000)-self.E
        if now==self.last:
            self.seq=(self.seq+1)&0xFFF
            if self.seq==0:
                while int(time.time()*1000)-self.E==now: pass
                now=int(time.time()*1000)-self.E
        else: self.seq=0; self.last=now
        return (now<<22)|(self.w<<12)|self.seq

sf=Snowflake(worker_id=42)
print([sf.next() for _ in range(3)])