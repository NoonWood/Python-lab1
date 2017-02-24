def get_frames(signal,size,overlap):
    
    print ('Step: ')
    x = signal
    step = size * overlap
    print (step)
    i = 0
    while i<len(signal):
        print (signal[i:i+size]) #ot 0 do stap, ot stap + size
        i = i + int(step)


size = 10     #razmer okna
signal = [i for i in range(0,1024)] #razer signala
overlap = 0.4 #stepen perekritia


get_frames(signal,size,overlap)
