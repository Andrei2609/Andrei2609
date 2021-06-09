
image BG_flip = "Images/Backgrounds/flip.png"
image BG_flip_shop = "Images/Backgrounds/flip_shop.png"

image user_work_flip = "Images/CG/05-User/user_flip.png"

screen flip_shop():
    vbox:
        xalign 0.3
        yalign 0.6
        grid 4 2:
            spacing 10
            xalign 0.5
            yalign 0.5
            use obj_shop("flip", flipi_citron, "flipi_citron", 10)
            use obj_shop("flip", flipi_fraise, "flipi_fraise", 10)
            use obj_shop("flip", flipi_framboise_bleu, "flipi_framboise_bleu", 10)
            use obj_shop("flip", flipi_framboise, "flipi_framboise", 10)
            use obj_shop("flip", flipi_kiwi, "flipi_kiwi", 10)
            use obj_shop("flip", flipi_pastheque, "flipi_pastheque", 10)
            use obj_shop("flip", flipi_raisin, "flipi_raisin", 10)
            null
        text ""
        frame:
            xalign 0.5
            yalign 0.5
            textbutton _("Rien"):
                action Jump("flip_in_2")

screen flip_ext():
    imagebutton:
        xalign 0.99
        yalign 0.99
        idle "Images/Plans/Minis/flecheBD.png"
        hover "Images/Plans/Minis/flecheBD_hover.png"
        action Jump("map")

    frame:
        xalign 0.5
        yalign 0.7
        imagebutton:
            idle "Images/Plans/Minis/porte.png"
            hover "Images/Plans/Minis/porte_hover.png"
            action Jump("flip_in")

label flip:
    call timer (0, 10) from _call_timer_7
    jump flip_2

label flip_2:
    $ checkZone = "flip_out"
    scene BG_flip
    with fondu
    call screen flip_ext

label flip_in:
    $ checkZone = "flip_in"
    scene BG_flip_shop
    show Flip_P at right
    with fondu
    flip "Bonjour !"
    label flip_in_2:
    hide I_Flip
    show Flip_P at right
    with fondu
    menu:
        "Voir pour un job" if flip_job == False:
            flip "Tu veux travailler ? {w}\nOk, mais c'est 5 $ de l'heure à prendre où laisser !"

            $ flip_job = True
            jump flip_in_2
        "Travailler 1h" if flip_job ==True and vie_points >= 10:
            show user_work_flip
            with fondu
            nar ""
            $ user_coins += 5
            $ vie_points -= 10
            hide user_work_flip
            with fondu
            call timer (1, 0) from _call_timer_8
            flip "Tiens ton salaire"
            jump flip_in_2
        "Acheter" if True:
            hide Flip_P
            show I_Flip at right
            with fondu
            call screen flip_shop
        "Partir" if True:
            flip "Bonne journée !"
            hide Flip_P
            with fondu
            jump flip_2
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
