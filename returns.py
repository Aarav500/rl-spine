def discounted_return(rewards, gamma):
  """rewards[0] + gamma*rewards[1] + gamma**2*rewards[2] + ...  (Zhao L1 P2; B&H A.8.2)"""
  # your body: a loop like B01, then return G
  G = 0.0
  for k in range(len(rewards)):
    G = G + (gamma**k) * rewards[k]
  return G

if __name__ == "__main__":
    print(discounted_return([0, 1], 0.9))                               # expect 0.9
    print(discounted_return([1] * 50, 0.9), (1 - 0.9**50) / (1 - 0.9))  # oracle: the two numbers must agree
    print(discounted_return([2, 2, 2], 1.0))                            # gamma = 1 is a plain sum: 6
    print(discounted_return([], 0.9))                                   # no rewards: 0
