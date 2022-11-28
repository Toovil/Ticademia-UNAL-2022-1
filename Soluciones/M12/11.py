N = int(input())
D = {0:'Hasta luego curso! Turing, puedes estar orgulloso de mi',
            1:'Goodbye course! Turing, you can be proud of me',
            2:'Au revoir cours! Turing, tu peux etre fier de moi',
            3:'Adeus, curso! Turing, pode se orgulhar de mim',
            4:'Auf Wiedersehen! Turing, du kannst stolz auf mich sein'}
n = 6
while N > 4:
    print(D[N % (n-1)])
    N //= n -1