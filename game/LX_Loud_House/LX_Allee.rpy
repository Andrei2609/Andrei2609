screen allee():
    imagebutton:
        xalign 0.009
        yalign 0.99
        idle "Images/Plans/Minis/flecheBG.png"
        hover "Images/Plans/Minis/flecheBG_hover.png"
        action Jump("exit")

    imagebutton:
        xalign 0.216
        yalign 0.858
        idle "Images/Plans/Allee/jardin.png"
        hover "Images/Plans/Allee/jardin_hover.png"
        action Jump("jardin")

    imagebutton:
        xalign 0.581
        yalign 0.82
        idle "Images/Plans/Allee/garage.png"
        hover "Images/Plans/Allee/garage_hover.png"
        action Jump("garage")

    if vanzilla == True and heure < 9 or vanzilla == True and heure > 17:
        imagebutton:
            xalign 0.9
            yalign 1.0
            idle "Images/Plans/Allee/vanzilla.png"
            hover "Images/Plans/Allee/vanzilla_hover.png"
            action Jump("vanzilla")

label allee:
    scene BG_allee
    with fondu
    call screen allee

label vanzilla:
    if permis == False:
        show screen User("normal", "_P")
        with fondu
        user "Faudrait que je pense à passer mon permis..."
        hide screen User
        jump allee
    elif True:
        $ time_car = 10
        $ pos_bad_car = 0
        $ pos_car = 1
        call screen conduite("ville")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
