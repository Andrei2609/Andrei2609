
image BG_gen_shop_back = "Images/Backgrounds/shop_back_4.png"

screen general_mall():
    modal True
    zorder 100
    vbox:
        xsize 650
        xalign 0.5
        yalign 0.5
        grid 5 2:
            spacing 10
            xalign 0.5
            yalign 0.5
            use obj_shop("general", mouchoir, "mouchoir", 2)
            use obj_shop("general", bonbon, "bonbon", 8)
            use obj_shop("general", chocolat, "chocolat", 10)
            use obj_shop("general", clopes, "clopes", 10)
            use obj_shop("general", fleur, "fleur", 20)
            use obj_shop("general", eau, "eau", 15)
            use obj_shop("general", alcool, "alcool", 35)
            use obj_shop("general", halteres, "halteres", 15)
            use obj_shop("general", journal, "journal", 5)
            if tournevis == 0:
                use obj_shop("general", tournevis, "tournevis", 20)
            else:
                null
        imagebutton:
            xalign 0.01
            yalign 0.99
            idle "Images/Bases/Icones/Faces/face_retour.png"
            hover "Images/Bases/Icones/Faces/face_retour_hover.png"
            action Jump("General_shop")

screen general_caisse():
    imagebutton:
        xalign 0.953
        yalign 0.487
        idle "Images/Plans/Centre_Commercial/gen_porte.png"
        hover "Images/Plans/Centre_Commercial/gen_porte_hover.png"
        action Jump("mall_in")

    imagebutton:
        xalign 0.25
        yalign 0.515
        idle "Images/Plans/Centre_Commercial/shop_girl_1.png"
        hover "Images/Plans/Centre_Commercial/shop_girl_1_hover.png"
        action Jump("general_girl")

label General_shop:
    $ checkZone = "mall_general"
    hide screen Actor1
    scene BG_gen_shop_back
    with fondu
    call screen general_caisse

label General_shop_prod:
    hide screen Actor1
    call screen general_mall

label general_girl:
    show screen Actor1("shop_girl_1", "job", "normal", "sh_0", "sb_1", "job", "boucle_1", "percing_1", "", "Neutre", "P")
    with fondu
    shop_girl_1 "Bienvenue, ça sera quoi pour vous ?"
    show screen Actor1("shop_girl_1", "job", "normal", "sh_0", "sb_1", "job", "boucle_1", "percing_1", "", "Neutre", "")
    call screen shop_girl_1_option

label general_girl_talk:
    show screen Actor1("shop_girl_1", "job", "normal", "sh_0", "sb_1", "job", "boucle_1", "percing_1", "", "Neutre", "")
    with fondu
    call screen shop_girl_1_talk
    hide screen Actor1
    jump General_shop
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
