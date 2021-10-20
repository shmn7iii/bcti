# RSA暗号

# 拡張ユークリッド互除法
def egcd(a,b)
    if a%b==0
        return [0,1,b]
    else
        xp, yp, gcd = egcd(b, a%b)
        return [yp,xp-(a/b)*yp,gcd]
    end
end

# 素数生成
require 'securerandom'
def ftPrime(size)
    n = 0
    begin
        n = SecureRandom.random_number(2**size)
        a = rand(2**size)
        b = rand(2**size)
    end until n%2 !=0 && n%3 !=0 && egcd(a,n)[2]==1 && egcd(b,n)[2]==1 && powmod(a,(n-1),n)==1 && powmod(b,(n-1),n)==1
    return n
end

# べき剰余計算
# @param a 暗号文
# @param e 秘密鍵
# @param m 公開鍵
def powmod(a,e,m)
    (e.bit_length-2).downto(0).reduce(a) do |x,i|
        if e[i] == 0
            x = (x*x)%m
        else
            x = (((x*x)%m)*a)%m
        end
    end
end

# 鍵生成 （2048bit）
p,q= [ftPrime(1024), ftPrime(1024)]
n = p*q                     # 公開鍵 n
e = 65537                   # 公開鍵 e
fai = (p-1)*(q-1)
d = egcd(e,fai)[0]%fai      # 秘密鍵 d

puts "公開鍵n: #{n}"
puts "公開鍵e: #{e}"
puts "秘密d: #{d}"

# 平文メッセージ
m = 12345678987654321
puts "平文: #{m}"

# 暗号化
c = powmod(m,e,n)
puts "暗号文: #{c}"

# 復号化
dm = powmod(c,d,n)
puts "復号化: #{dm}"