from ngram_gen.sample import sample_next_token


def generate_text(n, context_counts,next_counts, max_len = 50):
    context = tuple(["<s>"] * (n - 1))
    output = []

    for _ in range(max_len):
        nxt = sample_next_token(context, context_counts,next_counts)
        if nxt is None:
            break
        if nxt == "</s>":
            break

        output.append(nxt)
        context = tuple(list(context[1:]) + [nxt])

    return "".join(output)