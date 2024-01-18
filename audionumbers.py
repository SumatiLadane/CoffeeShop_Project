from playsound import playsound


def numberToWord(num):

    arr = ['zero', 'one','two','three','four','five','six','seven','eight','nine']
    arr2 = ['Zero','ten','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety']
    arr3 = ['zero','one hundred','two hundred','three hundred','four hundred','five hundred','six hundred','seven hundred','eight hundred','nine hundred']
    arr4 = ['zero','eleven','twelve','thirteen','foourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    word = ""
    num = str(num)
    
    if len(num) == 1:
        ones = int(num)
        word = arr[ones]
        
    elif len(num) == 2:
        ones = int(num[0])
        tens = int(num[1])
        if tens == 0:
            word = arr2[ones]
        elif ones == 1 and tens>=1 and tens<=9:
            word = arr4[tens] 
        else:  
            word = arr2[ones]+" "+arr[tens]
      
    elif len(num) == 3:
        ones = int(num[0])
        tens  = int(num[1])
        centurys = int(num[2])
        if ones!=0 and tens == 0 and centurys == 0:
            word = arr3[ones]  
        elif ones!=0 and tens!=0 and centurys == 0:
            word = arr3[ones] +" "+ arr2[tens] 
        elif ones!=0 and tens == 0 and centurys !=0:
            word =  arr3[ones] +" "+ arr[centurys]       
        elif ones>=1 and ones<=9 and tens==1 and centurys>=1 and centurys<=9:
            word = arr3[ones] +" "+ arr4[centurys]       
           
        else:
            word = arr3[ones] +" "+ arr2[tens] +" "+arr[centurys]
    return word        

def wordToVoice(word):

    words = word.split(" ")
    
    for w in words:
        path = "audionumbers/audio/"+ w + ".wav"
        n = playsound(path)
    return n    


def numberToVoice(n):
    
    wordToVoice(numberToWord(n)) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # wordToVoice(numberToWord())




# wordToVoice(numberToWord(234))


# for num in range(801,999):
#     re = numberToWord(num)
#     print(re)

