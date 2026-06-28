# command_executer
🤖 Robot Command Executor (ROS 2)
A ROS 2 project that receives robot control commands through a topic and executes the corresponding actions. The node acts as a command interpreter, enabling robots to respond to external instructions in real time.

✨ Features
Subscribes to robot control commands
Executes actions based on received messages
Supports multiple movement commands
Provides real-time logging of robot actions
Demonstrates event-driven communication in ROS 2
Easily extendable to integrate with real robot hardware

🛠️ Technologies Used
ROS 2
Python
rclpy
std_msgs/String
Publisher–Subscriber Architecture

📂 Project Structure
robot_command_executor/
│
└── command_executor.py    # Receives and executes robot commands

🚀 How it Works
A publisher sends control commands to the robot_commands topic.
The CommandExecutor node subscribes to the topic.
Upon receiving a command, it checks the message and performs the corresponding action.
Invalid commands are detected and reported as warnings.

Supported Commands
Command	Action
Start	Starts the robot
Stop	Stops the robot
Left	Turns the robot left
Right	Turns the robot right

Any unsupported command generates a warning message.

Example Output
[INFO] Robot started
[INFO] Robot turn Left
[INFO] Robot turn right
[INFO] Robot Stop

For an invalid command:
[WARN] Command Error

Future Improvements
Add Forward and Backward movement
Integrate with /cmd_vel for controlling mobile robots
Support custom ROS 2 services and actions
Execute autonomous navigation commands
Add emergency stop functionality
Integrate with TurtleBot3 or custom robots
Create a GUI for sending commands

Learning Outcomes
ROS 2 Subscriber implementation
Topic-based communication
Processing incoming messages
Conditional command execution
Building modular robot control nodes
Python-based ROS 2 application development
