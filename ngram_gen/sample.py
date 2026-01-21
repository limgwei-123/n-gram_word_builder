import random

def sample_next_token(context, context_counts, next_counts, temperature: float = 1.0, top_k: int | None = None, top_p: float | None = None ):
    candidates = []
    weights = []

    for (ctx, nxt), c in next_counts.items():
        if ctx == context:
            candidates.append(nxt)
            weights.append(c)

    if not candidates:
        return None

    if temperature <= 0:
        raise ValueError("temperature must be > 0")

    if temperature != 1.0:
        inv_t = 1.0 / temperature
        weights = [w ** inv_t for w in weights]  # 不需要先归一化

    if top_k is not None:
        if top_k <= 0:
            raise ValueError("top_k must be > 0")
        # 按权重排序，保留前 k
        pairs = sorted(zip(candidates, weights), key=lambda x: x[1], reverse=True)[:top_k]
        candidates, weights = zip(*pairs)
        candidates, weights = list(candidates), list(weights)

    # 4) top-p：按概率从高到低累加，保留累计 >= p 的最小集合
    if top_p is not None:
        if not (0 < top_p <= 1.0):
            raise ValueError("top_p must be in (0, 1]")

        # 先算概率（归一化）用于累计
        total = sum(weights)
        if total <= 0:
            return None

        probs = [w / total for w in weights]
        pairs = sorted(zip(candidates, probs, weights), key=lambda x: x[1], reverse=True)

        kept = []
        cum = 0.0
        for tok, p, w in pairs:
            kept.append((tok, w))
            cum += p
            if cum >= top_p:
                break

        candidates, weights = zip(*kept)
        candidates, weights = list(candidates), list(weights)

    return random.choices(candidates, weights = weights, k=1)[0]