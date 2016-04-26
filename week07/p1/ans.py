def CaeserCipher(s, k):
  L = []
  for i in range(0, len(s)):
    if ord(s[i]) >= ord("a") and ord(s[i]) <= ord("z"):
      temp = ord(s[i]) - ord("a")
      x = (temp + k) % 26
      x = x + ord("a")
      L.append(chr(x))
    elif ord(s[i]) >= ord("A") and ord(s[i]) <= ord("Z"):
      temp = ord(s[i]) - ord("A")
      x = (temp + k) %26
      x = x + ord("A")
      L.append(chr(x))
    else:
      L.append(s[i])
  return ''.join(L)

# main program

s = input('Enter text to encrypt : ')
key = int(input('Enter key value : '))
print('Encrypted result : ', CaeserCipher(s, key))
