"""
This module is for the sound effects
"""
import os

# plays the sound and because of dev/null , any output that comes out is passed to dev/null
# so as to not disrupt the screen

def play_sound(filename):
    """
    Play the file for sound effects
    """
    command = 'bash -c "aplay ./tracks/%s &> /dev/null &"' % (filename)
    os.system(command)
