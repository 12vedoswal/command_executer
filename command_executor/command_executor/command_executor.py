import rclpy
from rclpy.node import Node
from std_msgs.msg import String 

class CommandExecutor(Node):
    def __init__(self):
        super().__init__("command_executor")
        self.subscriptions_ = self.create_subscription(String,"robot_commands", self.command_callback,10)

    def command_callback(self, msg):
        command = msg.data

        if command == "Start" :
            self.get_logger().info("Robot started")
        
        elif command == "Stop" :
            self.get_logger().info("Robot Stop")

        elif command == "Left" :
            self.get_logger().info("Robot turn Left")

        elif command == "Right" :
            self.get_logger().info("Robot turn right")

        else :
            self.get_logger().warn(" Command Error")



def main(args=None):
    rclpy.init(args=args)
    node = CommandExecutor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__" :
    main()