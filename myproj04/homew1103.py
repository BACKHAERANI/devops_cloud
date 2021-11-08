

#number = 3
for number in range(3, 10, 3):
    for i in range(1, 10):
        print(f"{number}*{1}={number*i}")





for i in range(1, 100):
    #if i %3== 0 and i%5 ==0:
    if i % 15 ==0:
        print(i)        


for i in range(15, 100, 15):
    print(i) 



number_list=[]

for i in range(1, 100):
    for i %3 == 0 and i % 5 == 0:
        number_list.apped(i)

print(sum(number_list))




for number in range(2, 10):
    for i in range(1, number+1):
        #if number >= i:
            print(f"{number}*{1}={number*i}")