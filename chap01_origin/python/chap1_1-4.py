import hashlib


# chap1_1
print("")
print("===== chap1_1 ====")

def get_hash_sha256(str):
    # encode
    str = str.encode('UTF-8')
    # hashing
    hash = hashlib.sha256(str).hexdigest()
    return hash

print("12345: " + get_hash_sha256("12345"))
print("12346: " + get_hash_sha256("12346"))



# chap1_2
print("")
print("===== chap1_2 ====")

IV = "0000"
data_list = ["0001", "0002", "0003", "0004"]

def hashchain(_data_list, _prevhash):
    chained_list = []

    for data in _data_list:
        block = f"{data}:{_prevhash}"
        chained_list.append(block)
        _prevhash = hashlib.sha256(block.encode('utf-8')).hexdigest()

    return chained_list

blockchain = hashchain(data_list, IV)
print(f"Blockchain: {blockchain}")

lasthash = hashlib.sha256(blockchain[-1].encode('utf-8')).hexdigest()
print(f"LastHash: {lasthash}")



# chap1_3
print("")
print("===== chap1_3 ====")

def verifyhashchain(_hashchain, _prevhash, _lasthash):
    for block in _hashchain:
        hash = block.split(":")[1]
        if hash == _prevhash:
            _prevhash = hashlib.sha256(block.encode('utf-8')).hexdigest()
        else:
            return False

    if _prevhash == _lasthash:
        return True
    else:
        return False

print(verifyhashchain(blockchain, IV, lasthash))



# chap1_4
print("")
print("===== chap1_4 ====")

import random
import time

def hashcash(target):
    hash = 0
    pow = ""
    size = 2**256
    while True:
        pow = str(random.randint(0,size))
        hash = int(hashlib.sha256(pow.encode('utf-8')).hexdigest(), 16)
        if hash < target:
            break
    return [pow, hash]

def hashcashTime(target):
    t0 = time.time()
    hashcash(target)
    return time.time() - t0

print(f"2**240: {hashcashTime(2**240)}")
print(f"2**239: {hashcashTime(2**239)}")
print(f"2**238: {hashcashTime(2**238)}")
print(f"2**237: {hashcashTime(2**237)}")
print(f"2**236: {hashcashTime(2**236)}")
print(f"2**235: {hashcashTime(2**235)}")