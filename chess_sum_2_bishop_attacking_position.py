def bishop_attacking_r_not(lst):
        dict={}
        count=0
        for i in lst:
            count+=1
            if "B" in i:
                dict[count]=i.find("B")+1
        print("position of bishopes",dict,"\n")        
        start_row,start_col=min(zip(dict.keys(),dict.values()))[0],min(zip(dict.keys(),dict.values()))[1]  #1st bishop position are taken as string
        end_row,end_col=max(zip(dict.keys(),dict.values()))[0],max(zip(dict.keys(),dict.values()))[1]      #2nd bishop position 
        end_str=str(end_row)+str(end_col)                       
        sum_lst=[]
        start_roww=start_row
        start_coll=start_col
        start_roww1=start_row
        start_coll1=start_col

        #(+) point_values

        while start_roww<=end_row-1 and start_coll<=7:
            start_roww+=1
            start_coll+=1
            sum_lst.append(str(start_roww)+str(start_coll))    

        #(-) point_values

        dif_lst=[]
        while start_coll1>1:
            start_roww1+=1
            start_coll1-=1
            dif_lst.append(str(start_roww1)+str(start_coll1))

        sum_lst=sum_lst+dif_lst    
        print("attacking area of 1st bishop",sum_lst,"\n") 

        if end_str in sum_lst or end_str in dif_lst:
            return "yes the two bishop are in attacking position \n"
        else:
            return "no the two bishop aren't in attacking position \n"


n=int(input())
lst=[]
for j in range(n):
    for i in range(8):
        st=input()
        lst.append(st)
    print(bishop_attacking_r_not(lst))  

#input in the form following type"
#the position of bishop is denote by 'B'
#so,
'''****B***
   ********
   ********
   ********
   ******B*
   ********
   ********
   ********'''


        
