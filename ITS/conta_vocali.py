def contavocali():
    vocali=0
    parola=input("Scrivi una parola e ne verranno contate le vocali: ")
    for i in parola:
        if (i in ("a", "e", "i", "o", "u")):
            
            vocali += 1
    print(f"{vocali}")

contavocali()
    
  
