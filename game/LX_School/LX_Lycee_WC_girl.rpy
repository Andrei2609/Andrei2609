screen WC_girl():
    imagebutton:
        xalign 0.009
        yalign 0.99
        idle "Images/Plans/Minis/flecheBG.png"
        hover "Images/Plans/Minis/flecheBG_hover.png"
        action Jump("wc")

    imagebutton:
        xalign 0.25
        yalign 0.6
        idle "Images/Plans/Minis/peek.png"
        hover "Images/Plans/Minis/peek_hover.png"
        action Jump("peek_wc_1")

    imagebutton:
        xalign 0.335
        yalign 0.55
        idle "Images/Plans/Minis/peek.png"
        hover "Images/Plans/Minis/peek_hover.png"
        action Jump("peek_wc_2")

    imagebutton:
        xalign 0.39
        yalign 0.5
        idle "Images/Plans/Minis/peek.png"
        hover "Images/Plans/Minis/peek_hover.png"
        action Jump("peek_wc_3")

    imagebutton:
        xalign 0.43
        yalign 0.45
        idle "Images/Plans/Minis/peek.png"
        hover "Images/Plans/Minis/peek_hover.png"
        action Jump("peek_wc_4")

label wc_filles:
    $ checkZone = "school_wc_girl"
    scene BG_lycee_wc_fille
    with fondu
    if heure >= 12 and heure < 14 and jour == 5 or jour == 2:
        show screen Actor1("cristina", "normal", "normal", "sh_1", "sb_1", "normal", "boucle_1", "bandeau_1", "", "Colere", "P")
        with fondu
        cristina "Lincoln ! C'est les toilette des filles sale pervers !"
        $ sex_points += 5
        hide screen Actor1
        jump wc
    elif True:
        call screen WC_girl

label peek_wc_1:
    if min >= 55:
        $ heure += 1
        $ min = 0
    elif True:
        $ min += 5
    $ sex_points += 10
    show screen peekWC("BG_standby")
    pause
    hide screen peekWC
    jump wc_filles

label peek_wc_2:
    if min >= 55:
        $ heure += 1
        $ min = 0
    elif True:
        $ min += 5
    $ sex_points += 10
    show screen peekWC("BG_standby")
    pause
    hide screen peekWC
    jump wc_filles

label peek_wc_3:
    if min >= 55:
        $ heure += 1
        $ min = 0
    elif True:
        $ min += 5
    $ sex_points += 10
    show screen peekWC("BG_standby")
    pause
    hide screen peekWC
    jump wc_filles

label peek_wc_4:
    if min >= 55:
        $ heure += 1
        $ min = 0
    elif True:
        $ min += 5
    $ sex_points += 10
    show screen peekWC("BG_standby")
    pause
    hide screen peekWC
    jump wc_filles

label peek_wc_filles:
    if vie_points <= 0:
        show screen User(tenue, "_P")
        user "trop fatiguer pour ça..."
        hide screen User
    elif True:
        if min >= 55:
            $ heure += 1
            $ min = 0
        elif True:
            $ min += 5
        $ sex_points += 10
        $ int_points += 1
        $ vie_points -= 10
        if heure >= 12 and heure < 14 and jour == 5 or jour == 2:
            $ sex_points += 30
            show screen peek("cristina_WC_peek")
            pause
            hide screen peek
            show cristina_WC_boobs_size
            pause
        elif True:
            show screen peek("BG_lycee_wc_fille")
            pause
            hide screen peek
    jump wc
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
