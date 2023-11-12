from example_interfaces.srv import AddTwoInts
import signal
import rclpy
from rclpy.node import Node
import subprocess

def saveMapOnExit(sig, frame):
    subprocess.run(["ros2", "run", "nav2_map_server", "map_saver_cli","-f", "map"]) 


signal.signal(signal.SIGINT, saveMapOnExit)

class mapJobs(Node):

    def __init__(self):
        super().__init__('map_jobs')
        self.get_logger().info("---------------------------------------")
        self.get_logger().info("---------------------------------------")
        self.get_logger().info("---------------------------------------")
        self.get_logger().info("---------------------------------------")
        self.get_logger().info("")
        self.get_logger().info("INTRUÇÕES:")
        self.get_logger().info("")
        self.get_logger().info(" Utilize a nova janela de terminal que acabou de abrir para movimentar o robo. Mapeie todo o mapa")
        self.get_logger().info("")
        self.get_logger().info(" Quando terminar de mapear, volte a este terminal e pressione CTRL+C para finalizar o mapeamento")
        self.get_logger().info(" dois arquivos chamados (map.yaml e map.gdm) serão gerados no seu diretorio atual")
        self.get_logger().info("")
        self.get_logger().info("---------------------------------------")
        self.get_logger().info("---------------------------------------")
        self.get_logger().info("---------------------------------------")
        self.get_logger().info("---------------------------------------")



def main(args=None):
    rclpy.init(args=args)

    map_jobs = mapJobs()


if __name__ == '__main__':
    main()
    
    
# import sys
# import rclpy



# def main():
#     rclpy.logger.info("---------------------------------------", flush=True)
#     print("---------------------------------------",flush=True)
#     print(flush=True)
#     print("INTRUÇÕES:",flush=True)
#     print(flush=True)
#     print(" Utilize a nova janela de terminal que acabou de abrir para movimentar o robo. Mapeie todo o mapa",flush=True)
#     print(flush=True)
#     print(" Quando terminar de mapear, volte a este terminal e pressione CTRL+C para finalizar o mapeamento",flush=True)
#     print(flush=True)
#     print("---------------------------------------",flush=True)
#     print("---------------------------------------",flush