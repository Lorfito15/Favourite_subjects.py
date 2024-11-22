asignaturas_validas = ["Fundamentals of Programming", "Fundamentals of Computers", "Discrete Mathematics", "Professional Skills for Engineers", "Algebra and Geometry"]

# Initialize a dictionary to store favorite subjects
asignaturas = {}

# Function to add a student and their favorite subject
def agregar_alumno(nombre, asignatura):
    if asignatura in asignaturas:
        asignaturas[asignatura].append(nombre)
    else:
        asignaturas[asignatura] = [nombre]

# Function to calculate the percentage of each subject
def calcular_porcentajes(total_alumnos):
    return {asignatura: (len(alumnos) / total_alumnos) * 100 for asignatura, alumnos in asignaturas.items()}

# Input data
total_alumnos = int(input("Enter the total number of students: "))

for _ in range(total_alumnos):
    nombre = input("Enter the student's name: ")
    
    # Validate the subject
    while True:
        asignatura = input("Enter the student's favorite subject: ")
        if asignatura in asignaturas_validas:
            break
        else:
            print("Invalid subject. Please choose one of the following:")
            print(", ".join(asignaturas_validas))  # Show valid subjects

    agregar_alumno(nombre, asignatura)

# Calculate and display the percentages
porcentajes = calcular_porcentajes(total_alumnos)

print("\nPercentage of students who prefer each subject:")
for asignatura, porcentaje in porcentajes.items():
    barra = '█' * int(porcentaje // 2)  # Each block represents 2%
    print(f"{asignatura}: {porcentaje:.2f}% [{barra:<50}]")  # Adjust the width of the bar
