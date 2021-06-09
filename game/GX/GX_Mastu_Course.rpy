
image MC_go_1 = "Images/Mini-Jeux/MastuCourse/go_1.png"
image MC_go_2 = "Images/Mini-Jeux/MastuCourse/go_2.png"
image BG_MC = "Images/Mini-Jeux/MastuCourse/back.png"

image MC_l5:
    "Images/Mini-Jeux/MastuCourse/l5_UP.png"
    pause 0.3
    "Images/Mini-Jeux/MastuCourse/l5_DOWN.png"
    pause 0.3
    repeat

init:
    $ user_MC_jauge = 0
    $ l5_MC_jauge = 0
    $ user_hand = True

screen MastuBar(name, pts):
    vbox:
        spacing 5
        label name xalign 0.5
        bar value AnimatedValue(pts, 100, 0.5) style "vbar" ysize 400 xsize 60 xalign 0.5

label Mastu_Course:
    $ user_MC_jauge = 0
    $ l5_MC_jauge = 0
    $ user_hand = True
    show MC_go_1
    with fondu
    l5 "Lincoln, tu fait quoi ?"
    user "Heu... rien !"
    l5 "C'est ça... Viens dans ma chambre de suite !"
    hide MC_go_1
    scene BG_lynn_lucy
    show screen Actor1("l5", "sleep", "normal", "sh_0", "", "sleep", "", "", "", "Neutre", "P")
    show screen User(tenue, "")
    with fondu
    l5 "Si tu arrive à jouir avant moi, je garde le secret."
    menu:
        l5 "Partant ?"
        "oui" if True:
            jump MastuCourse_GO
        "non" if True:
            $ warn_loud_points += 10
            hide screen Actor1
            hide screen User
            jump couloir

label MastuCourse_GO:
    show screen Actor1("l5", "sleep", "normal", "sh_0", "", "sleep", "", "", "", "Neutre", "P")
    with fondu
    l5 "Prépare toi, si tu gagne tu pourras giclé sur moi"
    hide screen Actor1
    hide screen User
    show MC_go_2
    with fondu
    l5 "Mais si tu perd, tu devras me lécher !"
    $ sex_points += 50
    hide MC_go_2
    show screen Actor1("l5", "sleep", "normal", "sh_0", "", "sleepA", "", "", "", "Neutre", "P")
    show screen User(tenue, "I")
    l5 "Prêt !{w} Partez !!!!"
    $ tenue = "nu"
    show screen Actor1("l5", "sleep", "normal", "sh_0", "", "sleepA", "", "", "", "Neutre", "")
    show screen User(tenue, "_P")
    user "Partez !"
    hide screen Actor1
    hide screen User
    scene BG_MC
    with fondu
    call screen MastuCourse

label MastuCourse_END:
    scene BG_lynn_lucy
    show screen Actor1("l5", "sleep", "normal", "sh_0", "", "sleepA", "", "", "", "Colere", "P")
    show screen User(tenue, "")
    with fondu
    l5 "Bravo Puanteur !"
    l5 "Tu as gagner je ne dirais rien"
    $ sex_l5_points += 1
    $ l5_cum += 1
    $ sex_points = 0
    $ tenue = "slip"
    hide screen Actor1
    hide screen User
    jump couloir

label MastuCourse_BADEND:
    scene BG_lynn_lucy
    show screen Actor1("l5", "sleep", "normal", "sh_0", "", "sleepA", "", "", "", "Neutre", "P")
    show screen User(tenue, "")
    with fondu
    l5 "C'est qui la meilleure !"
    l5 "Hey ban dans ta face !"
    l5 "Bon allez je vais être gentille, si tu me donne 5 $. Je ne dirais rien !"
    show screen Actor1("l5", "sleep", "normal", "sh_0", "", "sleepA", "", "", "", "Neutre", "")
    menu:
        "Donner 5$ pour son silence ?"
        "Oui" if user_coins >= 5:
            $ user_coins -= 5
            show screen Actor1("l5", "sleep", "normal", "sh_0", "", "sleepA", "", "", "", "Neutre", "P")
            l5 "merci !"
        "Non" if True:
            $ warn_loud_points += 1
            show screen Actor1("l5", "sleep", "normal", "sh_0", "", "sleepA", "", "", "", "Colere", "P")
            l5 "Comme tu voudras !"
    $ sex_l5_points += 1
    $ tenue = "slip"
    hide screen Actor1
    hide screen User
    jump couloir


screen MastuCourse():
    timer 1.0 repeat True action SetVariable("l5_MC_jauge", l5_MC_jauge + 10)
    if user_MC_jauge >= 100:
        $ sex_points = 0
        button:
            add "Images/Mini-Jeux/MastuCourse/user_WIN.png"
            action Jump("MastuCourse_END")
    elif l5_MC_jauge >= 100:
        button:
            add "Images/Mini-Jeux/MastuCourse/l5_WIN.png"
            action Jump("MastuCourse_BADEND")
    else:
        add "MC_l5" xalign 0.8 yalign 1.0

        if user_hand == True:
            add "Images/Mini-Jeux/MastuCourse/user_DOWN.png" xalign 0.2 yalign 1.0
            key "K_UP" action SetVariable("user_hand", False), SetVariable("user_MC_jauge", user_MC_jauge + force_points)
        elif user_hand == False:
            add "Images/Mini-Jeux/MastuCourse/user_UP.png" xalign 0.2 yalign 1.0
            key "K_DOWN" action SetVariable("user_hand", True), SetVariable("user_MC_jauge", user_MC_jauge + force_points)

        frame:
            yalign 0.5
            xalign 0.01
            use MastuBar("Lincoln", user_MC_jauge)

        frame:
            yalign 0.5
            xalign 0.99
            use MastuBar("Lynn", l5_MC_jauge)

        frame:
            yalign 0.9
            xalign 0.5
            has vbox
            label _("Appuie sur :") xalign 0.5
            if user_hand == True:
                add "Images/Plans/Minis/flecheH.png" xalign 0.5
            elif user_hand == False:
                add "Images/Plans/Minis/flecheB.png" xalign 0.5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
