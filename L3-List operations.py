print("121901313006","Rohit Bharadwaj Kadiyala")
choice=int(input("Enter a number for an operation on list:"))
if(choice==1):
    l1 = []  # creating a array
    n = int ( input ( "Enter array size:" ) )
    for i in range ( 0 , n ) :
        l1.append ( int ( input ( "Enter element:" ) ) )
    print ( "Original array:" , l1 )  # Original array
    l2 = [None] * len ( l1 )
    l = len ( l1 )
    for i in range ( 0 , l ) :
        l2[i] = l1[i]
    for i in range ( 0 , len ( l2 ) ) :
        print ( l2[i] )
    print ( "New array is" , l2 )  # new array
elif(choice==2):
    l1 = []  # creating a array
    n = int ( input ( "Enter array size:" ) )
    for i in range ( 0 , n ) :
        l1.append ( int ( input ( "Enter element:" ) ) )
    print ( "Original array:" , l1 )  # Original array
    res = []  # creating a new array
    for i in l1 :
        if i not in res :
            res.append ( i )
    print ( "New array is:" , res )  # Array without duplicate elements
elif(choice==3):
    l1 = []  # creating a array
    n = int ( input ( "Enter array size:" ) )
    for i in range ( 0 , n ) :
        l1.append ( int ( input ( "Enter element:" ) ) )
    print ( l1 )
    z = int ( input ( "Enter index of the elemnts to be removed:" ) )
    l1.pop ( z )
    print ( l1 )
elif(choice==4):
    x = 0
    def search(arr) :  # Fuction 1
        x = int ( input ( "Enter search element:" ) )
        for i in arr :
            if (x == i) :
                flag = 1
                break
            else :
                flag = 0
        if (flag == 1) :
            print ( "Search element" , x , "found in the array at" , i - 1 )
        else :
            print ( "Search element not found" )


    l1 = []  # creating an array
    n = int ( input ( "Enter array size:" ) )
    for i in range ( 0 , n ) :
        l1.append ( int ( input ( "Enter element:" ) ) )
    print ( "array:" , l1 )
    search ( l1 )  # function call
elif(choice==5):
    l1 = []  # creating an array
    n = int ( input ( "Enter array size:" ) )
    for i in range ( 0 , n ) :
        l1.append ( int ( input ( "Enter element:" ) ) )
    print ( "array:" , l1 )
else:
    print("!!!Please enter a correct choice!!!")





















