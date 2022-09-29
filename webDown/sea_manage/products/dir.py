import os
list = []
arr = 'S1A_EW_GRDM_1SSH_20220209T063445_20220209T063545_041832_04FAD2_C3F9.zip'
# arr = 'S1A_EW_GRDM_1SSH_20220209T063345_20220209T063445_041832_04FAD2_6738.zip,S1A_EW_GRDM_1SSH_20220209T063445_20220209T063545_041832_04FAD2_C3F9.zip'
name =  arr.split(',')
print(name)
down_path = 'D:\\dataSource\\webDown\\'
for root, dirs, files in os.walk(down_path):
    for file in files:
        for i in range(len(name)):
            if file == name[i]:
                load = down_path + '\\' + name[i]
                list.append(load)
                name.pop(i)


print(list)
print(name)