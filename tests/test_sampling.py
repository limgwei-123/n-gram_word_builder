import random
from ngram_gen.sample import sample_next_token

def test_temperature_zero_like_behavior():
  context = ("A",)
  next_counts = {
      (("A",), "x"): 100,
      (("A",), "y"): 1,
  }

  random.seed(0)
  out = sample_next_token(
      context,
      context_counts={},
      next_counts=next_counts,
      temperature=0.5
  )

  assert out == "x"

def test_top_k_restricts_candidates():
  context = ("A",)
  next_counts = {
      (("A",), "x"): 10,
      (("A",), "y"): 9,
      (("A",), "z"): 1,
  }

  random.seed(0)
  out = sample_next_token(
      context,
      {},
      next_counts,
      top_k=1
  )

  assert out == "x"

def test_top_p_keeps_high_prob_tokens():
  context = ("A",)
  next_counts = {
      (("A",), "x"): 90,
      (("A",), "y"): 9,
      (("A",), "z"): 1,
  }

  random.seed(0)
  out = sample_next_token(
      context,
      {},
      next_counts,
      top_p=0.9
  )

  assert out in {"x", "y"}

