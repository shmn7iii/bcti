# フロイドの循環検出法

require 'digest'


def sha40(x)
    Digest::SHA256.hexdigest(x)[0..9]
end


def rho(h0)
    kame,usagi=h0,h0
    begin
        kame=sha40(kame)                # single hashの系列
        usagi=sha40(sha40(usagi))       # double hashの系列
    end until kame==usagi               # loop の合流
    goryu=kame                          # 合流地点を記憶
    kame=h0
    begin
        kame_p,goryu_p=kame,goryu       # 直前のデータ（ハッシュ値の原像）を記憶
        kame=sha40(kame)                # h0から再スタートする系列
        goryu=sha40(goryu)              # 合流地点からスタートする系列
    end until kame==goryu               # ハッシュ値が一致
    return [kame_p,goryu_p]             # ハッシュ値の原像ペアを出力
end


pair=rho("0000000000")
puts "原像ペア: #{[pair[0], pair[1]]}"
puts "ハッシュ値: #{[sha40(pair[0]),sha40(pair[1])]}"
