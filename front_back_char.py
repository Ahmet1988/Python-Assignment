def front_back(word):
    if len(word) <= 1 :
      return word
    else :
      return word[-1] + word[1:len(word)-1] + word[0]
