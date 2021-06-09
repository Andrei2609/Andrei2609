screen cuisine():
    imagebutton:
        xalign 0.99
        yalign 0.99
        idle "Images/Plans/Minis/flecheBD.png"
        hover "Images/Plans/Minis/flecheBD_hover.png"
        action Jump("Diningroom")

    frame:
        xalign 0.0
        yalign 1.0
        has vbox:
            spacing 2
        imagebutton:
            xalign 0.5
            idle "Images/Plans/Minis/porte.png"
            hover "Images/Plans/Minis/porte_hover.png"
            action Jump("exit_jardin")
        text _("Jardin") xalign 0.5
        imagebutton:
            xalign 0.5
            idle "Images/Plans/Minis/escalier.png"
            hover "Images/Plans/Minis/escalierB_hover.png"
            action Jump("cave")
        text _("Cave") xalign 0.5

    imagebutton:
        xalign 0.78
        yalign 0.526
        idle "Images/Plans/Cuisine/smoothie.png"
        hover "Images/Plans/Cuisine/smoothie_hover.png"
        action ShowMenu("smoothie")

    if heure < 8:
        imagebutton:
            xalign 0.6
            yalign 0.8
            idle "Images/Plans/Cuisine/mom_sleep.png"
            hover "Images/Plans/Cuisine/mom_sleep_hover.png"
            action Jump("mom_cuisine_matin")
    elif go_school == False and heure < 9:
        imagebutton:
            xalign 0.6
            yalign 0.8
            idle "Images/Plans/Cuisine/mom.png"
            hover "Images/Plans/Cuisine/mom_hover.png"
            if heure == 8:
                action Jump("mom_cuisine_matin")
            else:
                action Jump("cuisine_mom")

    if heure >= 16 and heure <= 18 and jour == 2 or jour == 4:
        imagebutton:
            xalign 0.25
            yalign 0.8
            idle "Images/Plans/Cuisine/l4.png"
            hover "Images/Plans/Cuisine/l4_hover.png"
            action Jump("l4_cuisine_tarte_GO")
        if tarte_OK == True:
            imagebutton:
                xalign 0.85
                yalign 0.55
                idle "Images/Plans/Cuisine/tarte.png"
                hover "Images/Plans/Cuisine/tarte_hover.png"
                action Jump("l4_cuisine_tarte_END")

label cuisine:
    $ checkZone = "cuisine"
    scene BG_cuisine
    with fondu
    call screen cuisine

label exit_jardin:
    if tenue == "slip" or tenue == "slipA":
        show screen User(tenue, "_P")
        with fondu
        user "Je peux pas sortir de la maison comme ça !"
        hide screen User
        with fondu
        jump cuisine
    elif True:
        jump jardin

label cuisine_mom:
    if heure <= 8:
        show screen Actor1("mom", "sleep", "normal", "sh_0", "", "sleep", "", "", "", "Neutre", "P")
        with fondu
        mom "Bonjour Lincoln"
        show screen Actor1("mom", "sleep", "normal", "sh_0", "", "sleep", "", "", "", "Neutre", "")
        with fondu
    elif True:
        show screen Actor1("mom", "normal", "normal", "sh_1", "sb_1", "normal", "boucle_1", "", "", "Neutre", "P")
        with fondu
        mom "Bonjour Lincoln"
        show screen Actor1("mom", "normal", "normal", "sh_1", "sb_1", "normal", "boucle_1", "", "", "Neutre", "")
        with fondu
    call screen mom_talk
    hide screen Actor1
    jump cuisine
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
