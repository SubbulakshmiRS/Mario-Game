"""
The config file - all common variables and exceptions
"""
import tty
import sys
import signal
# common variables
M = ""  # Mario
B = ""  # Boss
E_LIST = []  # Enemy
W_LIST = []  # Wall
P_LIST = []  # Platform
G_LIST = []  # Gap
M_LIST = []  # Marijuana
F_LIST = []  # Fish
S_LIST = []  # Star
B_LIST = []  # Bullets
LIVES = 3  # LIVES for LEVEL 1
POINTS = 0
LEVEL = 1  # current LEVEL
STAGE = "losing"  # if you aint winning , then you are loosing

ELEMENTS = ["Wall", "Platform", "Marijuana",
            "Gap", "Fish", "Star", "Boss", "Bullet"]

'''
    Allow certain inputs and translate to easier to read format
    START : 0
    BREAK : 1
    RIGHT : 2
    LEFT : 3
    JUMP : 4
    GUN : 5
    QUIT : 6
'''

# key presses
START, BREAK, RIGHT, LEFT, JUMP, QUIT = range(6)
DIR = [JUMP, BREAK, START, RIGHT, LEFT]
INVALID = -1

# allowed inputs
_ALLOWED_INPUTS = {
    JUMP: ['d', '\x1b[A'],
    BREAK: ['s', '\x1b[B'],
    START: ['m', '\x1b[D'],
    RIGHT: ['a', '\x1b[C'],
    LEFT: ['w', '\x1b[E'],
    QUIT: ['q']
}


# contains all the exceptions used

class DeletedElement(Exception):
    """
    Element deleted from list
    """
    pass


class DeadMario(Exception):
    """
    Mario has lost a life
    """
    pass


class TouchBoundary(Exception):
    """
    One of the elements of the screen has touched the boundary
    thus must be killed and not rendered again
    """
    pass


class WallHere(Exception):
    """
    Element can;t be rendered here
    """
    pass


class GapHere(Exception):
    """
    Element will fall through
    """
    pass


class EnemyHere(Exception):
    """
    Enemy present at the same location
    """
    pass


class PlatformHere(Exception):
    """
    Element wont fall through
    """
    pass


class MarioAbove(Exception):
    """
    Mario when above the POINTS and about to
    hit , it gets those coins
    """
    pass

# functions for getting the input key


def get_key(key):
    """
    From the inputted key, check whether it is allowed
    """
    for x_key in _ALLOWED_INPUTS:
        if key in _ALLOWED_INPUTS[x_key]:
            return x_key
    return INVALID


# Gets a single character from standard input.  Does not echo to the screen.


class _Getch:
    """
    Get the inputted character
    """
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self):
        return self.impl()

    def dummy(self):
        """
        dummy function for one public method
        """
        pass


class _GetchUnix:
    """
    Get inputted character for Unix operating system
    """
    def __init__(self):
        pass

    def __call__(self):
        import termios
        f_d = sys.stdin.fileno()
        old_settings = termios.tcgetattr(f_d)
        try:
            tty.setraw(sys.stdin.fileno())
            c_h = sys.stdin.read(1)
        finally:
            termios.tcsetattr(f_d, termios.TCSADRAIN, old_settings)
        return c_h

    def dummy(self):
        """
        dummy function for one public method
        """
        pass


class _GetchWindows:
    """
    Get inputted character for Windows operating system
    """
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()

    def dummy(self):
        """
        dummy function for one public method
        """
        pass


_GETCH = _Getch()


class AlarmException(Exception):
    """
    Alarm exception
    """
    pass


def alarm_handler(signum, frame):
    """
    Alarm handler
    Raises the exception
    """
    raise AlarmException


def get_input(timeout=1):
    """
    Get input
    """
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.alarm(timeout)
    try:
        text = _GETCH()
        signal.alarm(0)
        return text
    except AlarmException:
        pass
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''
