label school_couloir_1:
    $ checkZone = "school_couloir_1"
    scene BG_lycee_casiers_1
    with fondu
    call screen school_casier

screen school_casier():
    imagebutton:
        xalign 0.497
        yalign 0.0
        idle "Images/Plans/Lycee/casiers_user.png"
        hover "Images/Plans/Lycee/casiers_user_hover.png"
        action Jump("casier_user")

    if casier_key_1 == True:
        imagebutton:
            xalign 0.087
            yalign 0.0
            idle "Images/Plans/Lycee/casiers_1.png"
            hover "Images/Plans/Lycee/casiers_1_hover.png"
            action Jump("casier_1")
    if casier_key_2 == True:
        imagebutton:
            xalign 0.222
            yalign 0.0
            idle "Images/Plans/Lycee/casiers_2.png"
            hover "Images/Plans/Lycee/casiers_2_hover.png"
            action Jump("casier_2")
    if casier_key_3 == True:
        imagebutton:
            xalign 0.362
            yalign 0.0
            idle "Images/Plans/Lycee/casiers_3.png"
            hover "Images/Plans/Lycee/casiers_3_hover.png"
            action Jump("casier_3")
    if casier_key_5 == True:
        imagebutton:
            xalign 0.634
            yalign 0.0
            idle "Images/Plans/Lycee/casiers_5.png"
            hover "Images/Plans/Lycee/casiers_5_hover.png"
            action Jump("casier_5")
    if casier_key_6 == True:
        imagebutton:
            xalign 0.772
            yalign 0.0
            idle "Images/Plans/Lycee/casiers_6.png"
            hover "Images/Plans/Lycee/casiers_6_hover.png"
            action Jump("casier_6")
    if casier_key_7 == True:
        imagebutton:
            xalign 0.907
            yalign 0.0
            idle "Images/Plans/Lycee/casiers_7.png"
            hover "Images/Plans/Lycee/casiers_7_hover.png"
            action Jump("casier_7")

    if heure < 12 and heure >= 10:
        imagebutton:
            xalign 0.2
            yalign 0.7
            idle "Images/Plans/Lycee/EVENT/stella.png"
            hover "Images/Plans/Lycee/EVENT/stella_hover.png"
            action Jump("school_stella")

    if heure < 13 and heure >= 10:
        imagebutton:
            xalign 0.65
            yalign 0.9
            idle "Images/Plans/Lycee/EVENT/jordan.png"
            hover "Images/Plans/Lycee/EVENT/jordan_hover.png"
            action Jump("school_jordan")

    if heure == 12:
        imagebutton:
            xalign 0.9
            yalign 0.85
            idle "Images/Plans/Lycee/EVENT/cristina.png"
            hover "Images/Plans/Lycee/EVENT/cristina_hover.png"
            action Jump("school_cristina")

    imagebutton:
        xalign 0.009
        yalign 0.5
        idle "Images/Plans/Minis/flecheG.png"
        hover "Images/Plans/Minis/flecheG_hover.png"
        action Jump("cantine")

    imagebutton:
        xalign 0.99
        yalign 0.5
        idle "Images/Plans/Minis/flecheD.png"
        hover "Images/Plans/Minis/flecheD_hover.png"
        action Jump("hall")

label casier_user:
    scene BG_lycee_casiers_1
    with fondu
    call screen penderie
    jump user_tenue_verif

label user_tenue_verif:
    if tenue == "nu" or tenue == "slip" or tenue == "slipA":
        show screen User(tenue, "_P")
        user "Je peux pas aller en cours comme ça !"
        hide screen User
        jump casier_user
    elif True:
        call screen school_casier

label casier_1:
    scene BG_standby
    with fondu
    nar "en construction..."
    scene BG_lycee_casiers_1
    with fondu
    call screen school_casier

label casier_2:
    scene BG_standby
    with fondu
    nar "en construction..."
    scene BG_lycee_casiers_1
    with fondu
    call screen school_casier

label casier_3:
    scene BG_standby
    with fondu
    nar "en construction..."
    scene BG_lycee_casiers_1
    with fondu
    call screen school_casier

label casier_4:
    scene BG_standby
    with fondu
    nar "en construction..."
    scene BG_lycee_casiers_1
    with fondu
    call screen school_casier

label casier_5:
    scene BG_standby
    with fondu
    nar "en construction..."
    scene BG_lycee_casiers_1
    with fondu
    call screen school_casier

label casier_6:
    scene BG_standby
    with fondu
    nar "en construction..."
    scene BG_lycee_casiers_1
    with fondu
    call screen school_casier

label casier_7:
    scene BG_standby
    with fondu
    nar "en construction..."
    scene BG_lycee_casiers_1
    with fondu
    call screen school_casier
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
