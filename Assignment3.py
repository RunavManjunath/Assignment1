numbers=(1,2,3,4,5,6,7,8,9)
Count_odd=0
Count_even=0
for x in numbers:
    if not x %2:
        Count_odd+=1
    else:
        Count_even+=1
Print("number of odd number :",Count_odd)
Print("number of odd number :",Count_even)
