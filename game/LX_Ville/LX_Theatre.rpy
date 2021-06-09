
image BG_theatre = "Images/Backgrounds/theatre.png"
image BG_theatre_in = "Images/Backgrounds/theatre_in.png"
image BG_theatre_back = "Images/Backgrounds/theatre_back.png"

image concert_1 = "Images/Backgrounds/concert_1.png"

screen theatre_ext():
    imagebutton:
        xalign 0.01
        yalign 0.99
        idle "Images/Plans/Minis/flecheBG.png"
        hover "Images/Plans/Minis/flecheBG_hover.png"
        action Jump("map")

    if heure > 9 and heure < 24 and jour < 7:
        frame:
            xalign 0.5
            yalign 0.7
            imagebutton:
                idle "Images/Plans/Minis/porte.png"
                hover "Images/Plans/Minis/porte_hover.png"
                action Jump("theatre_in")

    vbox:
        xalign 0.85
        yalign 0.6
        text _("Concert") xalign 0.5
        text _("Galoche") xalign 0.5
        text _("Samedi 30 - 22h") xalign 0.5
        text _("100 $") xalign 0.5

screen theatre_in():
    imagebutton:
        xalign 0.5
        yalign 0.99
        idle "Images/Plans/Minis/flecheB.png"
        hover "Images/Plans/Minis/flecheB_hover.png"
        action Jump("theatre_2")

    imagebutton:
        xalign 0.487
        yalign 0.56
        idle "Images/Plans/Theatre/guichet.png"
        hover "Images/Plans/Theatre/guichet_hover.png"
        action Jump("theatre_caisse")

    if theatre_billet == True:
        imagebutton:
            xalign 0.25
            yalign 0.5
            idle "Images/Plans/Minis/flecheH.png"
            hover "Images/Plans/Minis/flecheH_hover.png"
            action Jump("theatre_salle")
        imagebutton:
            xalign 0.73
            yalign 0.5
            idle "Images/Plans/Minis/flecheH.png"
            hover "Images/Plans/Minis/flecheH_hover.png"
            action Jump("theatre_salle")

label theatre:
    call timer (0, 10) from _call_timer_1
    scene BG_theatre
    with fondu
    jump theatre_2

label theatre_2:
    $ checkZone = "theatre_out"
    scene BG_theatre
    with fondu
    call screen theatre_ext

label theatre_in:
    $ checkZone = "theatre_hall"
    scene BG_theatre_in
    with fondu
    call screen theatre_in

label theatre_caisse:
    scene BG_theatre_back
    with fondu
    menu:
        "Acheter un billet pour 100 $" if user_coins >= 100:
            $ theatre_billet = True
            $ user_coins -= 100
            jump theatre_in
        "Ne pas acheter un billet pour 100 $" if True:
            jump theatre_in

label theatre_salle:
    show concert_1
    with fondu
    nar ""
    $ theatre_billet = False
    call timer (2, 0) from _call_timer_2
    jump theatre_in
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
