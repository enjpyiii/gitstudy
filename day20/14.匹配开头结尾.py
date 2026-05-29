# writer:enjoyiii
# 2026年05月29日20时05分28秒
# @163.com
import re

email_list =["xiaoWang@163.com","xiaoWang@163.comheihei",".com.xiaowang@qq.com"]
for email in email_list:
    ret = re.match(r"[\w]{4,20}@163\.com$",email)
    if ret:
        print("%s 是符合规定的邮件地址,匹配后的结果是:%s"%(email,ret.group()))
    else:
        print("%s 不符合要求"% email)