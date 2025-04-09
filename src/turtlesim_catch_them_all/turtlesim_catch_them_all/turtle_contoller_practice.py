#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

class ControlTurtleSim(Node): #MODIFY NAME
    def __init__(self):
        super().__init__("control_turtle") #MODIFY NAME
        self.pose_: Pose = None
        self.cmd_vel_publisher_ = self.create_publisher(
            Twist, "/turtle1/cmd_vel", 10)
        self.turtle_subscriber_ = self.create_subscription(
            Pose, "/turtle1/pose", self.callback_turtlesim, 10)
        self.turtle_timer = self.create_timer(0.01, self.motion_loop)

    def callback_turtlesim(self, pose: Pose):
        self.pose_ = pose

    def motion_loop(self):
        if self.pose == None:
            return

        
        

def main(args=None):
    rclpy.init(args=args)
    node = ControlTurtleSim() #MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()