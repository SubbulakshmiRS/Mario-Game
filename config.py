#common variables 
m = ""
e_list = []
w_list = []
lives = 3

'''
    Allow certain inputs and translate to easier to read format
    START : 0
    BREAK : 1
    RIGHT : 2
    JUMP : 3
    GUN : 4
    QUIT : 5
'''

# key presses
START, BREAK, RIGHT, JUMP, GUN, QUIT = range(6)
DIR = [JUMP, BREAK, START, RIGHT]
INVALID = -1

# allowed inputs
_allowed_inputs = {
    JUMP      : ['w', '\x1b[A'], \
    BREAK    : ['s', '\x1b[B'], \
    START    : ['a', '\x1b[D'], \
    RIGHT   : ['d', '\x1b[C'], \
    GUN    : ['b'],           \
    QUIT    : ['q']
}

class Dead_Mario(Exception):
    pass

class Touch_Boundary(Exception):
    pass

class Wall_Here(Exception):
    pass

def get_key(key):
    for x in _allowed_inputs:
        if key in _allowed_inputs[x]:
            return x
    return INVALID

# Gets a single character from standard input.  Does not echo to the screen.
class _Getch:

    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()


    def __call__(self):
        return self.impl()


class _GetchUnix:

    def __init__(self):
        import tty, sys


    def __call__(self):
        import sys
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:

    def __init__(self):
        import msvcrt


    def __call__(self):
        import msvcrt
        return msvcrt.getch()


_getch = _Getch()


class AlarmException(Exception):
    pass


def alarmHandler(signum, frame):
    raise AlarmException


def get_input(timeout=1):
    import signal
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.alarm(timeout)
    try:
        text = _getch()
        signal.alarm(0)
        return text
    except AlarmException:
        pass
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''

