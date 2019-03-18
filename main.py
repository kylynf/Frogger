#
# Draw picture
#

import pygame
import math
import game_mouse
import froggerlib
import frogger

class PygameApp(game_mouse.Game):

    def __init__( self, width, height, size, frame_rate ):

        # title of the application is ""
        game_mouse.Game.__init__( self, "Frogger",
                                  width,
                                  height,
                                  frame_rate )
        # create a Picture instance
        self.mFrogger = frogger.Frogger( width, height, size)
        return
        
        
    def game_logic( self, keys, newkeys, buttons, newbuttons, mouse_position ):
        x = mouse_position[0]
        y = mouse_position[1]

        if pygame.K_a in newkeys:
            print("a key pressed")
        
        if 1 in newbuttons:
            print("button clicked")

        self.mFrogger.update( 1 / self.frames_per_second, keys )

        return
    
    def paint( self, surface ):
        # draw the picture
        self.mFrogger.draw( surface )
        return


def main():
    pygame.font.init( )
    #70 = grid size
    #840 = 12 *70 width
    #910 = 12 * 70 height
##    game = PygameApp( 300, 500, 70, 30 )
    game = PygameApp( 600, 605, 70, 30 )
    game.main_loop( )
    
if __name__ == "__main__":
    main()

