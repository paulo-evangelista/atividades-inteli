
import rclpy
from math import floor
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf_transformations import euler_from_quaternion
import time

class Turtle(Node):
    def __init__(self):

        # posição atual do robô
        self.currentPos = [0,0]
        # posição anterior do robô
        self.lastPos = [0,0]
        # ângulo atual do robô em relação ao eixo x
        self.currentAngle = 0


        super().__init__("turtle")
        self.movePublisher = self.create_publisher(Twist, f'/cmd_vel', 10)
        self.odomenterSubscription = self.create_subscription(
            Odometry,
            '/odom',
            self.handleOdometer,
            10)
        
    def handleOdometer(self, msg):
        self.lastPos = self.currentPos
        self.currentPos = [msg.pose.pose.position.x, msg.pose.pose.position.y]

        # print( f"Current position: {self.currentPos}")
        orientiation = msg.pose.pose.orientation
        _, _, theta = euler_from_quaternion(
            [orientiation.x, orientiation.y, orientiation.z, orientiation.w])

        self.currentAngle = floor(theta*180/3.14)

    def publishMove(self, linearV:float=0.0, angularV:float=0.0):
        self.twist_msg_ = Twist()
        self.twist_msg_.angular.z = angularV
        self.twist_msg_.linear.x = linearV
        self.movePublisher.publish(self.twist_msg_)

    def publishStop(self):
        self.publishMove()

    def moveTo(self, desiredX = None, desiredY= None):
        if desiredX > self.currentPos[0]:
            self.rotate(0)
            self.movePositive(X=desiredX)
        else:
            self.rotate(-180)
            self.moveNegative(X=desiredX)
        
        if desiredY > self.currentPos[1]:
            self.rotate(90)
            self.movePositive(Y=desiredY)
        else:
            self.rotate(-90)
            self.moveNegative(Y=desiredY)
        
        print(f"\n--> Coordenada atingida! \n--> Posição real atingida: {self.currentPos}")

    def rotate(self, desiredAngle):
        while desiredAngle != self.currentAngle:
            self.publishMove(.0, .5)
            rclpy.spin_once(self)

        self.publishStop()
        
    def movePositive(self, X=None, Y=None):

        usingX = False
        usingY = False 

        if X and not Y:
            desiredPos = X
            usingX = True
            currentPos = self.currentPos[0]

        elif Y and not X:
            desiredPos = Y
            usingY = True
            currentPos = self.currentPos[1]
        else:
            raise Exception("X e Y não podem ser especificados ao mesmo tempo")

        while desiredPos != floor(currentPos):

            if usingX:
                currentPos = self.currentPos[0]
                shouldTurnRight = self.currentAngle > 0
                shouldTurnLeft = self.currentAngle < 0
            elif usingY:
                currentPos = self.currentPos[1]
                shouldTurnRight = self.currentAngle > 90
                shouldTurnLeft = self.currentAngle < 90
            else:
                raise Exception("X e Y não podem ser especificados ao mesmo tempo")
        

            rclpy.spin_once(self)
            # print("aa ->", self.currentAngle)

            angularVelocity = 0.0

            if shouldTurnRight:
                angularVelocity = -1.0
            elif shouldTurnLeft:
                angularVelocity = 1.0

            self.publishMove(1.0, angularVelocity)

        self.publishStop()
        time.sleep(1)
    
    def moveNegative(self, X=None, Y=None):

        usingX = False
        usingY = False 

        if X and not Y:
            desiredPos = X
            usingX = True
            currentPos = self.currentPos[0]

        elif Y and not X:
            desiredPos = Y
            usingY = True
            currentPos = self.currentPos[1]
        else:
            raise Exception("X e Y não podem ser especificados ao mesmo tempo")

        while desiredPos != floor(currentPos):

            if usingX:
                currentPos = self.currentPos[0]
                shouldTurnRight = self.currentAngle > -180 and self.currentAngle < 0
                shouldTurnLeft = self.currentAngle < 180 and self.currentAngle > 0

            elif usingY:
                currentPos = self.currentPos[1]
                shouldTurnLeft = (self.currentAngle < -90 and self.currentAngle > -180) or (self.currentAngle < 180 and self.currentAngle > 90)
                shouldTurnRight = (self.currentAngle > -90 and self.currentAngle <= 90)

            else:
                raise Exception("X e Y não podem ser especificados ao mesmo tempo")
        

            rclpy.spin_once(self)
            # print("aa ->", self.currentAngle)
            angularVelocity = 0.0

            if shouldTurnRight:
                angularVelocity = -1.0
            elif shouldTurnLeft:
                angularVelocity = 1.0

            self.publishMove(1.0, angularVelocity)
            self.movePublisher.publish(self.twist_msg_)

        self.publishStop()
        time.sleep(1)

coordinates = [[-8, -5], [10, 8], [1, 1], [6, -2], [-1, -3]]

def main():
    rclpy.init()
    robot = Turtle()
    coordinates= []
    coordinateAmount = input("Quantas coordenadas você quer alcançar? --> ")

    if not coordinateAmount.isnumeric():
        raise Exception("Apenas números são aceitos")
    
    for i in range(int(coordinateAmount)):
        x = input(f"insira o valor X desejado para a {i+1}ª coordenada --> ")
        y = input(f"insira o valor Y desejado para a {i+1}ª coordenada --> ")
        coordinates.append([int(x), int(y)])
        print(f"{i+1}ª coordenada adicionada com sucesso!\n")

    print("Iniciando movimentação do robô...")
    for i in coordinates:
        robot.moveTo(i[0], i[1])
        print(f"--> Posição desejada: {i}")

    print("\n\n--Movimentação finalizada!--")
    rclpy.shutdown()

if __name__ == '__main__':
    main()