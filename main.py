import os
import time


# import local files
import create_scenery
import config
import common
import sound

Char = ''

while config.STAGE == "losing":
    try:
        # for next LEVEL
        if config.POINTS > 50 and config.LEVEL == 1:
            config.LEVEL = 2
            common.restart_all()
            config.LIVES = 10

        # if mario goes below the floor LEVEL
        if config.M != "" and config.M.y_pos > common.mids_r:
            raise config.DeadMario

        # create the scene depending on the LEVEL
        create_scenery.create_scene()
        if config.M != "":
            if Char != config.JUMP:
                create_scenery.check_floor()
        common.print_all()

        # get input from user
        Char = config.get_key(config.get_input())

        if Char == config.QUIT:
            # shut down all [q]
            config.STAGE = "quit"
            common.game_over()

        if Char == config.START:
            # create a Person [m]
            sound.play_sound("mb_new.wav")
            create_scenery.create_mario()

        elif Char == config.BREAK:
            # break the loop [s]
            os.system("tput reset")
            break

        elif Char == config.RIGHT:
            # Person moving right[a]
            if config.M != "":
                config.M.move(config.M.x_pos+2, config.M.y_pos)

        elif Char == config.LEFT:
            # Person moving left[w]
            if config.M != "":
                config.M.move(config.M.x_pos-2, config.M.y_pos)

        elif Char == config.JUMP:
            # Person jumping [d]
            sound.play_sound("mb_jump.wav")
            if config.M != "":
                config.M.jump()

    except config.DeadMario:
        common.print_all()
        sound.play_sound("mb_die.wav")
        config.LIVES -= 1
        if config.LIVES > 0:
            common.restart_all()
        else:
            common.game_over()
            break


time.sleep(2)
print("\nBYEEE!!!\n")
exit(0)
