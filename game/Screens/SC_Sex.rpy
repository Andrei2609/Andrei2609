

image KISS_1 = "Images/CG/KISS/[sexName_1]_1.png"
image KISS_2:
    "Images/CG/KISS/[sexName_1]_2.png"
    pause .4
    "Images/CG/KISS/[sexName_1]_3.png"
    pause .4
    repeat
image KISS_3 = "Images/CG/KISS/[sexName_1]_4.png"
image KISS_4:
    "Images/CG/KISS/[sexName_1]_5.png"
    pause .3
    "Images/CG/KISS/[sexName_1]_6.png"
    pause .3
    repeat


image BOOBS_1 = "Images/CG/BOOBS/[sexName_1]_1.png"
image BOOBS_2 = "Images/CG/BOOBS/[sexName_1]_2.png"
image BOOBS_3:
    "Images/CG/BOOBS/[sexName_1]_3.png"
    pause .4
    "Images/CG/BOOBS/[sexName_1]_4.png"
    pause .4
    "Images/CG/BOOBS/[sexName_1]_3.1.png"
    pause .6
    "Images/CG/BOOBS/[sexName_1]_3.2.png"
    pause .6
    "Images/CG/BOOBS/[sexName_1]_3.1.png"
    pause .6
    "Images/CG/BOOBS/[sexName_1]_3.2.png"
    pause .6
    "Images/CG/BOOBS/[sexName_1]_4.png"
    pause .4
    repeat
image BOOBS_4:
    "Images/CG/BOOBS/[sexName_1]_5.png"
    pause .5
    "Images/CG/BOOBS/[sexName_1]_6.png"
    pause .5
    "Images/CG/BOOBS/[sexName_1]_7.png"
    pause .5
    repeat
image BOOBS_5:
    "Images/CG/BOOBS/[sexName_1]_8.png"
    pause .4
    "Images/CG/BOOBS/[sexName_1]_9.png"
    pause .4
    repeat


image HJ_1 = "Images/CG/HJ/[sexName_1]_1.png"
image HJ_2 = "Images/CG/HJ/[sexName_1]_2.png"
image HJ_3:
    "Images/CG/HJ/[sexName_1]_3.png"
    pause .5
    "Images/CG/HJ/[sexName_1]_4.png"
    pause .5
    repeat
image HJ_4:
    "Images/CG/HJ/[sexName_1]_3.png"
    pause .2
    "Images/CG/HJ/[sexName_1]_4.png"
    pause .2
    repeat
image HJ_5 = "Images/CG/HJ/[sexName_1]_2.png"
image HJ_6 = "Images/CG/HJ/[sexName_1]_6.png"
image HJ_7 = "Images/CG/HJ/[sexName_1]_7.png"


image MASTU_BOOBS_1 = "Images/CG/MASTU_BOOBS/[sexName_1]_1.png"
image MASTU_BOOBS_2 = "Images/CG/MASTU_BOOBS/[sexName_1]_2.png"
image MASTU_BOOBS_3 = "Images/CG/MASTU_BOOBS/[sexName_1]_3.png"
image MASTU_BOOBS_4:
    "Images/CG/MASTU_BOOBS/[sexName_1]_4.png"
    pause .3
    "Images/CG/MASTU_BOOBS/[sexName_1]_3.png"
    pause .3
    repeat
image MASTU_BOOBS_5:
    "Images/CG/MASTU_BOOBS/[sexName_1]_5.png"
    pause .3
    "Images/CG/MASTU_BOOBS/[sexName_1]_6.png"
    pause .3
    repeat
image MASTU_BOOBS_6:
    "Images/CG/MASTU_BOOBS/[sexName_1]_5.png"
    pause .2
    "Images/CG/MASTU_BOOBS/[sexName_1]_6.png"
    pause .2
    repeat
image MASTU_BOOBS_7:
    "Images/CG/MASTU_BOOBS/[sexName_1]_5.png"
    pause .1
    "Images/CG/MASTU_BOOBS/[sexName_1]_6.png"
    pause .1
    repeat
image MASTU_BOOBS_8 = "Images/CG/MASTU_BOOBS/[sexName_1]_7.png"
image MASTU_BOOBS_9 = "Images/CG/MASTU_BOOBS/[sexName_1]_8.png"


image BJ_1 = "Images/CG/BJ/[sexName_1]_1.png"
image BJ_2 = "Images/CG/BJ/[sexName_1]_2.png"
image BJ_3 = "Images/CG/BJ/[sexName_1]_3.png"
image BJ_4:
    "Images/CG/BJ/[sexName_1]_4.png"
    pause .5
    "Images/CG/BJ/[sexName_1]_5.png"
    pause .5
    repeat
image BJ_5:
    "Images/CG/BJ/[sexName_1]_4.png"
    pause .2
    "Images/CG/BJ/[sexName_1]_5.png"
    pause .2
    repeat
image BJ_6 = "Images/CG/BJ/[sexName_1]_6.png"
image BJ_7 = "Images/CG/BJ/[sexName_1]_7.png"
image BJ_8 = "Images/CG/BJ/[sexName_1]_8.png"
image BJ_9 = "Images/CG/BJ/[sexName_1]_9.png"
image BJ_10 = "Images/CG/BJ/[sexName_1]_10.png"
image BJ_11 = "Images/CG/BJ/[sexName_1]_11.png"
image BJ_12 = "Images/CG/BJ/[sexName_1]_12.png"


image SEX_WIN = "Images/CG/VICTORY/[sexName_1].png"

init:
    $ verif_sex = 0

screen Sex_Action(nom, second):
    modal True
    if nom == l2:
        $ verif_sex = sex_l2_points
    else:
        $ verif_sex = 0

    if second <> "":
        add "Images/CG/Avatar_Sex/Alternative/[second].png" xalign 0.25 yalign 1.0
        add "Images/CG/Avatar_Sex/[nom].png" xalign 0.75 yalign 1.0
    else:
        add "Images/CG/Avatar_Sex/[nom].png" xalign 0.5 yalign 1.0
    if verif_sex >= 20:
        imagebutton:
            idle "Images/Bases/Icones/Actions/action_kiss.png"
            hover "Images/Bases/Icones/Actions/action_kiss_hover.png"
            xalign 0.15
            yalign 0.95
            action SetVariable("sexName_1", nom), SetVariable("sexName_2", second), Jump("KISS_wheel")
    else:
        vbox:
            xalign 0.15
            yalign 0.95
            add "Images/Bases/Icones/Actions/action_kiss_no_dispo.png" xalign 0.5
            text _("Pas prête") xalign 0.5
    if verif_sex >= 30:
        imagebutton:
            idle "Images/Bases/Icones/Actions/action_boobs.png"
            hover "Images/Bases/Icones/Actions/action_boobs_hover.png"
            xalign 0.1
            yalign 0.65
            action SetVariable("sexName_1", nom), SetVariable("sexName_2", second), Jump("BOOBS_wheel")
    else:
        vbox:
            xalign 0.1
            yalign 0.65
            add "Images/Bases/Icones/Actions/action_boobs_no_dispo.png" xalign 0.5
            text _("Pas prête") xalign 0.5
    if verif_sex >= 40:
        imagebutton:
            idle "Images/Bases/Icones/Actions/action_HJ.png"
            hover "Images/Bases/Icones/Actions/action_HJ_hover.png"
            xalign 0.15
            yalign 0.35
            action SetVariable("sexName_1", nom), SetVariable("sexName_2", second), Jump("HJ_wheel")
    else:
        vbox:
            xalign 0.15
            yalign 0.35
            add "Images/Bases/Icones/Actions/action_HJ_no_dispo.png" xalign 0.5
            text _("Pas prête") xalign 0.5
    if verif_sex >= 40:
        imagebutton:
            idle "Images/Bases/Icones/Actions/action_FJ.png"
            hover "Images/Bases/Icones/Actions/action_FJ_hover.png"
            xalign 0.2
            yalign 0.05
            action SetVariable("sexName_1", nom), SetVariable("sexName_2", second), Jump("FJ_wheel")
    else:
        vbox:
            xalign 0.2
            yalign 0.05
            add "Images/Bases/Icones/Actions/action_FJ_no_dispo.png" xalign 0.5
            text _("Pas prête") xalign 0.5
    if verif_sex >= 50:
        imagebutton:
            idle "Images/Bases/Icones/Actions/action_touch.png"
            hover "Images/Bases/Icones/Actions/action_touch_hover.png"
            xalign 0.35
            yalign 0.01
            action SetVariable("sexName_1", nom), SetVariable("sexName_2", second), Jump("TOUCH_wheel")
    else:
        vbox:
            xalign 0.35
            yalign 0.01
            add "Images/Bases/Icones/Actions/action_touch_no_dispo.png" xalign 0.5
            text _("Pas prête") xalign 0.5
    if verif_sex >= 50:
        imagebutton:
            idle "Images/Bases/Icones/Actions/action_mastuboobs.png"
            hover "Images/Bases/Icones/Actions/action_mastuboobs_hover.png"
            xalign 0.5
            yalign 0
            action SetVariable("sexName_1", nom), SetVariable("sexName_2", second), Jump("MB_wheel")
    else:
        vbox:
            xalign 0.5
            yalign 0
            add "Images/Bases/Icones/Actions/action_mastuboobs_no_dispo.png" xalign 0.5
            text _("Pas prête") xalign 0.5
    if verif_sex >= 60 and l2_cum >= 5:
        imagebutton:
            idle "Images/Bases/Icones/Actions/action_BJ.png"
            hover "Images/Bases/Icones/Actions/action_BJ_hover.png"
            xalign 0.65
            yalign 0.01
            action SetVariable("sexName_1", nom), SetVariable("sexName_2", second), Jump("BJ_wheel")
    else:
        vbox:
            xalign 0.65
            yalign 0.01
            add "Images/Bases/Icones/Actions/action_BJ_no_dispo.png" xalign 0.5
            text _("Pas prête") xalign 0.5
    if verif_sex >= 60:
        imagebutton:
            idle "Images/Bases/Icones/Actions/action_lick.png"
            hover "Images/Bases/Icones/Actions/action_lick_hover.png"
            xalign 0.8
            yalign 0.05
            action SetVariable("sexName_1", nom), SetVariable("sexName_2", second), Jump("LICK_wheel")
    else:
        vbox:
            xalign 0.8
            yalign 0.05
            add "Images/Bases/Icones/Actions/action_lick_no_dispo.png" xalign 0.5
            text _("Pas prête") xalign 0.5
    if verif_sex >= 70:
        imagebutton:
            idle "Images/Bases/Icones/Actions/action_pussy.png"
            hover "Images/Bases/Icones/Actions/action_pussy_hover.png"
            xalign 0.85
            yalign 0.35
            action SetVariable("sexName_1", nom), SetVariable("sexName_2", second), Jump("PUSSY_1_wheel")
    else:
        vbox:
            xalign 0.85
            yalign 0.35
            add "Images/Bases/Icones/Actions/action_pussy_no_dispo.png" xalign 0.5
            text _("Pas prête") xalign 0.5
    if verif_sex >= 70:
        imagebutton:
            idle "Images/Bases/Icones/Actions/action_pussyA.png"
            hover "Images/Bases/Icones/Actions/action_pussyA_hover.png"
            xalign 0.9
            yalign 0.65
            action SetVariable("sexName_1", nom), SetVariable("sexName_2", second), Jump("PUSSY_2_wheel")
    else:
        vbox:
            xalign 0.9
            yalign 0.65
            add "Images/Bases/Icones/Actions/action_pussyA_no_dispo.png" xalign 0.5
            text _("Pas prête") xalign 0.5
    if verif_sex >= 90:
        imagebutton:
            idle "Images/Bases/Icones/Actions/action_anal.png"
            hover "Images/Bases/Icones/Actions/action_anal_hover.png"
            xalign 0.85
            yalign 0.95
            action SetVariable("sexName_1", nom), SetVariable("sexName_2", second), Jump("ANAL_wheel")
    else:
        vbox:
            xalign 0.85
            yalign 0.95
            add "Images/Bases/Icones/Actions/action_anal_no_dispo.png" xalign 0.5
            text _("Pas prête") xalign 0.5
    if second <> "":
        imagebutton:
            idle "Images/Bases/Icones/Actions/action_lesbian.png"
            hover "Images/Bases/Icones/Actions/action_lesbian_hover.png"
            xalign 0.97
            yalign 0.1
            action SetVariable("sexName_1", nom), SetVariable("sexName_2", second), Jump("LESBIAN_wheel")
    frame:
        has vbox
        label _("Click droit")
        label _("de la souris")
        label _("pour quitter.")
        add "Images/Bases/Icones/click_droit.png" xalign 0.5

label KISS_wheel:
    show KISS_1
    with fondu
    pause
    hide KISS_1
    show KISS_2
    with fondu
    pause
    if sex_l2_points >= 30:
        menu:
            "Lui touché les seins ?"
            "oui" if True:
                hide KISS_2
                show KISS_3
                with fondu
                pause
                hide KISS_3
                show KISS_4
                with fondu
                pause
                hide KISS_4
                with fondu
            "non" if True:
                hide KISS_2
                with fondu
                call screen Sex_Action(sexName_1, sexName_2)
    hide KISS_2
    with fondu
    call screen Sex_Action(sexName_1, sexName_2)

label BOOBS_wheel:
    show BOOBS_1
    with fondu
    pause
    hide BOOBS_1
    jump boobs_0

label boobs_0:
    show BOOBS_2
    with fondu
    pause
    menu:
        "Que faire ?"
        "malaxer" if True:
            hide BOOBS_2
            jump boobs_1
        "tétons" if True:
            hide BOOBS_2
            jump boobs_2
        "presser" if True:
            hide BOOBS_2
            jump boobs_3
        "arrêter" if True:
            hide BOOBS_2
            call screen Sex_Action(sexName_1, sexName_2)

label boobs_1:
    show BOOBS_3
    with fondu
    pause
    hide BOOBS_3
    jump boobs_0

label boobs_2:
    show BOOBS_4
    with fondu
    pause
    hide BOOBS_4
    jump boobs_0

label boobs_3:
    show BOOBS_5
    with fondu
    pause
    hide BOOBS_5
    jump boobs_0

label HJ_wheel:
    show HJ_1
    with fondu
    pause
    hide HJ_1
    show HJ_2
    with fondu
    pause
    hide HJ_2
    show HJ_3
    with fondu
    pause
    hide HJ_3
    show HJ_4
    with fondu
    pause
    hide HJ_4
    show HJ_5
    with fondu
    pause
    hide HJ_5
    show HJ_5
    with flash
    pause 0.1
    hide HJ_5
    show HJ_5
    with flash
    pause 0.1
    hide HJ_5
    show HJ_6
    with flash
    pause
    hide HJ_6
    show HJ_7
    with fondu
    pause
    hide HJ_7
    with fondu
    $ l2_cum += 1
    call screen Sex_Action(sexName_1, sexName_2)

label FJ_wheel:
    nar "en cours..."
    call screen Sex_Action(sexName_1, sexName_2)

label TOUCH_wheel:
    nar "en cours..."
    call screen Sex_Action(sexName_1, sexName_2)

label MB_wheel:
    show MASTU_BOOBS_1
    with fondu
    pause
    hide MASTU_BOOBS_1
    show MASTU_BOOBS_2
    with fondu
    pause
    hide MASTU_BOOBS_2
    show MASTU_BOOBS_3
    with fondu
    pause
    menu:
        "Presser" if True:
            hide MASTU_BOOBS_3
            jump MB_wheel_1
        "Branler" if True:
            hide MASTU_BOOBS_3
            jump MB_wheel_2
label MB_wheel_1:
    show MASTU_BOOBS_4
    with fondu
    pause
    menu:
        "Branler" if True:
            hide MASTU_BOOBS_4
            jump MB_wheel_2
        "Finir" if True:
            hide MASTU_BOOBS_4
            jump MB_wheel_3
label MB_wheel_2:
    show MASTU_BOOBS_5
    with fondu
    pause
    menu:
        "Presser" if True:
            hide MASTU_BOOBS_5
            jump MB_wheel_1
        "Plus vite" if True:
            hide MASTU_BOOBS_5
            jump MB_wheel_2_1
        "Finir" if True:
            hide MASTU_BOOBS_5
            jump MB_wheel_3
label MB_wheel_2_1:
    show MASTU_BOOBS_6
    with fondu
    pause
    menu:
        "Presser" if True:
            hide MASTU_BOOBS_6
            jump MB_wheel_1
        "Moins vite" if True:
            hide MASTU_BOOBS_6
            jump MB_wheel_2
        "Finir" if True:
            hide MASTU_BOOBS_6
            jump MB_wheel_3
label MB_wheel_3:
    show MASTU_BOOBS_7
    with fondu
    pause
    hide MASTU_BOOBS_7
    show MASTU_BOOBS_8
    with flash
    show MASTU_BOOBS_8
    with flash
    show MASTU_BOOBS_8
    with flash
    pause
    hide MASTU_BOOBS_8
    show MASTU_BOOBS_9
    with fondu
    pause
    hide MASTU_BOOBS_9
    $ l2_cum += 1
    call screen Sex_Action(sexName_1, sexName_2)

label BJ_wheel:
    show BJ_1
    with fondu
    pause
    hide BJ_1
    show BJ_2
    with fondu
    pause
    hide BJ_2
    show BJ_3
    with fondu
    pause
    hide BJ_3
    show BJ_4
    with fondu
    pause
    hide BJ_4
    show BJ_5
    with fondu
    pause
    hide BJ_5
    show BJ_6
    with flash
    pause 0.1
    hide BJ_6
    show BJ_7
    with flash
    pause 0.1
    hide BJ_7
    show BJ_7
    with flash
    pause 0.1
    hide BJ_7
    show BJ_8
    with fondu
    pause
    hide BJ_8
    show BJ_9
    with fondu
    pause
    hide BJ_9
    show BJ_10
    with fondu
    pause
    hide BJ_10
    show BJ_11
    with fondu
    pause
    hide BJ_11
    show BJ_12
    with fondu
    pause
    hide BJ_12
    with fondu
    $ l2_cum += 2
    call screen Sex_Action(sexName_1, sexName_2)

label LICK_wheel:
    nar "en cours..."
    call screen Sex_Action(sexName_1, sexName_2)

label PUSSY_1_wheel:
    nar "en cours..."
    if sexName_1 == "leni" and l2_win == False:
        $ l2_win = True
    show SEX_WIN
    with fondu
    pause
    hide SEX_WIN
    with fondu
    call screen Sex_Action(sexName_1, sexName_2)

label PUSSY_2_wheel:
    nar "en cours..."
    if sexName_1 == "leni" and l2_win == False:
        $ l2_win = True
    show SEX_WIN
    with fondu
    pause
    hide SEX_WIN
    with fondu
    call screen Sex_Action(sexName_1, sexName_2)

label ANAL_wheel:
    nar "en cours..."
    if sexName_1 == "leni" and l2_win == False:
        $ l2_win = True
    show SEX_WIN
    with fondu
    pause
    hide SEX_WIN
    with fondu
    call screen Sex_Action(sexName_1, sexName_2)

label LESBIAN_wheel:
    nar "en cours..."
    call screen Sex_Action(sexName_1, sexName_2)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
