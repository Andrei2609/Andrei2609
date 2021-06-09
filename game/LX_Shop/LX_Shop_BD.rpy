
image BG_BD_shop_back = "Images/Backgrounds/shop_back_2.png"

screen BD_mall():
    modal True
    zorder 100
    vbox:
        xsize 650
        xalign 0.5
        yalign 0.5
        grid 3 2:
            spacing 10
            xalign 0.5
            yalign 0.5
            use obj_shop("BD", book_1, "book_1", 15)
            use obj_shop("BD", book_2, "book_2", 15)
            use obj_shop("BD", book_3, "book_3", 15)
            use obj_shop("BD", book_princess_pony, "book_princess_pony", 20)
            use obj_shop("BD", journal, "journal", 5)
            null
        imagebutton:
            xalign 0.01
            yalign 0.99
            idle "Images/Bases/Icones/Faces/face_retour.png"
            hover "Images/Bases/Icones/Faces/face_retour_hover.png"
            action Jump("BD_shop")


screen BD_caisse():
    imagebutton:
        xalign 0.5
        yalign 0.32
        idle "Images/Plans/Centre_Commercial/BD_girl.png"
        hover "Images/Plans/Centre_Commercial/BD_girl_hover.png"
        action Jump("BD_girl")

    imagebutton:
        xalign 0.99
        yalign 0.99
        idle "Images/Plans/Centre_Commercial/hall.png"
        hover "Images/Plans/Centre_Commercial/hall_hover.png"
        action Jump("mall_in")

label BD_shop:
    $ checkZone = "mall_BD"
    hide screen Actor1
    scene BG_BD_shop_back
    with fondu
    call screen BD_caisse

label BD_shop_prod:
    hide screen Actor1
    call screen BD_mall

label BD_girl:
    show screen Actor1("BD_girl", "nue", "normal", "sh_1", "sb_1", "job", "boucle_1", "", "", "Neutre", "P")
    with fondu
    BD_girl "Salut, en quoi je peux vous aidez ?"
    show screen Actor1("BD_girl", "nue", "normal", "sh_1", "sb_1", "job", "boucle_1", "", "", "Neutre", "")
    call screen BD_girl_option

label BD_girl_talk:
    show screen Actor1("BD_girl", "nue", "normal", "sh_1", "sb_1", "job", "boucle_1", "", "", "Neutre", "")
    with fondu
    call screen BD_girl_talk
    hide screen Actor1
    jump BD_shop
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
