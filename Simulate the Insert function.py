lst = [1,2,3,'a',4,'b',5] #sample list

value = input('''list = [1,2,3,a,4,b,5]
Enter a value from the list : ''')

for i in range (len(lst)) :
       
    if str(lst[i]) == str(value) :
        
        print('Index of selected value is ',i)
