label hall:
    if warn_school_points >= 100:
        jump GAME_OVER
    elif True:
        $ checkZone = "school_hall"
        scene BG_lycee_couloir
        with fondu
        call screen ecole

screen ecole():
    frame:
        xalign 0.5
        yalign 0.99
        imagebutton:
            idle "Images/Plans/Minis/porte.png"
            hover "Images/Plans/Minis/porte_hover.png"
            action Jump("exit_school")

    imagebutton:
        xalign 0.2957
        yalign 0.35
        idle "Images/Plans/Lycee/annonce.png"
        hover "Images/Plans/Lycee/annonce_hover.png"
        action Jump("annonces")

    imagebutton:
        xalign 0.4
        yalign 0.45
        idle "Images/Plans/Minis/flecheG.png"
        hover "Images/Plans/Minis/flecheG_hover.png"
        action Jump("school_couloir_1")

    imagebutton:
        xalign 0.594
        yalign 0.45
        idle "Images/Plans/Minis/flecheD.png"
        hover "Images/Plans/Minis/flecheD_hover.png"
        action Jump("school_couloir_2")

    if heure < 9 or heure == 12:
        imagebutton:
            xalign 0.69
            yalign 0.75
            idle "Images/Plans/Lycee/EVENT/l5.png"
            hover "Images/Plans/Lycee/EVENT/l5_hover.png"
            action Jump("school_hall_l5")

    imagebutton:
        xalign 0.16
        yalign 0.5
        idle "Images/Plans/Minis/flecheG.png"
        hover "Images/Plans/Minis/flecheG_hover.png"
        action Jump("gym_in")

    imagebutton:
        xalign 0.83
        yalign 0.5
        idle "Images/Plans/Minis/flecheD.png"
        hover "Images/Plans/Minis/flecheD_hover.png"
        action Jump("wc")

    imagebutton:
        xalign 0.0
        yalign 1.0
        idle "Images/Plans/Lycee/room_1.png"
        hover "Images/Plans/Lycee/room_1_hover.png"
        action Jump("room_1")

    imagebutton:
        xalign 1.0
        yalign 1.0
        idle "Images/Plans/Lycee/room_2.png"
        hover "Images/Plans/Lycee/room_2_hover.png"
        action Jump("room_2")

screen ecole_ext():
    imagebutton:
        xalign 0.5
        yalign 0.75
        idle "Images/Plans/Minis/porte.png"
        hover "Images/Plans/Minis/porte_hover.png"
        action Jump("in_school")

    if heure >= 15:
        imagebutton:
            xalign 0.95
            yalign 0.95
            idle "Images/Plans/Lycee/bus.png"
            hover "Images/Plans/Lycee/bus_hover.png"
            action Jump("school_ville")

    if heure < 10 and jour == 5 and school_group_ext == False:
        imagebutton:
            xalign 0.85
            yalign 0.8
            idle "Images/Plans/Lycee/EVENT/groupe_1.png"
            hover "Images/Plans/Lycee/EVENT/groupe_1_hover.png"
            action Jump("groupe_1")

label exit_school:
    $ checkZone = "school_out"
    scene BG_lycee
    with fondu
    call screen ecole_ext

label in_school:
    $ ecole_in = True
    $ school_OK = True
    jump hall

label school_ville:
    $ ecole_in = False
    play sound "audio/voiture.mp3"
    show bus
    with inL
    pause 0.0
    hide bus
    with outR
    stop sound
    jump map
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
