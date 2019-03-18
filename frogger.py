import pygame
import froggerlib

class Frogger:

    def __init__( self,width, height, size):
        self.mSize = 45
        self.mReducedSize = 0.4 * size
        pad = (self.mSize - self.mReducedSize)/2
        self.mWidth = width
        self.mHeight = height
        self.mGameState = 1
        
##        x = self.mSize * 3 - self.mReducedSize + 40
##        y = self.mSize * 8 + pad
        x = self.mWidth//2-(self.mReducedSize/2)
        y = (55 * 10) + 15
        self.mFrog = froggerlib.Frog(x , y , self.mReducedSize, self.mReducedSize, x,y,8, 55, 55)
        
        self.mBeginningStage = froggerlib.Stage(0,55 * 10,self.mWidth, 55)
        self.mMidStage = froggerlib.Stage(0,55 * 5,self.mWidth,55)
        self.mHome = froggerlib.Home(0,55 * 0,self.mWidth,55)
        self.mRoad = froggerlib.Road(0,55*6, self.mWidth,55*4)
        self.mWater = froggerlib.Water(0,55,self.mWidth, 55*4)

        self.mDozer = froggerlib.Dozer(0,55 * 9 + 15,self.mReducedSize, self.mReducedSize, self.mWidth,55 * 9 + 15,3)
        self.mDozer1 = froggerlib.Dozer(205,55 * 9 + 15,self.mReducedSize, self.mReducedSize, self.mWidth,55 * 9 + 15,3)
        self.mDozer2 = froggerlib.Dozer(405,55 * 9 + 15,self.mReducedSize, self.mReducedSize, self.mWidth,55 * 9 + 15,3)

        self.mTruck =  froggerlib.Truck(0,55 * 8 + 15,self.mReducedSize, self.mReducedSize, -self.mReducedSize,55 * 8 + 15,5)
        self.mTruck1 = froggerlib.Truck(205,55 * 8 + 15,self.mReducedSize, self.mReducedSize, -self.mReducedSize,55 * 8 + 15,5)
        self.mTruck2 = froggerlib.Truck(405,55 * 8 + 15,self.mReducedSize, self.mReducedSize, -self.mReducedSize,55 * 8 + 15,5)

        self.mRacer = froggerlib.RaceCar(0,55 * 7 + 15,self.mReducedSize, self.mReducedSize, self.mWidth,55 * 7 + 15,4,10)
        self.mRacer1 = froggerlib.RaceCar(205,55 * 7 + 15,self.mReducedSize, self.mReducedSize, self.mWidth,55 * 7 + 15,4,10)
        self.mRacer2 = froggerlib.RaceCar(405,55 *7 + 15,self.mReducedSize, self.mReducedSize, self.mWidth,55 * 7 + 15,4,10)

        self.mCar = froggerlib.Car(0,55 * 6 + 15,self.mReducedSize, self.mReducedSize, -self.mReducedSize,55 * 6 + 15,8)
        self.mCar1 = froggerlib.Car(205,55 * 6 + 15,self.mReducedSize, self.mReducedSize, -self.mReducedSize,55 * 6 + 15,8)
        self.mCar2 = froggerlib.Car(405,55 * 6 + 15,self.mReducedSize, self.mReducedSize, -self.mReducedSize,55 * 6 + 15,8)

        self.mDodge = [self.mDozer,self.mDozer1,self.mDozer2, self.mTruck, self.mTruck1, self.mTruck2, self.mRacer, self.mRacer1, self.mRacer2, self.mCar, self.mCar1, self.mCar2]

        self.mAlligator = froggerlib.Alligator(0,55 * 4 + 15,self.mReducedSize, self.mReducedSize, self.mWidth,55 * 4 + 15,7)
        self.mAlligator1 = froggerlib.Alligator(205,55 * 4 + 15,self.mReducedSize, self.mReducedSize, self.mWidth,55 * 4 + 15,7)
        self.mAlligator2 = froggerlib.Alligator(405,55 * 4 + 15,self.mReducedSize, self.mReducedSize, self.mWidth,55 * 4 + 15,7)

        self.mLog = froggerlib.Log(0,55 * 3+ 15,self.mReducedSize + 20, self.mReducedSize , -self.mReducedSize,55 * 3 + 15,3)
        self.mLog1 = froggerlib.Log(205,55 * 3 + 15,self.mReducedSize + 20, self.mReducedSize, -self.mReducedSize,55 * 3 + 15,3)
        self.mLog2 = froggerlib.Log(405,55 * 3 + 15,self.mReducedSize + 20, self.mReducedSize, -self.mReducedSize,55 * 3 + 15,3)

        self.mLog3 = froggerlib.Log(0,55 * 2+ 15,self.mReducedSize + 40, self.mReducedSize, self.mWidth,55 * 2 + 15,4)
        self.mLog4 = froggerlib.Log(205,55 * 2 + 15,self.mReducedSize + 40, self.mReducedSize, self.mWidth,55 * 2 + 15,4)
        self.mLog5 = froggerlib.Log(405,55 * 2 + 15,self.mReducedSize + 40, self.mReducedSize, self.mWidth,55 * 2 + 15,4)

        self.mTurtle = froggerlib.Turtle(0,55 * 1 + 15,self.mReducedSize, self.mReducedSize, -self.mReducedSize,55 * 1 + 15,5)
        self.mTurtle1 = froggerlib.Turtle(205,55 * 1 + 15,self.mReducedSize, self.mReducedSize, -self.mReducedSize,55 * 1 + 15,5)
        self.mTurtle2 = froggerlib.Turtle(405,55 * 1 + 15,self.mReducedSize, self.mReducedSize, -self.mReducedSize,55 * 1 + 15,5)

    def game_over(self):
        if self.mFrog.outOfBounds(self.mWidth, self.mHeight):
           return True
        for car in self.mDodge:
           if car.hits(self.mFrog):
               return True
        if self.mFrog.hits(self.mWater):
            return True
        return False
 
    def update( self, dt, keys ):

        if pygame.K_w in keys:
            self.mFrog.up()
        elif pygame.K_s in keys:
            self.mFrog.down()
        elif pygame.K_a in keys:
            self.mFrog.left()
        elif pygame.K_d in keys:
            self.mFrog.right()


        if self.mDozer.atDesiredLocation():
           self.mDozer.setX(-self.mDozer.getWidth())

        if self.mDozer1.atDesiredLocation():
           self.mDozer1.setX(-self.mDozer1.getWidth())

        if self.mDozer2.atDesiredLocation():
           self.mDozer2.setX(-self.mDozer2.getWidth())

        if self.mTruck.atDesiredLocation():
           self.mTruck.setX(self.mWidth)

        if self.mTruck1.atDesiredLocation():
           self.mTruck1.setX(self.mWidth)

        if self.mTruck2.atDesiredLocation():
           self.mTruck2.setX(self.mWidth)

        if self.mCar.atDesiredLocation():
           self.mCar.setX(self.mWidth)

        if self.mCar1.atDesiredLocation():
           self.mCar1.setX(self.mWidth)

        if self.mCar2.atDesiredLocation():
           self.mCar2.setX(self.mWidth)

        if self.mRacer.atDesiredLocation():
           self.mRacer.setX(-self.mRacer.getWidth())

        if self.mRacer1.atDesiredLocation():
           self.mRacer1.setX(-self.mRacer1.getWidth())

        if self.mRacer2.atDesiredLocation():
           self.mRacer2.setX(-self.mRacer2.getWidth())

        if self.mAlligator.atDesiredLocation():
           self.mAlligator.setX(-self.mAlligator.getWidth())

        if self.mAlligator1.atDesiredLocation():
           self.mAlligator1.setX(-self.mAlligator1.getWidth())

        if self.mAlligator2.atDesiredLocation():
           self.mAlligator2.setX(-self.mAlligator2.getWidth())

        if self.mLog.atDesiredLocation():
           self.mLog.setX(self.mWidth)

        if self.mLog1.atDesiredLocation():
           self.mLog1.setX(self.mWidth)

        if self.mLog2.atDesiredLocation():
           self.mLog2.setX(self.mWidth)

        if self.mLog3.atDesiredLocation():
           self.mLog3.setX(-self.mLog3.getWidth())

        if self.mLog4.atDesiredLocation():
           self.mLog4.setX(-self.mLog4.getWidth())

        if self.mLog5.atDesiredLocation():
           self.mLog5.setX(-self.mLog5.getWidth())

        if self.mTurtle.atDesiredLocation():
           self.mTurtle.setX(self.mWidth)

        if self.mTurtle1.atDesiredLocation():
           self.mTurtle1.setX(self.mWidth)

        if self.mTurtle2.atDesiredLocation():
           self.mTurtle2.setX(self.mWidth)



        if self.mGameState == 1:
            self.mFrog.move()
            self.mDozer.move()
            self.mDozer1.move()
            self.mDozer2.move()
            self.mTruck.move()
            self.mTruck1.move()
            self.mTruck2.move()
            self.mCar.move()
            self.mCar1.move()
            self.mCar2.move()
            self.mRacer.move()
            self.mRacer1.move()
            self.mRacer2.move()
            self.mAlligator.move()
            self.mAlligator1.move()
            self.mAlligator2.move()
            self.mLog.move()
            self.mLog1.move()
            self.mLog2.move()
            self.mLog3.move()
            self.mLog4.move()
            self.mLog5.move()
            self.mTurtle.move()
            self.mTurtle1.move()
            self.mTurtle2.move()
            if self.game_over():
                self.mGameState = 2
        elif self.mGameState == 2:
            print("Game over")


        return




    def draw( self, surface ):
        color = ( 0, 0, 0 )
        surface.fill( color )
        #
        # for dozer in self.mDozers:
        #     self.mDozers.draw(surface,(255,128,0), rect)
        #
        # for truck in self.mTrucks:
        #    self.mTrucks.draw(surface,(204,0,102), rect)
        #
        # for race_car in self.mRacers:
        #    self.mRacers.draw(surface,(102,178,205), rect)
        #
        # for car in self.mCars:
        #    self.mCars.draw(surface,(255,0,0), rect)

        for i in range(11):
            pygame.draw.line(surface, (255,255,255), (0,55*i), (self.mWidth,55*i))

        

        self.mBeginningStage.draw(surface,(255,255,255))
        self.mMidStage.draw(surface,(255,255,255))
        self.mHome.draw(surface,(76,0,153))
        self.mRoad.draw(surface,(50,50,50))
        self.mWater.draw(surface,(0,0,255))
        self.mDozer.draw(surface,(255,128,0))
        self.mDozer1.draw(surface,(255,128,0))
        self.mDozer2.draw(surface,(255,128,0))
        self.mTruck.draw(surface,(204,0,102))
        self.mTruck1.draw(surface,(204,0,102))
        self.mTruck2.draw(surface,(204,0,102))
        self.mCar.draw(surface,(204,153,255))
        self.mCar1.draw(surface,(204,153,255))
        self.mCar2.draw(surface,(204,153,255))
        self.mRacer.draw(surface,(255,255,123))
        self.mRacer1.draw(surface,(255,255,123))
        self.mRacer2.draw(surface,(255,255,123))
        self.mAlligator.draw(surface,(191,255,0))
        self.mAlligator1.draw(surface,(191,255,0))
        self.mAlligator2.draw(surface,(191,255,0))
        self.mLog.draw(surface,(255,0,255))
        self.mLog1.draw(surface,(255,0,255))
        self.mLog2.draw(surface,(255,0,255))
        self.mLog3.draw(surface,(255,0,0))
        self.mLog4.draw(surface,(255,0,0))
        self.mLog5.draw(surface,(255,0,0))
        self.mFrog.draw(surface,(0,255,0))
        self.mTurtle.draw(surface,(69,0,255))
        self.mTurtle1.draw(surface,(69,0,255))
        self.mTurtle2.draw(surface,(69,0,255))

        return
