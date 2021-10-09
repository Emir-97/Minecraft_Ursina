from ursina import *

#Se establece una clase para crear un cubo y tener un mayor espacio de trabajo
class Test_cube(Entity):
    def __init__(self):
        super().__init__(
          model = 'cube',
          color = color.white,
          texture = 'white_cube',
          #Se realiza en un campo tridimensional x,y,z
          rotation = Vec3(45,45,45),
          position=(-2,-3)
        )


#Se establece una función para darle movimiento a la figura
def update():
    #Se fija la tecla para mover la figura
    if held_keys['a']:
        #Se marca el eje de desplazamiento y la velocidad del mismo
        test_square.x -= 4 * time.dt

    if held_keys['d']:
        test_square.x += 4 * time.dt

#Se crea una clase para el boton que hereda de la clase integrada Button
class Test_button(Button):
    def __init__(self):
        super().__init__(
          #se establece el tamaño acorde a la pantalla
          parent = scene,
          model = 'cube',
          #el diseño del boton
          texture = 'brick',
          color = color.blue,
          #El color cuando se clickea en el
          highlight_color = color.lime,
          #El color cuando el raton pasa por el boton
          pressed_color = color.red)

    #Se fija la acción que realizará el Button cuando sea clickeado
    def input(self,key):
        if self.hovered:
           if key == 'left mouse down':
              print('Button pressed')


#Se crea una variable almacenadora de la aplicación
app = Ursina()

#Entity (son todos los objetos que interactuan en la pantalla de la app)
#Se crea un cuadrado con su color, tamaño y posición en la pantalla
test_square = Entity(model = 'quad', color = color.red, scale=(1,4), position=(5,4))

#Se carga la imagen que se quiere utilizar  para el  Entity
sans_texture = load_texture('assets/Sans.png')
#Se crea el Entity con la imagen cargada
sans = Entity(model ='quad', texture = sans_texture, position=(3,0))

#Se instancia la clase Test_cube
test_cube = Test_cube()

#Se instancia la clase Test_button
test_button = Test_button()

#Se ejecuta la app
app.run()
