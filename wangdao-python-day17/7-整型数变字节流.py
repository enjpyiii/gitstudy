# writer:enjoyiii
# 2026年05月15日23时02分35秒
# 15211281589@163.com
import struct

temp_byte=struct.pack('i',12345)
print(temp_byte)#有ascii码

temp_int=struct.unpack('ii',temp_byte+temp_byte)#一次性可以解析多个字节流
print(temp_int)