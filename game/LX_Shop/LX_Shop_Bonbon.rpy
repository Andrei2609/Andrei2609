
image BG_bonbon_shop_back = "Images/Backgrounds/shop_back_5.png"

screen bonbon_mall():
    modal True
    zorder 100
    vbox:
        xsize 650
        xalign 0.5
        yalign 0.5
        hbox:
            spacing 10
            xalign 0.5
            yalign 0.5
            use obj_shop("bonbon", bonbon, "bonbon", 5)
            use obj_shop("bonbon", chocolat, "chocolat", 5)
        imagebutton:
            xalign 0.01
            yalign 0.99
            idle "Images/Bases/Icones/Faces/face_retour.png"
            hover "Images/Bases/Icones/Faces/face_retour_hover.png"
            action Jump("Bonbon_shop")

screen bonbon_caisse():
    imagebutton:
        xalign 0.5
        yalign 0.539
        idle "Images/Plans/Centre_Commercial/candy_girl.png"
        hover "Images/Plans/Centre_Commercial/candy_girl_hover.png"
        action Jump("candy_girl")

    imagebutton:
        xalign 0.01
        yalign 0.99
        idle "Images/Plans/Centre_Commercial/hall.png"
        hover "Images/Plans/Centre_Commercial/hall_hover.png"
        action Jump("mall_in")

label Bonbon_shop:
    $ checkZone = "mall_bonbon"
    hide screen Actor1
    scene BG_bonbon_shop_back
    with fondu
    call screen bonbon_caisse

label Bonbon_shop_prod:
    hide screen Actor1
    call screen bonbon_mall

label candy_girl:
    show screen Actor1("candy_girl", "nue", "normal", "sh_0", "sb_1", "job", "percing_1", "boucle_1", "", "Neutre", "P")
    with fondu
    candy_girl "Salut, en quoi je peux vous aidez ?"
    show screen Actor1("candy_girl", "nue", "normal", "sh_0", "sb_1", "job", "percing_1", "boucle_1", "", "Neutre", "")
    call screen candy_girl_option

label candy_girl_talk:
    show screen Actor1("candy_girl", "nue", "normal", "sh_0", "sb_1", "job", "percing_1", "boucle_1", "", "Neutre", "")
    with fondu
    call screen candy_girl_talk
    hide screen Actor1
    jump Bonbon_shop
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
