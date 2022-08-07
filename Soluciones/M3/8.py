"""
Si consideramos la calificación como un porcentaje entre 0% y 100%, la equivalencia con
la escala norteamericana (aunque otros países también la adoptan) es la siguiente:
'A' significa mayor o igual a 90
'B' significa mayor o igual a 80, pero menor a 90
'C' significa mayor o igual a 70, pero menor a 80
'D' significa mayor o igual a 60, pero menor a 70
'E' significa mayor o igual a 40, pero menor a 60
'F' significa menor a 40


Debes escribir un programa para determinar, dada una calificación expresada en
porcentaje, su correspondencia en esta escala.


!Entrada:
?La entrada contiene una única línea con un valor real X correspondiente al porcentaje.

!Salida:
?Una única línea con el mensaje (sin comillas ni puntuación): 'El porcentaje X corresponde
?a la calificacion Y'.

"""
grade = float(input())


if(grade >= 90):
    print(f'El porcentaje {str(grade)} corresponde a la calificacion A')
elif(grade >= 80 and grade < 90):
    print(f'El porcentaje {str(grade)} corresponde a la calificacion B')
elif(grade >= 70 and grade < 80):
    print(f'El porcentaje {str(grade)} corresponde a la calificacion C')
elif(grade >= 60 and grade < 70):
    print(f'El porcentaje {str(grade)} corresponde a la calificacion D')
elif(grade >= 40 and grade < 60):
    print(f'El porcentaje {str(grade)} corresponde a la calificacion E')
else:
    print(f'El porcentaje {str(grade)} corresponde a la calificacion F')    