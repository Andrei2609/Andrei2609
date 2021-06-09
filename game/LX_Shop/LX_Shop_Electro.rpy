
image BG_electro_shop_back = "Images/Backgrounds/shop_back_3.png"

screen electro_mall():
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
            use obj_shop("techno", usb, "usb", 20)
            if radio == 0:
                use obj_shop("techno", radio, "radio", 20)
            else:
                null
            if phone == 0:
                use obj_shop("techno", phone, "phone", 500)
            else:
                null
            if tournevis == 0:
                use obj_shop("techno", tournevis, "tournevis", 20)
            else:
                null
            if ordiUser == 0:
                use obj_shop("techno", ordiUser, "ordiUser", 500)
            else:
                null
            null
        imagebutton:
            xalign 0.01
            yalign 0.99
            idle "Images/Bases/Icones/Faces/face_retour.png"
            hover "Images/Bases/Icones/Faces/face_retour_hover.png"
            action Jump("Electro_shop")

screen electro_caisse():
    imagebutton:
        xalign 0.25
        yalign 0.28
        idle "Images/Plans/Centre_Commercial/electro_girl.png"
        hover "Images/Plans/Centre_Commercial/electro_girl_hover.png"
        action Jump("electro_girl")

    imagebutton:
        xalign 0.99
        yalign 0.99
        idle "Images/Plans/Centre_Commercial/hall.png"
        hover "Images/Plans/Centre_Commercial/hall_hover.png"
        action Jump("mall_in")

label Electro_shop:
    $ checkZone = "mall_electro"
    hide screen Actor1
    scene BG_electro_shop_back
    with fondu
    call screen electro_caisse

label Electro_shop_prod:
    hide screen Actor1
    call screen electro_mall

label electro_girl:
    show screen Actor1("electro_girl", "job", "normal", "sh_1", "sb_1", "jobA", "boucle_1", "colier_1", "lunette_1", "Neutre", "P")
    with fondu
    electro_girl "Salut, en quoi je peux vous aidez ?"
    show screen Actor1("electro_girl", "job", "normal", "sh_1", "sb_1", "jobA", "boucle_1", "colier_1", "lunette_1", "Neutre", "")
    call screen electro_girl_option

label electro_girl_talk:
    show screen Actor1("electro_girl", "job", "normal", "sh_1", "sb_1", "jobA", "boucle_1", "colier_1", "lunette_1", "Neutre", "")
    with fondu
    call screen electro_girl_talk
    hide screen Actor1
    jump Electro_shop
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
