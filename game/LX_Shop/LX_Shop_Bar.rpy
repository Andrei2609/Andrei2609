
image BG_bar = "Images/Backgrounds/bar.png"

screen bar():
    if jour < 7 and heure < 19:
        imagebutton:
            xalign 0.7
            yalign 0.05
            idle "Images/Plans/Centre_Commercial/luna_bar.png"
            hover "Images/Plans/Centre_Commercial/luna_bar_hover.png"
            action Jump("bar_l3")
    else:
        imagebutton:
            xalign 1.0
            yalign 1.0
            idle "Images/Plans/Centre_Commercial/bar.png"
            hover "Images/Plans/Centre_Commercial/bar_hover.png"
            action Jump("Bar_shop")

    imagebutton:
        xalign 0.01
        yalign 0.99
        idle "Images/Plans/Centre_Commercial/hall.png"
        hover "Images/Plans/Centre_Commercial/hall_hover.png"
        action Jump("mall_in")

label Bar_shop:
    $ checkZone = "mall_bar"
    scene BG_bar
    with fondu
    call screen bar

label bar_l3:
    show screen Actor1("l3", "nue", "normal", "sh_0", "sb_1", "job", "boucle_1", "bracelet_1", "collier_1", "Neutre", "P")
    with fondu
    l3 "Hey Brother ! Qu'est-ce que tu fais là ?"
    show screen Actor1("l3", "nue", "normal", "sh_0", "sb_1", "job", "boucle_1", "bracelet_1", "collier_1", "Neutre", "")
    call screen l3_talk
    hide screen Actor1
    jump Bar_shop
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
