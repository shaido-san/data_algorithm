import random

def push_sum(values, rounds=10):
    n = len(values)
    # 各ノードは (s, w) を持つ
    states = [(v, 1.0) for v in values]

    for r in range(rounds):
        new_states = [(0, 0) for _ in range(n)]
        for i, (s, w) in enumerate(states):
            # 半分は自分に残す
            share_s, share_w = s / 2, w / 2
            self_s, self_w = share_s, share_w
            # 半分はランダムな相手へ
            j = random.randint(0, n - 1)
            recv_s, recv_w = share_s, share_w

            # 自分に加算
            new_states[i] = (new_states[i][0] + self_s, new_states[i][1] + self_w)
            # 相手に加算
            new_states[j] = (new_states[j][0] + recv_s, new_states[j][1] + recv_w)

        states = new_states
        estimates = [s / w for s, w in states]
        print(f"Round {r+1}: {['%.3f' % e for e in estimates]}")

    return [s / w for s, w in states]


# --- 実行例 ---
values = [3, 7, 20, 10, 50]  # 各ノードの初期値
final_estimates = push_sum(values, rounds=10)
print("Final estimates:", final_estimates)
print("Real average:", sum(values) / len(values))