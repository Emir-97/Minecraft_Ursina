from ursina import *
#Se importa la clase para la primera persona del jugador
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

#Se importan las imagenes para usarlas como textura de la app
grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
dirt_texture = load_texture('assets/dirt_block.png')
sky_texture = load_texture('assets/skybox.png')
arm_texture = load_texture('assets/arm_texture.png')

#Se importa y carga el sonido y se establece que no se autoreprodusca
punch_sound = Audio('assets/punch_sound', loop = False, autoplay = False)

#Elimina el subrayado de la ventana
window.fps_counter.enabled = False
#Permite que se vea la x en la esquina superior para salir de la app
window.exit_button.visible =  True

block_pick = 1
#Se define la función para escoger el tipo de textura para los cubos creados
def update():
    global block_pick

    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.pasive()

    if held_keys['1']: block_pick = 1
    if held_keys['2']: block_pick = 2
    if held_keys['3']: block_pick = 3
    if held_keys['4']: block_pick = 4

#La clase para los voxel del juego
class Voxel(Button):
    def __init__(self, position= (0,0,0), texture= grass_texture):
        super().__init__(
        parent = scene,
        position = position,
        #Se importa un object para fijar la figura tridimensional
        model = 'assets/block',
        origin_y = 0.5,
        #Se utiliza la imagen para el bloque de pasto
        texture = texture,
        #Se establece un catalogo rgb de colores pero entre grises y random
        color = color.color(0,0, random.uniform(0.9,1)),
        #Se reduce el tamaño del cubo para que no se superpongan
        scale = 0.5)

   #Se crean las funcionalidades del button
    def input(self, key):
        # hovered se establece para poder trabajar con el teclado
        if self.hovered:
            #Si se hace clik izquierdo se crea un cubo en la misma posición que se hace clik
            if key == 'left mouse down':
                #Si se toca el click izquierdo reproduce el sonido
                punch_sound.play()
                if block_pick == 1: voxel =Voxel(position = self.position + mouse.normal, texture = grass_texture)
                if block_pick == 2: voxel =Voxel(position = self.position + mouse.normal, texture = stone_texture)
                if block_pick == 3: voxel =Voxel(position = self.position + mouse.normal, texture = brick_texture)
                if block_pick == 4: voxel =Voxel(position = self.position + mouse.normal, texture = dirt_texture)

            #Si se hace clik derecho se destruye el cubo
            if key == 'right mouse down':
                #Si se toca el click derecho reproduce el sonido
                punch_sound.play()
                destroy(self)

#Se crea la clase para el cielo de la app
class Sky(Entity):
    def __init__(self):
      super().__init__(
       parent = scene,
       model = 'sphere',
       texture = sky_texture,
       scale = 170,
       #Se fija que el cielo sea exterior al escenario
       double_sided = True)

#Se crea la clase para la mano del personaje
class Hand(Entity):
    def __init__(self):
        super().__init__(
          #Se establece la clase de la cúal hereda, en este caso de la vista 3d
			parent = camera.ui,
			model = 'assets/arm',
			texture = arm_texture,
            scale = 0.2,
            #Se establece la posición tanto en 3d como 2d
            rotation = Vec3(150,-10,0),
            position = Vec2(0.4, -0.6))

   #Se fija una nueva posición(movimiento) cuando se clickea
    def active(self):
        self.position = Vec2(0.3, -0.5)
   #Se fija la misma posición(movimiento) cuando no se hace nada
    def pasive(self):
        self.position = Vec2(0.4, -0.6)

#Se crea el escenario para el juego por medio de dos bucles for iterando uno dentro del otro
for z in range(30):
    for x in range(30):
        #Se va cambiando la posición de cada voxel para la plataforma
        voxel = Voxel(position = (x,0,z))

#Se crea el jugador pero con vista de primera persona
player = FirstPersonController()

#Se instancia el cielo
sky = Sky()

#Se instancia la clase para la mano
hand = Hand()

app.run()
