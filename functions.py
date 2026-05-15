# How can create a function thats adds up two numbers
''' def add (a,b,c):# yaha a,b kyaa hai parameter 
   print(a+b+c)

add(10,20)

'''
# problems is waht if hume hi nahi pata ki kitne parameter hone wale hai
# solutions = using args

# args -> *variable_name
# variable_name -> chacha ,mama ,kessa bhi likh skte ha 
# args value ko accept krte ha in the form tuple



'''
def add (*chacha):
    print(type(chacha))
    print(chacha)

add(10,20,30,40,50)
'''

# def polio (name,age,pin,contact):
#     print(name,age,pin,contact)
# polio(name = 'Ramesh',age = 22,pin=1222,contact =0000000,
#       grandfather ='lala')

'''
kwargs -> keyword argument
denote -> **variable_name -> Ramesh ,chacha ,doremon ,bahubali
kwargs -> accepts krte ha sari value ko in the form of dicitionary
parameter woh -> keys
Arguments -> values 

'''
# def polio (**variable):
#     print(type(variable))
#     print(variable)
# polio (name = "suresh ",age = 21 ,school= 'dps')    

'''
def polio (**a):

    for i in a:
        print(f"parameter -> {i} and arguments -> {a[i]}")
        # i -> dict keys , a [i] -> unn keys ki values
polio (name = "suresh ",age = 21 ,school= 'dps')    
'''

