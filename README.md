# MARIO *Game* 

This is a simple mario game purely written in python3 without the usage of standard libraries such as *Pygame* , *Curses* and such .The code strictly follows the many OOPS concepts and PEP8 standard .


## *Installation and Running*

Create the workspace to run the game 
> mkvirtualenv mario-game

> workon mario-game

Git instructions 
> git clone https://gitlab.com/SubbulakshmiRS/Mario-game (dev branch)

Install dependencies 
> pip3 install -r requirements.txt

Run the code for the game 
> python3 main.py


## *Inputs for the Mario*
Input the corresponding characters for Mario to do the following action in the game
> Start : 'm'

>Break : 's'

>Left : 'w'

>Right : 'a'

>Jump : 'd'

>Quit the game: 'q'


## *Story of the Game*
There are 2 LEVELs in the game .
# Level1 :
*LIVES = 3*
This LEVEL contains basic mario game with the obstacles being the wall,platform,enemy and holes/gaps which are created at random (at a safe distance from the current position of the Mario).All elements are created in such a way to avoid clumping and such.

# Level2 :
*LIVES = 10*
This LEVEL contains the boss enemy which is stationary and fires bullets ,always in the direction oF the Mario with respect to the Enemy .Platforms are randomly formed for Mario to jump on and thereby cross the enemy .
The only way to win this LEVEL is to fall on top of the Boss enemy .The LIVES of the Mario has increased .

Mario can only go from one LEVEL to another by having a certain number of POINTS and not dead .
Sound packages are used .For specific movements/situations , the packages will be played.


## *Characters*

>MARIO : the protagonist of the game who can jump(gravity effect is present),move left and right .

>ENEMY : the enemy can get killed either by falling into a pit or by getting jumped on by Mario .

>BOSS ENEMY : this stationary enemy(only one will be formed in the whole LEVEL) can shoot bullets and can only              die if Mario can jump on top of it without getting shot .

>PLATFORM : platforms move in random directions and if jumped on , Mario can run on top of it .

>WALL : if clash into it , Mario will die but enemy clashes into it , the enemy stops moving .

>STAR and FISH : part of the background .

>MARIJUANA : the infamous weed which when hit on by Mario , gains POINTS

>GAP : these random gaps will be formed in which Mario or the enemy can fall into and die .

>FLOOR : to show the LEVEL on which Mario can walk on 

## *References*
> http://www.numpy.org/

> https://pypi.org/project/colorama/

> https://themushroomkingdom.net/wav.shtml
