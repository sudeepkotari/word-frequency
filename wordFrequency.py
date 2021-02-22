fname = input("enter the filename: ")
try:
   file = open(fname)
   d1 = dict()
   for line in file:
       words = line.split()
       for word in words:
        #d1[word] = d1[word] + 1  
        if word in d1:
            d1[word] = d1.get(word,0) + 1 
        else:
            d1[word] =1
   print(d1)
    
except:
     print("file not found to display")
