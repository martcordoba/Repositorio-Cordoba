import random
estudiantes= 5
materias= 5
matriz5x5= []
for fil in range(estudiantes):
    matriz5x5.append([])
    for col in range(materias):
        matriz5x5[fil].append(random.randint(1,10))

for i in range(5):
    matriz5x5[i][0]="estudiante"

matriz5x5[0][0]=""
matriz5x5[0][1]="Matematica"
matriz5x5[0][2]="Lengua"
matriz5x5[0][3]="Quimica"
matriz5x5[0][4]="Historia"

for i in range (5):
    print (matriz5x5[i])

for i in range(4):
    num=matriz5x5[i+1][1]+matriz5x5[i+1][2]+matriz5x5[i+1][3]+matriz5x5[i+1][4]
    print("El promedio es ", num/4)
    