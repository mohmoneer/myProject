from ursina import *
from ursina.shaders import basic_lighting_shader
import random
from time import sleep


import sys

class Player(Entity):
    def __init__(self):
        super().__init__()
        self.parent = field
        self.model='sphere'
        # self.color = color.gray
        # self.texture = "skin_snake.jpg"
        self.scale = 0.04,0.04,1
        # self.position = (-0.1,-0.1,-0.1)
        self.collider = 'box'
        self.shader="colored_lights_shader"
        self.speed = 0.5
        self.dx = 0
        self.dy = 0
        self.eaten = 0
        self.size =0
        self.higth_eaten = 0
        self.text_higth_eaten = Text()
        self.new_body =Entity()
        self.time = sleep(0)

    def update(self):
        global body,text
        self.x += time.dt * self.dx
        self.y += time.dt * self.dy
        
        # red = random_generator.random() * 255
        # green = random_generator.random() * 255
        # blue = random_generator.random() * 255
        
        # s.color = color.rgb(red, green, blue)
 
        # Collision # or 
        # hit_info = self.intersects()
        # if hit_info.hit:
        
        # for checking the collision between the apple & snake
        if self.intersects(apple):
            
            Audio('apple_bite.wav')
            self.eaten += 1
            # to clear text update value eaten 
            text.y = -1
            self.text_higth_eaten.y = -1
            
            text = Text(text=f"Apple Eaten: {self.eaten}",position=(0,0.4),origin=(0,0),
                        scale=1.5,color=color.yellow,background=True)
            
            self.text_higth_eaten = Text(text=f"Hight Eaten: {self.higth_eaten}",position=(0.4,0.4),origin=(0,0),
                        scale=1.5,color=color.yellow,background=True) 
             
            # random apple posations between border land  4 * 4  
            apple.x = random_generator.randint(-4,4)*0.1
            apple.y = random_generator.randint(-4,4)*0.1
            
            

            
            self.new_body = Entity(parent=field,model='sphere',scale=(0.04,0.04,1),shader="lit_with_shadows_shader")# position=(z,x,y) z : hight new_body
            # add the head snake
            


            color_random = random_generator.choice(["#1235e2","#e23c42","#fef65b","#a3ffb4","#e1c0b6","#ffa500","#0000ff","#d7b4ae","#00ff00","#006400"])
            apple.color = color.hex(color_random)
            self.new_body.color = apple.color
            
            
            apple.animate_color(color.clear,duration=1,loop=True)
     
            body.append(self.new_body)

            #to speed up fast snake
            self.speed += 0.001
            
            if self.eaten > self.higth_eaten :
                self.higth_eaten = self.eaten
 
                # collction snake with selfbody
 
        # if abs(self.x) > abs(body) or abs(self.y)> abs(body):
        #       for dis in body:
        #         dis.position = (0,0)
        #         body = []  
        #       self.position = (0,0)       
        # Move the end segments first in range
        for i in range(len(body)-1,0,-1):
            body[i].position=body[i-1].position
            
   
        # First segment & move & add
        if len(body) > 0:
            body[0].x=self.x
            body[0].y=self.y
            

      
        # destroy snake border frame checking 
        # funa abs() to get real vlaue not -50
        if abs(self.x) >= 0.50 or abs(self.y)>= 0.50 :
            Audio('whistle.wav')
            for segment in body:
                segment.position=(10,10) 
                  
            body = []

            self.scale =0.04,0.04,1
            self.new_body.scale = 0.04,0.04,1        
            self.eaten = 0

            # for print in game
            print_on_screen("You crashed!",position=(0,0),origin=(0,0),scale=2, duration=2)
            # restart  the snake when Destroy
            self.position = (0,0)
            
            self.dx = 0
            self.dy = 0       
 
        
    def input(self, key):
        
        if key == "right arrow":
            if self.dx == -self.speed:
                self.dx = -self.speed
                self.dy = 0
            else:
                self.dy = 0
                self.dx = self.speed
        if key == "left arrow":
            if self.dx == self.speed:
                self.dx = self.speed
                self.dy = 0
            else:
                self.dy = 0
                self.dx = -self.speed

        if key == "up arrow":
            if self.dy == -self.speed:
                self.dy = -self.speed
                self.dx = 0
            else:
                self.dx = 0
                self.dy = self.speed
        if key == "down arrow":
            if self.dy == self.speed:
                self.dy = self.speed
                self.dx = 0
            else:
                self.dx = 0
                self.dy = -self.speed
         

                
        if key == "s": 
           self.speed = 0
        if key == "w":
           self.speed = 0.5
 
        # camera.z += self.x * 20 *time.dt
        # camera.y += self.y * 20 *time.dt
        # camera.x += self.dx * 20 *time.dt
        # camera.rotation_x += self.x * 20 *time.dt
        # camera.rotation_y += self.y * 20 *time.dt
        # camera.rotation_z += self.dx * 20 *time.dt

           
             
app=Ursina()
# animation start
camera.overlay.color = color.black
text_start = "mohammed moneer"

logo = Text(text=f'wellcome to snake game powerd by {text_start} prograss........',world_z=camera.overlay.z-0, scale=1.5, color=color.clear ,x=-0.44)
    # sys.stdout.write(i)
    # sys.stdout.flush()
    # sleep(0.1)
# animation text
logo.animate_color(color.white, duration=2, delay=1)
#clear colors for animations
camera.overlay.animate_color(color.clear, duration=1, delay=4)
# hide camera
destroy(logo, delay=4)

# window.size = (1280*.5, 720*.5)
Entity(model='quad', scale=50,color = color.black,position=(7.8,0.48))
# label = Text( x=-0.86,y=0.46, text="BY THABET-ALSOHIPY",color=color.yellow,background=True,scale=1.2)
s = Button(text="BY MOHAMMED MONEER", color=color.black, scale=.050 ,position=(-.76,0.48))
s.fit_to_text()


button_2d = Button(text="2D", color=color.blue,scale=.25 ,position=(-.84,.40))
button_3d = Button(text="3D", color=color.blue,scale=.25 ,position=(-.84,.33))
button_free_view = Button(text="free view", color=color.blue,scale=.25 ,position=(-.81,.25))
button_3d.fit_to_text()
button_2d.fit_to_text()
button_free_view.fit_to_text()

def _3d():
    
    camera.position = (9,-21, -21)
    camera.rotation_x = -56
def _2d():

    camera.x = 9.0
    camera.y= 9.2
    camera.z= -58.0515
    camera.rotation_x = -0

def free_view():
     
    camera.position = (world_size // 2, -10, -10)
    camera.rotation_x = -56

            
button_2d.on_click = _2d
button_3d.on_click = _3d
button_free_view.on_click = free_view
world_size = 19
field=Entity(model='quad', texture='R.jfif', texture_scale=(15,15),scale=(7,10,10,7),position=(world_size // 2, world_size // 2, -0.1))

apple = Entity(parent=field,model='sphere',color=color.red,scale=(0.04,0.04),
      position=(0.1,0.1,-0.2),collider='box',shader="lit_with_shadows_shader")


player = Player()

random_generator = random.Random() 
body=[]
# text = Text(text='')
# window.borderless = False               # Show a border
# window.fullscreen = False               # Do not go Fullscreen
# window.exit_button.visible = False      # Do not show the in-game red X that loses the window
window.fps_counter.enabled = True
# EditorCamera()
#button exit
b = Button(text='exit', color=color.azure, scale=.25 ,position=(-.84,0)) # to use icon or image icon='sword' or y = -.84 to size or x
b.fit_to_text()
b.on_click = application.quit

camera.position = (9,-21, -21)
camera.rotation_x = -56


app.run()
