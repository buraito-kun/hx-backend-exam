vowels = ["a", "e", "i", "o", "u"]

def count_vowel_clusters(word: str) -> None:
  count = 0
  is_prev_vowel = False

  for i in range(len(word)):
    if word[i] in vowels:
      if is_prev_vowel == False:
        count += 1
      is_prev_vowel = True
    else:
      is_prev_vowel = False
  print(count)

if __name__ == "__main__":
  count_vowel_clusters("beautiful")
  # count_vowel_clusters("architectures")
  # count_vowel_clusters("applications")
  # count_vowel_clusters("main")
  # count_vowel_clusters("experience")
