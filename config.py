# common variables
m = ""
e_list = []
w_list = []
p_list = []
g_list = []
m_list = []
lives = 3

Obstacles = ["Wall", "Platform", "Marijuana", "Gap"]

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
START, BREAK, RIGHT, LEFT, JUMP, GUN, QUIT = range(7)
DIR = [JUMP, BREAK, START, RIGHT, LEFT]
INVALID = -1

# allowed inputs
_allowed_inputs = {
    JUMP: ['d', '\x1b[A'],
    BREAK: ['s', '\x1b[B'],
    START: ['m', '\x1b[D'],
    RIGHT: ['a', '\x1b[C'],
    LEFT: ['w', '\x1b[E'],
    GUN: ['b'],
    QUIT: ['q']
}


class Dead_Mario(Exception):
    pass


class Touch_Boundary(Exception):
    pass


class Wall_Here(Exception):
    pass


class Gap_Here(Exception):
    pass


class Enemy_Here(Exception):
    pass


class Platform_Here(Exception):
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
        import tty
        import sys

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
