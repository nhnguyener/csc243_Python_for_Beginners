class robot:
    '''the big class'''
    def __init__(self, xc,yc,df):
        '''defines self input values'''

        self.x = xc
        self.y = yc
        self.d = df

    def turnLeft(self):
        '''turns robot left by a quarter'''
        if(self.d.lower() == 'u'):
            self.d = 'L'
        elif(self.d.lower() == 'l'):
            self.d = 'D'
        elif(self.d.lower() == 'd'):
            self.d = 'R'
        elif(self.d.lower() == 'r'):
            self.d = 'U'
    
    def turnRight(self):
        '''turns robot right by a quarter'''
        if(self.d.lower() == 'u'):
            self.d = 'R'
        elif(self.d.lower() == 'r'):
            self.d = 'D'
        elif(self.d.lower() == 'd'):
            self.d = 'L'
        elif(self.d.lower() == 'l'):
            self.d = 'U'

    def advance(self):
        '''moves robot forward by one in faced direction'''
        if(self.d.lower() == 'u'):
            self.y += 1
        elif(self.d.lower() == 'r'):
            self.x += 1
        elif(self.d.lower() == 'd'):
            self.y -= 1
        elif(self.d.lower() == 'l'):
            self.x -= 1

    def getPosition(self):
        '''returns (x,y) coords of robot'''
        return (self.x,self.y)

    def getFacing(self):
        '''returns robot's facing direction'''
        return (self.d.upper())

    def runProgram(self, cmds):
        '''run through multiple methods stated above'''
        for i in cmds:
            if(i == 'A'):
                robot.advance(self)
            elif(i == 'R'):
                robot.turnRight(self)
            elif(i == 'L'):
                robot.turnLeft(self)
    def __str__(self):
        '''returns string of robot pos details'''
        return "(" + str(self.x) + ", " + str(self.y) + '):' + str(self.d)
    
        
