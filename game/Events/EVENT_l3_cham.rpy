
label l3_surprise_nue_cham_1:
    $ luna_peek_1 = True

    scene BG_luna_luan
    show screen Actor1("l3", "nue", "normal", "sh_0", "", "", "", "", "", "Neutre", "")
    with fondu
    show screen User(tenue, "")
    with inL
    pause .3
    show screen User(tenue, "_S")
    with fondu
    pause .5
    hide screen User
    hide screen Actor1
    show EF_surprise
    show luna_zoom_1 behind EF_surprise
    with flash
    pause
    hide luna_zoom_1
    show luna_zoom_2 behind EF_surprise
    with flash
    pause
    hide luna_zoom_2
    hide EF_surprise
    show screen User(tenue, "I")
    show screen Actor1("l3", "colere", "normal", "sh_0", "", "", "", "", "", "Colere", "P")
    with fondu
    l3 "Hey ! tu fais quoi Lincoln !?"

    $ sex_l3_points += 5
    $ warn_loud_points += 1

    show screen Actor1("l3", "colere", "normal", "sh_0", "", "", "", "", "", "Colere", "")
    show screen User(tenue, "_P")
    with fondu
    user "Désolé !"

    $ sex_points += 10

    show screen User(tenue, "")
    show screen Actor1("l3", "colere", "normal", "sh_0", "", "", "", "", "", "Colere", "EX")
    pause .8
    hide screen User
    hide screen Actor1
    jump couloir
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
