flag = 0
a='201811123012'

file = open(r'./log_files/201811123012.log',encoding='utf-8')
line =file.readline()
while line:
    if a in line:
        flag=flag+1
    line = file.readline()
file.close()
print(a)
print("出现次数为")
print(flag)

