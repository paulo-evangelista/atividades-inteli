import rclpy
from geometry_msgs.msg import PoseStamped
from tf_transformations import quaternion_from_euler
from rclpy.node import Node
from slam_toolbox.srv import DeserializePoseGraph
from rclpy.action import ActionClient
from nav2_msgs.action import NavigateToPose
from geometry_msgs.msg import PoseStamped
from time import sleep

class navigator(Node):

    def __init__(self):
        super().__init__('navigator')
        # CARREGAR O MAPA
        self.cli = self.create_client(DeserializePoseGraph, '/slam_toolbox/deserialize_map')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')

        self.action_client = ActionClient(self, NavigateToPose, 'navigate_to_pose')


        self.req = DeserializePoseGraph.Request()
        self.req.match_type = 1
        self.req.filename = "/home/paulo/navigation_data"

        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        self.get_logger().info('MAPA CARREGADO')

    def send_goal(self, pose):
        goal_msg = NavigateToPose.Goal()
        goal_msg.pose = pose

        self.action_client.wait_for_server()
        send_goal_future = self.action_client.send_goal_async(goal_msg)
        rclpy.spin_until_future_complete(self, send_goal_future)

        goal_handle = send_goal_future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected')
            return False

        self.get_logger().info('Goal accepted')
        result_future = goal_handle.get_result_async()
        rclpy.spin_until_future_complete(self, result_future)

        result = result_future.result().result
        self.get_logger().info('Result: {0}'.format(result))
        return True

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info('Received feedback: {0}'.format(feedback))

    def create_pose_stamped(self, node, pos_x, pos_y, rot_z):
        q_x, q_y, q_z, q_w = quaternion_from_euler(0.0, 0.0, rot_z)
        pose = PoseStamped()
        pose.header.frame_id = 'map'
        pose.header.stamp = node.get_clock().now().to_msg()
        pose.pose.position.x = pos_x
        pose.pose.position.y = pos_y
        pose.pose.position.z = pos_x
        pose.pose.orientation.x = q_x
        pose.pose.orientation.y = q_y
        pose.pose.orientation.z = q_z
        pose.pose.orientation.w = q_w
        return pose

def main():
    sleep(5)
    rclpy.init()

    nav = navigator()

    goal_pose = nav.create_pose_stamped(nav, -2.0, 0.0, 0.0)
    goal_pose2 = nav.create_pose_stamped(nav, 0.0, 2.0, 0.0)
    goal_pose3 = nav.create_pose_stamped(nav, -2.0, 0.0, 0.0)

    nav.send_goal(goal_pose)
    nav.send_goal(goal_pose2)

    rclpy.shutdown()

if __name__ == '__main__':
    main()