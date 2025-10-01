import numpy as np

def hits(adj_matrix, max_iter=100, tol=1e-6):
    n = adj_matrix.shape[0]
    hubs = np.ones(n)
    auth = np.ones(n)

    for _ in range(max_iter):
        # Authority update
        new_auth = adj_matrix.T @ hubs
        # Hub update
        new_hubs = adj_matrix @ new_auth

        # 正規化
        new_auth = new_auth / np.linalg.norm(new_auth, 2)
        new_hubs = new_hubs / np.linalg.norm(new_hubs, 2)

        # 収束判定
        if np.allclose(auth, new_auth, atol=tol) and np.allclose(hubs, new_hubs, atol=tol):
            break

        auth, hubs = new_auth, new_hubs

    return auth, hubs


# --- テスト ---
# ページ間リンクを隣接行列で表す
# 例: 0→1, 0→2, 1→2, 2→0, 2→3
adj = np.array([
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 0, 0, 0]
])

auth, hubs = hits(adj)
print("Authority scores:", auth)
print("Hub scores:", hubs)