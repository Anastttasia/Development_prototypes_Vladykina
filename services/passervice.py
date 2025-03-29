from hashlib import md5, sha256, sha3_512
from passlib.hash import pbkdf2_sha256

slat = "netology"
pas = "12345" + slat

# hash_md5 = md5(pas.encode()).hexdigest()
hash_sha256 = sha256(pas.encode()).hexdigest()
# hash_sha3512 = sha3_512(pas.encode()).hexdigest()

hash_pbk = pbkdf2_sha256.hash(pas)

my_hash = "$pbkdf2-sha256$29000$hjBGCAFAyLm3tnbuXev9nw$pYNl1BYWe0ZhDH1W.BRd/DGVLmb0aDdo2M0.KQ0laO1"
my_hash2 = "$pbkdf2-sha256$29000$eI8x5jxnTCkFwBjDuBfinA$hTpqWQzKIQVAqmJZVQsj6Pygcr3qOJ3dt6tXLyUjIKA"
# print(hash_md5)
print(hash_sha256)
print(hash_pbk)
print(pbkdf2_sha256.verify(pas, my_hash2))

# print(hash_sha3512)