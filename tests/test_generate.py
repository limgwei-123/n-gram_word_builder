from ngram_gen.generate import generate_text

def test_generate_respects_max_len():
    context_counts = {
        ("<s>",): 1
    }
    next_counts = {
        (("<s>",), "a"): 1,
        (("a",), "a"): 1,   # 无限循环风险
    }

    out = generate_text(
        n=2,
        context_counts=context_counts,
        next_counts=next_counts,
        max_len=5
    )

    assert len(out) <= 5
