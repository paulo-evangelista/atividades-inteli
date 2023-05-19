
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time
from turtlesim.srv import SetPen, TeleportAbsolute, Kill, Spawn

# classe Pilha e Fila em outro arquivo
from storage import Pilha, Fila

# classe responsável por controlar a tartaruga
class Turtle(Node):

    def __init__(self, turtleName: str):
        super().__init__(turtleName)
        time.sleep(0.4)
        #cria os clientes e publishers necessários para utilizar os tópicos e serviços.
        self.publisher_ = self.create_publisher(Twist, f'/{turtleName}/cmd_vel', 10)
        self.penClient = self.create_client(SetPen, f'/{turtleName}/set_pen')
        time.sleep(0.4)

    # função que recebe valores (X,Y) e publica no tópico cmd_vel, movendo a tartaruga
    def move(self, lx=0.0, ly=0.0):
        self.twist_msg_ = Twist()
        self.twist_msg_.linear.x = lx
        self.twist_msg_.linear.y = ly
        self.publisher_.publish(self.twist_msg_)
        time.sleep(1.1)

    # função que muda a cor e largura do rastro, publicando valores RGB e Width no tópico set_pen
    def change_pen(self, r=0, g=0, b=0, w=5):
        self.penReq = SetPen.Request()
        self.penReq.off = False
        self.penReq.r = r
        self.penReq.g = g
        self.penReq.b = b      
        self.penReq.width = w
        self.penClient.call_async(self.penReq)

# Lista com as coordenadas propostas no enunciado
coordinates = [
                [0.0, 0.5],
                [0.5, 0.0],
                [0.0, 0.5],
                [0.5, 0.0],
                [0.0, 1.0],
                [1.0, 0.0] 
                ]

# colocamos todas as coordenadas na nossa fila
fila = Fila()
for i in coordinates:
    fila.add(i)

# colocamos a oposta (negativa) de todas as coordenadas na nossa pilha
# dessa forma a tartaruga vai percorrer o caminho inverso 
pilha = Pilha()
for i in coordinates:
    pilha.add([-i[0], -i[1]])


def main():
    rclpy.init()

    # instanciando o nó
    turtle1 = Turtle("turtle1")

    # deixa o desenho vermelho
    turtle1.change_pen(r=255,g=0,b=0,w=3)

    # enquanto a fila não está vazia...
    while not fila.isEmpty():

        # pega a coordenada na primeira posição da fila
        [x, y] = fila.next()

        #e move a tartaruga para essa coordenada
        turtle1.move(lx=x, ly=y)

    #deixa o desenho verde
    turtle1.change_pen(r=0,g=255,b=0,w=3)

    #enquanto a pilha não está vazia...        
    while not pilha.isEmpty():
            
            # pega a coordenada do topo da pilha
            [x, y] = pilha.next()
            #e move a tartaruga para essa coordenada
            turtle1.move(lx=x, ly=y)

    # mata a tartaruga
    turtle1.destroy_node()

    rclpy.shutdown()

if __name__ == '__main__':
    main()