'''
Código em python para fazer um desenho no turtleSim do ROS2

Vídeo-demonstração -> https://photos.app.goo.gl/3YXXFDVcFeN5XPNa6

O código controla tartarugas no simulador para fazer um desenho.
Criei a classe "Turtle" que é resposável por controlar uma tartaruga.
Cada instância dessa classe criará um nó ROS que responsável por controlar uma única tartaruga.
A classe tem funções para mover a tartaruga, mudar a cor de seu rastro e mata-lá.
Ao instanciar, a classe recebe apenas o nome da tartaruga desejada. O nó ROS criado será homônimo.

Depois disso, apenas utilizamos dessa clase para criar e mover várias tartarugas e fazer nosso desenho :)

Para mudar de cor, criar e matar tartarugas, estamos usando clients para consumir serviços disponibilizados pelo turtlesim.
    acredito que foram usados serviços em vez de tópicos pois são ações mais "imediatas", extraordinárias.
Já para mover a tartaruga, estamos publicando em um tópico.
    como a movimentação é uma ação rotineira, que acontece várias vezes em sequência, faz sentido utilizar um tópico.
'''

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time
from turtlesim.srv import SetPen, TeleportAbsolute, Kill, Spawn


class Turtle(Node):
    def __init__(self, turtleName: str):
        super().__init__(turtleName)
        time.sleep(0.4)
        self.killClient = self.create_client(Kill, '/kill')
        self.spawnClient = self.create_client(Spawn, '/spawn')

        # se já existe uma tartaruga com esse nome, vamos mata-la
        self.killReq = Kill.Request()
        self.killReq.name = turtleName
        self.killClient.call_async(self.killReq)
        time.sleep(0.5)

        # spawna a tartaruga desejada
        self.spawnReq = Spawn.Request()
        self.spawnReq.name = turtleName
        self.spawnReq.x = 1.0
        self.spawnReq.y = 1.0
        self.spawnClient.call_async(self.spawnReq)
        
        #cria os clientes e publishers necessários para utilizar os tópicos e serviços.
        self.publisher_ = self.create_publisher(Twist, f'/{turtleName}/cmd_vel', 10)
        self.penClient = self.create_client(SetPen, f'/{turtleName}/set_pen')
        time.sleep(0.4)

    def kill(self):
        self.killReq = Kill.Request()
        self.killReq.name = self.get_name()
        self.killClient.call_async(self.killReq)
        time.sleep(0.2)

    def move(self, repeat:int=1, lx=0.0, ly=0.0,lz=0.0, ax=0.0, ay=0.0, az=0.0):
        for i in range(0,repeat):
            self.twist_msg_ = Twist()
            self.twist_msg_.linear.x = lx
            self.twist_msg_.linear.y = ly
            self.twist_msg_.linear.z = lz
            self.twist_msg_.angular.x = ax
            self.twist_msg_.angular.y = ay
            self.twist_msg_.angular.z = az
            self.publisher_.publish(self.twist_msg_)
            time.sleep(1.1)

    def change_pen(self, r=0, g=0, b=0, w=5):
        self.penReq = SetPen.Request()
        self.penReq.off = False
        self.penReq.r = r
        self.penReq.g = g
        self.penReq.b = b      
        self.penReq.width = w
        self.penClient.call_async(self.penReq)

    
def main():
    rclpy.init()
    
    turtle1 = Turtle("turtle1")
    turtle1.change_pen(r=255,g=255,b=255,w=100)
    turtle1.move(lx=10.0)
    turtle1.move(ly=2.0)
    turtle1.move(lx=-10.0)
    turtle1.move(ly=2.0)
    turtle1.move(lx=10.0)
    turtle1.move(ly=2.0)
    turtle1.move(lx=-10.0)
    turtle1.move(ly=2.0)
    turtle1.move(lx=10.0)
    turtle1.move(ly=2.0)
    turtle1.move(lx=-10.0)
    
    turtle2 = Turtle("turtle2")
    turtle2.change_pen(w=4)
    turtle2.move(ly=5.0)
    turtle2.move(lx=2.0)
    turtle2.move(ly=-5.0)
    
    turtle3 = Turtle("turtle3")
    turtle3.change_pen(w=4)
    turtle3.move(lx=3.0)
    turtle3.move(ly=6.0)
    turtle3.move(lx=2.0)
    turtle3.move(ly=-6.0)
    turtle3.move(ly=6.0)
    turtle3.move(lx=-0.5)
    turtle3.move(ly=1.0)
    turtle3.move(lx=3.0)
    turtle3.move(ly=-7.0)
    
    turtle4 = Turtle("turtle4")
    turtle4.change_pen(w=4)
    turtle4.move(lx=9.0)
    turtle4.move(ly=7.5)
    turtle4.move(lx=3.0)
    
    turtle5 = Turtle("turtle5")
    turtle5.change_pen(w=1, r=255, g=255, b=255)
    turtle5.move(ly=8.0)
    turtle5.move(lx=-0.5)
    turtle5.change_pen(w=70, r=190, g=255, b=255)
    turtle5.move(lx=2.0, az=0.75, repeat=1)
    turtle5.move(lx=2.0, az=-0.75, repeat=2)
    turtle5.move(lx=2.0, az=0.75, repeat=2)
    turtle5.move(lx=2.0, az=-0.75, repeat=1)
    
    turtle6 = Turtle("turtle6")
    turtle6.change_pen(w=1, r=255, g=255, b=255)
    turtle6.move(ly=8.0, lx=1.5)
    turtle6.change_pen(w=80, r=255, g=184, b=41)
    turtle6.move(lx=0.5, az=1.5, repeat=4)
    
    turtle7 = Turtle("turtle57)
    turtle7.change_pen(w=100, r=0, g=138, b=23)
    turtle7.move(lx=12.0)

    turtle1.kill()
    turtle2.kill()
    turtle3.kill()
    turtle4.kill()
    turtle5.kill()
    turtle6.kill()
    turtle7.kill()
    rclpy.shutdown()

if __name__ == '__main__':
    main()