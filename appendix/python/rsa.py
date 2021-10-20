# RSA暗号

# 拡張ユークリッド互除法
def egcd(a,b):
    if a%b == 0:
        return [0,1,b]
    else:
        xp, yp, gcd = egcd(b, a%b)
        return [yp,xp-(a//b)*yp,gcd]


# 素数生成
import secrets
import random

def ftPrime(size):
    n = 0
    while True:
        n = secrets.randbelow(2**size)
        a = random.randint(0, 2**size)
        b = random.randint(0, 2**size)
        if n%2 !=0 and n%3 !=0 and egcd(a,n)[2]==1 and egcd(b,n)[2]==1 and powmod(a,(n-1),n)==1 and powmod(b,(n-1),n)==1:
            break
    return n


# べき剰余計算
# @param a 暗号文
# @param e 秘密鍵
# @param m 公開鍵
def powmod(a,e,m):
    # (e.bit_length-2).downto(0).reduce(a) do |x,i|
    x = a
    for i in range(e.bit_length()-2, -1, -1):
        if not e & (1 << i):
            x = (x*x)%m
        else:
            x = (((x*x)%m)*a)%m
    return x


# 鍵生成 （2048bit）
p,q= [ftPrime(1024), ftPrime(1024)]
n = p*q                     # 公開鍵 n
e = 65537                   # 公開鍵 e
fai = (p-1)*(q-1)
d = egcd(e,fai)[0]%fai      # 秘密鍵 d

print(f"公開鍵n: {n}")
print(f"公開鍵e: {e}")
print(f"秘密d: {d}")

# 平文メッセージ
m = 12345678987654321
print(f"平文: {m}")

# 暗号化
c = powmod(m,e,n)
print(f"暗号文: {c}")

# 復号化
dm = powmod(c,d,n)
print(f"復号化: {dm}")