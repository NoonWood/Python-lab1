def extra_enumerate(someArray, start):
    st = start
    cum = 0
    for elem in someArray:   
        yield st, elem  #vozvrashaet generator
        st += 1
        cum = cum + elem
        print('(',st,', ',elem,', ',cum,', ',cum*0.1,')')


x  = [1,3,4,2] 
print ('(id,num,sum,10%)')
for i in extra_enumerate(x,0):
    print() 
