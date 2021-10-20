# フロイドの循環検出法

import hashlib


def sha40(x: str):
    return hashlib.sha256(x.encode('utf-8')).hexdigest()[0:10]      # rubyとはスライスのしようが違うので注意


def rho(h0):
    kame, usagi = h0, h0
    while True:
        kame = sha40(kame)                  # single hashの系列
        usagi = sha40(sha40(usagi))         # double hashの系列
        if kame == usagi:                   # loop の合流
            break
    goryu = kame                            # 合流地点を記憶
    kame = h0
    while True:
        kame_p,goryu_p = kame,goryu           # 直前のデータ（ハッシュ値の原像）を記憶
        kame = sha40(kame)                    # h0から再スタートする系列
        goryu = sha40(goryu)                  # 合流地点からスタートする系列
        if kame == goryu:                     # ハッシュ値が一致
            break
    return [kame_p, goryu_p]                  # ハッシュ値の原像ペアを出力


pair = rho("0000000000")
print(f"原像ペア: {[pair[0], pair[1]]}")
print(f"ハッシュ値: {[sha40(pair[0]),sha40(pair[1])]}")