require 'digest'


# chap1_1
puts ""
puts "===== chap1_1 ===="

def get_hash_sha56(str)
    Digest::SHA256.hexdigest(str)
end

puts "12345: #{get_hash_sha56("12345")}"
puts "12346: #{get_hash_sha56("12346")}"



# chap1_2
puts ""
puts "===== chap1_2 ===="

IV = "0000"
data_list = ["0001","0002","0003","0004"]

def hashchain(_data_list, _prevhash)
    chained_list = []

    for data in _data_list
        block = "#{data}:#{_prevhash}"
        chained_list << block
        _prevhash = Digest::SHA256.hexdigest(block)
    end

    chained_list
end

blockchain = hashchain(data_list,IV)
puts "Blockchain: #{blockchain}"

lasthash = Digest::SHA256.hexdigest(blockchain[-1])
puts "LashHash: #{lasthash}"



# chap1_3
puts ""
puts "===== chap1_3 ===="

def verifyhashchain(_hashchain, _prevhash, _lasthash)
    for block in _hashchain
        hash = block.split(":")[1]
        if hash == _prevhash
            _prevhash = Digest::SHA256.hexdigest(block)
        else
            false
        end
    end
    if _prevhash == _lasthash
        true
    else
        false
    end
end

puts verifyhashchain(blockchain, IV, lasthash)



# chap1_4
puts ""
puts "===== chap1_4 ===="

def hashcash(target)
    hash = 0
    pow = ""
    size = 2**256
    begin
        pow = rand(size).to_s
        hash = Digest::SHA256.hexdigest(pow).to_i(16)
    end until hash < target
    return [pow, hash]
end

def hashcashTime(target)
    t0 = Time.now
    hashcash(target)
    Time.now - t0
end
puts "2**240: #{hashcashTime(2**240)}"
puts "2**239: #{hashcashTime(2**239)}"
puts "2**238: #{hashcashTime(2**238)}"
puts "2**237: #{hashcashTime(2**237)}"
puts "2**236: #{hashcashTime(2**236)}"
puts "2**235: #{hashcashTime(2**235)}"