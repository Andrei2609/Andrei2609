
image TV_on = "Images/Backgrounds/TV_on.png"
image TV_off = "Images/Backgrounds/TV_off.png"

image TV_show = "Images/Backgrounds/TV_soft_[TV_count].png"
image TV_show_X = "Images/Backgrounds/TV_porn_[TV_count].png"
image TV_jv = "Images/Backgrounds/TV_JV.png"

label TV_on:
    if TV_count < 4:
        show TV_show
        $ TV_count += 1
    elif True:
        show TV_show
        $ TV_count = 0
    $ int_points += 1
    nar "Vous regardez la TV"
    hide TV_show
    call timer (0, 30) from _call_timer_12
    jump salon

label TV_porn:
    if TV_count < 4:
        show TV_show_X
        $ TV_count += 1
    elif True:
        $ TV_count = 0
        show TV_show_X
    $ sex_points += 10
    nar "Vous regardez un film chaud sur la TV"
    hide TV_show_X
    call timer (0, 30) from _call_timer_13
    jump salon

label TV_jv:
    show TV_jv
    $ int_points += 1
    nar "Vous jouez aux jeux vidéos."
    hide TV_jv
    call timer (0, 30) from _call_timer_14
    jump salon
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
