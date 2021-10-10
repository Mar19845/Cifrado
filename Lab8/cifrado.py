from hashlib import blake2b

h = blake2b(key=b'pseudorandom key', digest_size=16)
h.update(b'message data')
print(h.hexdigest())