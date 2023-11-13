from example_interfaces.srv import AddTwoInts
import rclpy
from rclpy.node import Node
from slam_toolbox.srv import SerializePoseGraph
import time
class mapSaver(Node):

    def __init__(self):
        super().__init__('map_saver')
        self.cli = self.create_client(SerializePoseGraph, '/slam_toolbox/serialize_map')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = SerializePoseGraph.Request()

    def send_request(self):
        self.req.filename = "/home/paulo/navigation_data"
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        self.get_logger().info('saved map to /home/paulo/navigation_data')
        self.get_logger().info('-> O mapa foi salvo automaticamente. Quando terminar, pressione CTRL+C para finalizar o mapeamento')



def main(args=None):
    rclpy.init(args=args)
    map_saver = mapSaver()
    while True:
        time.sleep(5)
        map_saver.send_request()

if __name__ == '__main__':
    main()