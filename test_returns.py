import pytest
from returns import discounted_return


def test_empty_is_zero():
    assert discounted_return([], 0.9) == 0


def test_two_steps():
    assert discounted_return([0, 1], 0.9) == pytest.approx(0.9)


# your two tests:
# test_constant_reward_matches_formula: 30 rewards of 1 at gamma = 0.95 against the A.8.2 formula, with pytest.approx
def test_constant_reward_matches_formula():
    rewards = 30 * [1]       # 30 rewards of 1 (the list trick from B01)
    gamma = 0.95
    expected =  (1 - gamma**30) / (1 - gamma)   # A.8.2: (1 - gamma**30) / (1 - gamma)
    assert discounted_return(rewards, gamma) == pytest.approx(expected)
# test_gamma_one_is_plain_sum: gamma = 1.0, rewards [3, -1, 2] gives 4
def test_gamma_one_is_plain_sum():
   rewards =  [3, -1, 2]
   gamma = 1.0
   expected = 4
   assert discounted_return(rewards, gamma) == pytest.approx(expected)