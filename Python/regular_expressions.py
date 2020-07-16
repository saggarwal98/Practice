import re
str1='hel'
str2='hello'
str3='h1'
print(re.match(str1,str2))
print(re.match(str3,str2))
print(re.match(str1,str2*2))
print(re.search(str1,str2*2))
email_string="abc@xyz.com"
match=re.search('([\w]+)@([\w]+).([\w]+)',email_string)
print(match.group())
print(match.group(1))
print(match.group(2))
print(match.group(3))