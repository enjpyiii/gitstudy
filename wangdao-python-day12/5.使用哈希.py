# writer:enjoyiii
# 2025年05月26日17时46分34秒
# 1663472473@qq.com
class Hash:
    def __init__(self, hash_table_size):
        self.hash_table = [None]*hash_table_size
        self.hash_table_size = hash_table_size

    def elf_hash(self, hash_str):
        h = 0
        g = 0
        for i in hash_str:
            h = (h << 4) + ord(i)
            g = h & 0xf0000000
            if g:
                h ^= g >> 24
            h &= ~g
        return h % self.hash_table_size


if __name__ == '__main__':
    import random
    str_list = ['enjoyiii', 'lele', 'hanmeimei', 'wangdao', 'fenghua']
    temp_dict = {}
    stu_list = []
    for i in str_list:
        temp_dict.clear()
        temp_dict['name']=i
        temp_dict['age']=random.randint(1,100)
        stu_list.append(temp_dict.copy())
    print(stu_list)
    ha=Hash(1000)
    for i in stu_list:
        index=ha.elf_hash(i['name'])
        print(index)
        if ha.hash_table[index]==None:
            ha.hash_table[index]=[i]
        else:
            # print('存在哈希冲突')
            ha.hash_table[index].append(i)
    # print(ha.hash_table)#哈希表中存的字典
    stu_name=input('请输入要查找的姓名：')
    index=ha.elf_hash(stu_name)
    if ha.hash_table[index]==None:
        print('没有该学生')
    else:
        for i in ha.hash_table[index]:
            if i['name']==stu_name:
                print(i)
                break
        else:
            print('没有该学生')