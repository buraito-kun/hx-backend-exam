def all_possible_permutation(word: str, parent: str = "") -> None:
  if len(word) == 1:
    print(parent + word)
  else:
    for i in range(len(word)):
      all_possible_permutation(word[:i] + word[i+1:], parent + word[i])

if __name__ == "__main__":
  all_possible_permutation("ABC")
  # all_possible_permutation("HELO")
