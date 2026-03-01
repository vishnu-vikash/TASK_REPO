my_list =[[1,2,3],[1,2,3,4],("vishnu","vikash")]
print(my_list[2][1])# direct printing
for i in range(len(my_list)): #loop complex printing --  2 loops i=0 and i=1
    if(i==2):
        for j in range(len(my_list[i])):
            if(my_list[i][j]=="vikash"):
                print(my_list[i][j])
                break
            else:
                continue
    else:
        continue