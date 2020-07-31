import random
from tkinter import *
from tkinter import messagebox
import os

#---------Listas de nombres--------


nombres_hombre=['Daniel', 'David', 'Gabriel', 'Benjamín', 'Samuel', 'Lucas', 'Ángel', 'José', 'Adrián', 'Sebastián', 'Xavier', 'Juan', 'Luis', 'Diego', 'Óliver', 'Carlos', 'Jesús', 'Alex', 'Max', 'Alejandro', 'Antonio', 'Miguel', 'Víctor', 'Joel', 'Santiago', 'Elías', 'Iván', 'Óscar', 'Leonardo', 'Eduardo', 'Alan', 'Nicolás', 'Jorge', 'Omar', 'Paúl', 'Andrés', 'Julián', 'Josué', 'Román', 'Fernando', 'Javier', 'Abraham', 'Ricardo', 'Francisco', 'César', 'Mario', 'Manuel', 'Édgar', 'Alexis', 'Israel', 'Mateo', 'Héctor', 'Sergio', 'Emiliano', 'Simón', 'Rafael', 'Martín', 'Marco', 'Roberto', 'Pedro', 'Emanuel', 'Abel', 'Rubén', 'Fabián', 'Emilio', 'Joaquín', 'Marcos', 'Lorenzo', 'Armando', 'Adán', 'Raúl', 'Julio', 'Enrique', 'Gerardo', 'Pablo', 'Jaime', 'Saúl', 'Esteban', 'Gustavo', 'Rodrigo', 'Arturo', 'Mauricio', 'Orlando', 'Hugo', 'Salvador', 'Alfredo', 'Maximiliano', 'Ramón', 'Ernesto', 'Tobías', 'Abram', 'Noé', 'Guillermo', 'Ezequiel', 'Lucián', 'Alonzo', 'Felipe', 'Matías', 'Tomás', 'Jairo']     

nombres_mujer=['Isabella', 'Olivia', 'Alexis', 'Sofía', 'Victoria', 'Amelia', 'Alexa', 'Julia', 'Camila', 'Alexandra', 'Maya', 'Andrea', 'Ariana', 'María', 'Eva', 'Angelina', 'Valeria', 'Natalia', 'Isabel', 'Sara', 'Liliana', 'Adriana', 'Juliana', 'Gabriela', 'Daniela', 'Valentina', 'Lila', 'Vivian', 'Nora', 'Ángela', 'Elena', 'Clara', 'Eliana', 'Alana', 'Miranda', 'Amanda', 'Diana', 'Ana', 'Penélope', 'Aurora', 'Alexandría', 'Lola', 'Alicia', 'Amaya', 'Alexia', 'Jazmín', 'Mariana', 'Alina', 'Lucía', 'Fátima', 'Ximena', 'Laura', 'Cecilia', 'Alejandra', 'Esmeralda', 'Verónica', 'Daniella', 'Miriam', 'Carmen', 'Iris', 'Guadalupe', 'Selena', 'Fernanda', 'Angélica', 'Emilia', 'Lía', 'Tatiana', 'Mónica', 'Carolina', 'Jimena', 'Dulce', 'Talía', 'Estrella', 'Brenda', 'Lilian', 'Paola', 'Serena', 'Celeste', 'Viviana', 'Elisa', 'Melina', 'Gloria', 'Claudia', 'Sandra', 'Marisol', 'Asia', 'Ada', 'Rosa', 'Isabela', 'Regina', 'Elsa', 'Perla', 'Raquel', 'Virginia', 'Patricia', 'Linda', 'Marina', 'Leila', 'América', 'Mercedes']

apellidos=['González', 'Rodríguez', 'Gómez', 'Fernández', 'López', 'Díaz', 'Martínez', 'Pérez', 'García', 'Sánchez', 'Romero', 'Sosa', 'Álvarez', 'Torres', 'Ruiz', 'Ramírez', 'Flores', 'Acosta', 'Benítez', 'Medina', 'Suárez', 'Herrera', 'Aguirre', 'Pereyra', 'Gutiérrez', 'Giménez', 'Molina', 'Silva', 'Castro', 'Rojas', 'Ortíz', 'Núñez', 'Luna', 'Juárez', 'Cabrera', 'Ríos', 'Ferreyra', 'Godoy', 'Morales', 'Domínguez', 'Moreno', 'Peralta', 'Vega', 'Carrizo', 'Quiroga', 'Castillo', 'Ledesma', 'Muñoz', 'Ojeda', 'Ponce', 'Vera', 'Vázquez', 'Villalba', 'Cardozo', 'Navarro', 'Ramos', 'Arias', 'Coronel', 'Córdoba', 'Figueroa', 'Correa', 'Cáceres', 'Vargas', 'Maldonado', 'Mansilla', 'Farías', 'Rivero', 'Paz', 'Miranda', 'Roldán', 'Méndez', 'Lucero', 'Cruz', 'Hernández', 'Agüero', 'Páez', 'Blanco', 'Mendoza', 'Barrios', 'Escobar', 'Ávila', 'Soria', 'Leiva', 'Acuña', 'Martin', 'Maidana', 'Moyano', 'Campos', 'Olivera', 'Duarte', 'Soto', 'Franco', 'Bravo', 'Valdéz', 'Toledo', 'Andrada-Andrade', 'Montenegro', 'Leguizamón', 'Arce']

male_names= ['James', 'John', 'Robert', 'Michael', 'William', 'David', 'Richard', 'Joseph', 'Thomas', 'Charles', 'Christopher', 'Daniel', 'Matthew', 'Anthony', 'Donald', 'Mark', 'Paul', 'Steven', 'Andrew', 'Kenneth', 'Joshua', 'George', 'Kevin', 'Brian', 'Edward', 'Ronald', 'Timothy', 'Jason', 'Jeffrey', 'Ryan', 'Jacob', 'Gary', 'Nicholas', 'Eric', 'Stephen', 'Jonathan', 'Larry', 'Justin', 'Scott', 'Brandon', 'Frank', 'Benjamin', 'Gregory', 'Samuel', 'Raymond', 'Patrick', 'Alexander', 'Jack', 'Dennis', 'Jerry', 'Tyler', 'Aaron', 'Jose', 'Henry', 'Douglas', 'Adam', 'Peter', 'Nathan', 'Zachary', 'Walter', 'Kyle', 'Harold', 'Carl', 'Jeremy', 'Keith', 'Roger', 'Gerald', 'Ethan', 'Arthur', 'Terry', 'Christian', 'Sean', 'Lawrence', 'Austin', 'Joe', 'Noah', 'Jesse', 'Albert', 'Bryan', 'Billy', 'Bruce', 'Willie', 'Jordan', 'Dylan', 'Alan', 'Ralph', 'Gabriel', 'Roy', 'Juan', 'Wayne', 'Eugene', 'Logan', 'Randy', 'Louis', 'Russell', 'Vincent', 'Philip', 'Bobby', 'Johnny', 'Bradley']

female_names=['Mary', 'Patricia', 'Jennifer', 'Linda', 'Elizabeth', 'Barbara', 'Susan', 'Jessica', 'Sarah', 'Karen', 'Nancy', 'Margaret', 'Lisa', 'Betty', 'Dorothy', 'Sandra', 'Ashley', 'Kimberly', 'Donna', 'Emily', 'Michelle', 'Carol', 'Amanda', 'Melissa', 'Deborah', 'Stephanie', 'Rebecca', 'Laura', 'Sharon', 'Cynthia', 'Kathleen', 'Helen', 'Amy', 'Shirley', 'Angela', 'Anna', 'Brenda', 'Pamela', 'Nicole', 'Ruth', 'Katherine', 'Samantha', 'Christine', 'Emma', 'Catherine', 'Debra', 'Virginia', 'Rachel', 'Carolyn', 'Janet', 'Maria', 'Heather', 'Diane', 'Julie', 'Joyce', 'Victoria', 'Kelly', 'Christina', 'Joan', 'Evelyn', 'Lauren', 'Judith', 'Olivia', 'Frances', 'Martha', 'Cheryl', 'Megan', 'Andrea', 'Hannah', 'Jacqueline', 'Ann', 'Jean', 'Alice', 'Kathryn', 'Gloria', 'Teresa', 'Doris', 'Sara', 'Janice', 'Julia', 'Marie', 'Madison', 'Grace', 'Judy', 'Theresa', 'Beverly', 'Denise', 'Marilyn', 'Amber', 'Danielle', 'Abigail', 'Brittany', 'Rose', 'Diana', 'Natalie', 'Sophia', 'Alexis', 'Lori', 'Kayla', 'Jane']

family_names=['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzales', 'Wilson', 'Anderson', 'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin', 'Lee', 'Perez', 'Thompson', 'White', 'Harris', 'Sanchez', 'Clark', 'Ramirez', 'Lewis', 'Robinson', 'Walker', 'Young', 'Allen', 'King', 'Wright', 'Scott', 'Torres', 'Nguyen', 'Hill', 'Flores', 'Green', 'Adams', 'Nelson', 'Baker', 'Hall', 'Rivera', 'Campbell', 'Mitchell', 'Carter', 'Roberts', 'Gomez', 'Phillips', 'Evans', 'Turner', 'Diaz', 'Parker', 'Cruz', 'Edwards', 'Collins', 'Reyes', 'Stewart', 'Morris', 'Morales', 'Murphy', 'Cook', 'Rogers', 'Gutierrez', 'Ortiz', 'Morgan', 'Cooper', 'Peterson', 'Bailey', 'Reed', 'Kelly', 'Howard', 'Ramos', 'Kim', 'Cox', 'Ward', 'Richardson', 'Watson', 'Brooks', 'Chavez', 'Wood', 'James', 'Bennet', 'Gray', 'Mendoza', 'Ruiz', 'Hughes', 'Price', 'Alvarez', 'Castillo', 'Sanders', 'Patel', 'Myers', 'Long', 'Ross', 'Foster', 'Jimenez']


#---------Funciones-----------------
def generar():
    global nombre1
    global nombre2
    global apellido1
    global apellido2
    global sexo
    global pais

    if pais.get()=="mex":

        if sexo.get()== "hombre":
                    
            nombre1.set(random.choice(nombres_hombre))
            nombre2.set(random.choice(nombres_hombre))

        elif sexo.get()== "mujer":
                    
            nombre1.set(random.choice(nombres_mujer))
            nombre2.set(random.choice(nombres_mujer))


        apellido1.set(random.choice(apellidos))
        apellido2.set(random.choice(apellidos))
    
    elif pais.get()=="usa":

        if sexo.get()=="hombre":

            nombre1.set(random.choice(male_names))
            nombre2.set(random.choice(male_names))

        elif sexo.get()=="mujer":
            
            nombre1.set(random.choice(female_names))
            nombre2.set(random.choice(female_names))
        
        apellido1.set(random.choice(family_names))
        apellido2.set("")



def salir():
    root.destroy()

def acerca_de():

    messagebox.showinfo("Generador de nombres","Creado por Gustavo Allfadir\nTodos los derechos reservados.\n©2020")



#-----------Root--------------------
bgvar="#E6E6E6"

root=Tk()
root.config(bg=bgvar)
root.title("Generador de nombres")
root.geometry("500x350+300+100")
root.resizable(0,0)

#----------Frame------------------


frame=Frame(root,bg=bgvar)

frame.pack()




#--------Barra de menu----------
barramenu=Menu(root,bg="#0A0A2A",fg="white")

root.config(menu=barramenu)


menuArchivo=Menu(barramenu, tearoff=0,bg="#0A0A2A",fg="white")
menuArchivo.add_command(label="Salir     ", command=lambda:salir())


menuAyuda=Menu(barramenu,tearoff=0,bg="#0A0A2A",fg="white")
menuAyuda.add_command(label="Acerca de     ",command=lambda:acerca_de())

#-----------Textos de la barra menu----------

barramenu.add_cascade(label="Archivo     ",menu=menuArchivo)
barramenu.add_cascade(label="Ayuda     ",menu=menuAyuda)

#-----Contenidos del frame---------

#selector de país
pais=StringVar()

paistxt=Label(frame, text="Pais: ",bg=bgvar)
paistxt.grid(row=0, column=0, pady=20)

mexb=Radiobutton(frame, text="México", var=pais, value="mex",bg=bgvar)
mexb.grid(row=0,column=1, padx=20)

usab=Radiobutton(frame, text="USA", var=pais, value="usa",bg=bgvar)
usab.grid(row=0, column=2, padx=20)

#Selector de sexo
sexo=StringVar()

sexotxt=Label(frame, text="Sexo: ",bg=bgvar)
sexotxt.grid(row=1, column=0, pady=20)

hombreb=Radiobutton(frame, text="Hombre", var=sexo, value="hombre",bg=bgvar)
hombreb.grid(row=1,column=1, padx=20)

mujerb=Radiobutton(frame, text="Mujer", var=sexo, value="mujer",bg=bgvar)
mujerb.grid(row=1, column=2, padx=20)



#Casillas
nombre1=StringVar()
nombre2=StringVar()
apellido1=StringVar()
apellido2=StringVar()

nombretxt=Label(frame,text="Nombre: ",bg=bgvar)
nombretxt.grid(row=2, column=0, columnspan=1, padx=10,pady=10)

nombrebox=Entry(frame, width=18, textvariable=nombre1)
nombrebox.grid(row=2,column=1,columnspan=2)

nombre2txt=Label(frame,text="Segundo nombre: ",bg=bgvar)
nombre2txt.grid(row=3, column=0, columnspan=1, padx=10,pady=10)

nombre2box=Entry(frame, width=18, textvariable=nombre2)
nombre2box.grid(row=3,column=1,columnspan=2)

apellidotxt=Label(frame,text="Apellido: ",bg=bgvar)
apellidotxt.grid(row=4, column=0, columnspan=1, padx=10,pady=10)

apellidobox=Entry(frame, width=18, textvariable=apellido1)
apellidobox.grid(row=4,column=1,columnspan=2)

apellido2txt=Label(frame,text="Segundo apellido: ",bg=bgvar)
apellido2txt.grid(row=5, column=0, columnspan=1, padx=10,pady=10)

apellido2box=Entry(frame, width=18, textvariable=apellido2)
apellido2box.grid(row=5,column=1,columnspan=2)

#botón generar

gen_button=Button(frame,bd=4, text="Generar nombre",bg=bgvar,command=lambda:generar())
gen_button.grid(row=6, column=1, pady=20)


root.mainloop()

