# Version 1: Not very clean
# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        cleaned = set()
        blocked = set()
        x, y = 0, 0
        direction = 0
        cnt = 0
        
        def u_turn():
            nonlocal robot
            robot.turnLeft()
            robot.turnLeft() 
            
        def turn_up():
            nonlocal direction
            if direction == 1:
                robot.turnLeft()
            elif direction == 2:
                u_turn()
            elif direction == 3:
                robot.turnRight()
            direction = 0
        
        def turn_right():
            nonlocal direction
            if direction == 0:
                robot.turnRight()
            elif direction == 2:
                robot.turnLeft()
            elif direction == 3:
                u_turn()
            direction = 1
            
        def turn_down():
            nonlocal direction
            if direction == 0:
                u_turn()
            elif direction == 1:
                robot.turnRight()
            elif direction == 3:
                robot.turnLeft()
            direction = 2
            
        def turn_left():
            nonlocal direction
            if direction == 0:
                robot.turnLeft()
            elif direction == 1:
                u_turn()
            elif direction == 2:
                robot.turnRight()
            direction = 3
        
        def dfs():
            nonlocal x, y, direction, cleaned, cnt
            robot.clean()
            cleaned.add((x, y))
            cnt += 1
            
            # up
            if (x, y - 1) not in cleaned and (x, y - 1) not in blocked:
                turn_up()
                direction = 0
                if robot.move():
                    y -= 1
                    dfs()
                    turn_down()
                    robot.move()
                    y += 1
                else:
                    blocked.add((x, y - 1))
            
            # right
            if (x + 1, y) not in cleaned and (x + 1, y) not in blocked:
                turn_right()
                if robot.move():
                    x += 1
                    dfs()
                    turn_left()
                    robot.move()
                    x -= 1
                else:
                    blocked.add((x + 1, y))
                    
            # down
            if (x, y + 1) not in cleaned and (x, y + 1) not in blocked:
                turn_down()
                if robot.move():
                    y += 1
                    dfs()
                    turn_up()
                    robot.move()
                    y -= 1
                else:
                    blocked.add((x, y + 1))
                    
            # left
            if (x - 1, y) not in cleaned and (x - 1, y) not in blocked:
                turn_left()
                if robot.move():
                    x -= 1
                    dfs()
                    turn_right()
                    robot.move()
                    x += 1
                else:
                    blocked.add((x - 1, y))
        
        dfs()

