def decorator(funcToDec):
    def wrapper(): #obertka
        #before 
        print ('Func')
        print (funcToDec(),'\n')
        #after
        print ('Decorator_func')
        buf = [x for x in funcToDec() if x != '']
        print (buf,'\n')
    return wrapper()

@decorator #cintaksis dekoratora
def get_pages():
    return ['chapter1', '', 'contents', '', 'line1']
