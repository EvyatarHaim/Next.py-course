password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"

print("".join(chr(ord(char) + 2) if char.isalpha() else char for char in password))
