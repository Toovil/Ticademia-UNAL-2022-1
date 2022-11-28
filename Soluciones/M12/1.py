cantidad = int(input())
for i in range (cantidad):
    num=input()
    input_ = num.replace(' ','').split(':')
    guide=[]
    axis = []
    axis[:] = input_[1]
    guide[:]=input_[0]
    
    if len(guide)==len(axis):
         for i in axis:
             if guide.count(i) != axis.count(i):
                 print('No es anagrama')
                 anagram = False
                 break
             if i in input_[0]:
                 anagram = True
             else:
                 print('No es anagrama')
                 anagram = False
                 break
         if anagram == True:
             print('Es anagrama')
    else:
        print('No es anagrama')
