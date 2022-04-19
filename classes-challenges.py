# Setting Up Our Robot (Used Solution)
class DriveBot:
    robot_count = 0
    def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range
        DriveBot.robot_count += 1
        self.id = DriveBot.robot_count
        
        
    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction
        
    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range
    
    all_disabled = False
    latitude = -999999
    longitude = -999999
        
robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

robot_2 = DriveBot(35, 75, 25)
DriveBot.all_disabled = True
DriveBot.latitude = -50
DriveBot.longitude = 50
print(robot_1.motor_speed)
print(robot_2.motor_speed)

# Adding Robot Logic
# Enhanced Constructor
# Controlling Them All
# Identifying Robots (Used Solution)