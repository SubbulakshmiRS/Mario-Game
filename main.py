import os
import time


# import local files
import create_scenery
import config
import common
import sound

char = ''

while (config.stage == "losing"):
    try:
        # for next level
        if config.points > 50 and config.level == 1:
            config.level = 2
            common.restart_all()
            config.lives = 10

        # if mario goes below the floor level
        if config.m != "" and config.m.y > common.mids_r:
            raise config.Dead_Mario

        # create the scene depending on the level
        create_scenery.create_scene()
        if config.m is not "":
            if (char != config.JUMP):
                create_scenery.check_floor()
        common.print_all()

        # get input from user
        char = config.get_key(config.get_input())

        if (char == config.QUIT):
            # shut down all [q]
            config.stage = "quit"
            common.game_over()

        if (char == config.START):
            # create a Person [m]
            sound.PlaySound("mb_new.wav")
            create_scenery.create_Mario()

        elif (char == config.BREAK):
            # break the loop [s]
            os.system("tput reset")
            break

        elif (char == config.RIGHT):
            # Person moving right[a]
            if config.m is not "":
                config.m.move(config.m.x+2, config.m.y)

        elif (char == config.LEFT):
            # Person moving left[w]
            if config.m is not "":
                config.m.move(config.m.x-2, config.m.y)

        elif (char == config.JUMP):
            # Person jumping [d]
            sound.PlaySound("mb_jump.wav")
            if config.m is not "":
                config.m.jump()

    except config.Dead_Mario:
        common.print_all()
        sound.PlaySound("mb_die.wav")
        config.lives -= 1
        if config.lives > 0:
            common.restart_all()
        else:
            common.game_over()
            break


time.sleep(2)
print("\nBYEEE!!!\n")
exit(0)
