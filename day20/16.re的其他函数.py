# writer:enjoyiii
# 2026年05月29日20时50分26秒
# @163.com
import re
#search只能查找一次
ret = re.search(r"\d+","阅读次数为 9999，点赞777")
print(ret.group())
#findall可以查找多次
ret = re.findall(r"\d+","python=9999，c=7890，c++=12345")
print(ret)

def find_second_match(pattern,text):
    matches = re.finditer(pattern, text)
    try:
        next(matches)#跳过第一个匹配项second_match=next(matches)#获取第二个匹配项return
        second_match=next(matches)
        return second_match.group()
    except StopIteration:
        return None
# 示例用法
text="abc123def456ghi789"
pattern = r"\d+"
second_match = find_second_match(pattern,text)
print(second_match)

print("-----------------")
ret=re.sub(r"\d+",'998',"阅读次数777")
print(ret)

print("-----------------")
def add(a):
    num=a.group ()
    return str(int(num)+2)

ret=re.sub(r"\d+",add,"阅读次数777")
print(ret)

ret=re.sub(r"\d+",lambda a:str(int(a.group())+1),"阅读次数777")
print(ret)
print("-----------------")

text = "apple apple apple apple"
pattern = r"apple"
replacement = "orange"
new_text = re.sub(pattern,replacement,text,count=2)
print(new_text)

print("-----------------")

s='hello world,now is 2020/7/20 18:48，现在是2020年7月20日18时48分。'
ret_s=re.sub(r'年|月',r'/',s)
ret_s =re.sub(r'日',r' ',ret_s)
ret_s = re.sub(r'时|分',r':',ret_s)
print (ret_s)
# findall 有问题
com = re.compile(r'\d{4}/[01]?[0-9]/[1-3]?[0-9]\s(?:0[0-9]|1[0-9]|2[0-4])\:[0-5][0-9]')#一定要加？：表示非捕获组，这样才不会在findall中只返回小时
ret = com.findall(ret_s)
print (ret)