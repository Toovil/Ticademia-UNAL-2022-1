tarifa = int(input())

horas = int(input())

if(horas <= 45):
    nomina = tarifa * horas
else:
    h_extra = (tarifa * (horas-45)) * 0.5
    nomina = (tarifa * horas) + h_extra

print(f"$ {int(nomina)}")