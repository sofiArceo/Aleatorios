from nacl.utils import random
import nacl.encoding
import nacl.hash

message = "Arbitrary data to hash"
message_len = len(message)

size = 128
buf = nacl.utils.random(size)
print(size)
for char in buf:
    print (char.encode('hex')),
print("\n")
print("hash message: ")
hash = nacl.hash.sha256(message, encoder=nacl.encoding.HexEncoder)
print(hash)