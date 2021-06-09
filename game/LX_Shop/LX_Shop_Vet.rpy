
image BG_vet_shop_back = "Images/Backgrounds/shop_vet_1.png"
image BG_vet_shop_cabine = "Images/Backgrounds/shop_vet_2.png"
image BG_cabine = "Images/Backgrounds/cabine_essayage.png"

screen vet_mall():
    modal True
    zorder 100
    vbox:
        xsize 650
        xalign 0.5
        yalign 0.5
        grid 3 2:
            xalign 0.5
            spacing 10
            use obj_shop("vet", mouchoir, "mouchoir", 2)
            use obj_shop("vet", boucle, "boucle", 50)
            use obj_shop("vet", lingerie_sexy, "lingerie_sexy", 100)
            if pomgirl_1 == 0:
                use obj_shop("vet", pomgirl_1, "pomgirl_1", 75)
            else:
                null
            if pomgirl_2 == 0:
                use obj_shop("vet", pomgirl_2, "pomgirl_2", 75)
            else:
                null
            null
        imagebutton:
            xalign 0.01
            yalign 0.99
            idle "Images/Bases/Icones/Faces/face_retour.png"
            hover "Images/Bases/Icones/Faces/face_retour_hover.png"
            action Jump("Vet_shop")

screen vet_caisse():
    if tissu_leni_1 <> "win":
        imagebutton:
            xalign 0.2
            yalign 0.4918
            idle "Images/Plans/Centre_Commercial/fiona_caisse.png"
            hover "Images/Plans/Centre_Commercial/fiona_caisse_hover.png"
            action Jump("vet_fiona")
    elif jour == 3 and heure > 13 and heure < 19 or jour == 6 and heure > 14 and heure < 19:
        imagebutton:
            xalign 0.25
            yalign 0.515
            idle "Images/Plans/Centre_Commercial/leni_caisse.png"
            hover "Images/Plans/Centre_Commercial/leni_caisse_hover.png"
            action Jump("vet_l2")
    else:
        imagebutton:
            xalign 0.2
            yalign 0.4918
            idle "Images/Plans/Centre_Commercial/fiona_caisse.png"
            hover "Images/Plans/Centre_Commercial/fiona_caisse_hover.png"
            action Jump("vet_fiona")

    imagebutton:
        xalign 0.01
        yalign 0.99
        idle "Images/Plans/Centre_Commercial/hall.png"
        hover "Images/Plans/Centre_Commercial/hall_hover.png"
        action Jump("mall_in")

    imagebutton:
        xalign 0.99
        yalign 0.5
        idle "Images/Plans/Minis/flecheD.png"
        hover "Images/Plans/Minis/flecheD_hover.png"
        action Jump("Vet_shop_2")

screen vet_cabine():
    imagebutton:
        xalign 0.25
        yalign 0.8
        idle "Images/Plans/Minis/flecheH.png"
        hover "Images/Plans/Minis/flecheH_hover.png"
        action Jump("Vet_shop")

    imagebutton:
        xalign 0.85
        yalign 0.5
        idle "Images/Plans/Minis/peek.png"
        hover "Images/Plans/Minis/peek_hover.png"
        action Jump("peek_vet_shop")

    if jour == 1 or jour == 2 or jour == 4 or jour == 5 and heure > 12 and heure < 15:
        imagebutton:
            xalign 0.05
            yalign 0.6
            idle "Images/Plans/Centre_Commercial/l2.png"
            hover "Images/Plans/Centre_Commercial/l2_hover.png"
            action Jump("vet_l2_talk")

label Vet_shop:
    $ checkZone = "mall_vet_1"
    hide screen Actor1
    scene BG_vet_shop_back
    with fondu
    call screen vet_caisse

label Vet_shop_2:
    $ checkZone = "mall_vet_2"
    scene BG_vet_shop_cabine
    with fondu
    call screen vet_cabine

label Vet_shop_prod:
    hide screen Actor1
    call screen vet_mall

label vet_fiona:
    show screen Actor1("fiona", "normal", "normal", "sh_1", "sb_1", "job", "foulard_1", "", "", "Neutre", "P")
    with fondu
    fiona "Bonjour, je peux vous aidez ?"
    show screen Actor1("fiona", "normal", "normal", "sh_1", "sb_1", "job", "foulard_1", "", "", "Neutre", "")
    call screen fiona_option

label vet_fiona_talk:
    show screen Actor1("fiona", "normal", "normal", "sh_1", "sb_1", "job", "foulard_1", "", "", "Neutre", "")
    with fondu
    call screen fiona_talk
    hide screen Actor1
    jump Vet_shop

label vet_l2:
    show screen Actor1("l2", "nue", "normal", "sh_1", "sb_1", "job", "boucle_1", "lunettes", "", "Joyeux", "P")
    with fondu
    l2 "Salut Lincoln, Tu veux quelques choses ?"
    show screen Actor1("l2", "nue", "normal", "sh_1", "sb_1", "job", "boucle_1", "lunettes", "", "Joyeux", "")
    call screen l2_option

label vet_l2_talk:
    show screen Actor1("l2", "nue", "normal", "sh_1", "sb_1", "job", "boucle_1", "lunettes", "", "Joyeux", "")
    with fondu
    call screen l2_talk
    hide screen Actor1
    if jour == 1 or jour == 2 or jour == 4 or jour == 5 and heure > 12 and heure < 15:
        jump Vet_shop_2
    elif True:
        jump Vet_shop

label peek_vet_shop:
    call timer (0, 5) from _call_timer_53
    $ sex_points += 10
    $ int_points += 1
    show screen peekShop("BG_cabine")
    nar ""
    hide screen peekShop
    jump Vet_shop_2

label tissu_quete_shop:
    fiona "Du tissu... Il doit nous rester quelques vieux morceaux en réserve.{w} \nMais c'est pas gratuit ! 2 $ le morceau ça te va ?"

    menu:
        "Oui" if True:
            jump tissu_quete_shop_2
        "Non" if True:
            hide screen Actor1
            jump Vet_shop

label tissu_quete_shop_2:
    $ user_coins -= 2
    show screen Actor1("fiona", "normal", "normal", "sh_1", "sb_1", "job", "foulard_1", "", "", "Neutre", "P")
    fiona "Attends..."
    hide screen Actor1
    nar "Après un moment..."
    call timer (0, 10) from _call_timer_54
    show screen Actor1("fiona", "normal", "normal", "sh_1", "sb_1", "job", "foulard_1", "", "", "Neutre", "P")
    fiona "Il nous reste trois morceaux tu veux lequel ?"
    show screen Actor1("fiona", "normal", "normal", "sh_1", "sb_1", "job", "foulard_1", "", "", "Neutre", "")
    call screen choixTissu1()
    show screen Actor1("fiona", "normal", "normal", "sh_1", "sb_1", "job", "foulard_1", "", "", "Neutre", "P")
    fiona "Merci, à la prochaine !"
    hide screen Actor1
    jump Vet_shop

screen choixTissu1():
    frame:
        xalign 0.5
        yalign 0.5
        has vbox
        text _("Choisis la couleur du tissu") xalign 0.5
        hbox:
            imagebutton:
                idle "Images/Objets/item_tissu_rouge.png"
                hover "Images/Objets/item_tissu_rouge_hover.png"
                action SetVariable("tissu_leni_1", "rouge"), Return(True)
            imagebutton:
                idle "Images/Objets/item_tissu_bleu.png"
                hover "Images/Objets/item_tissu_bleu_hover.png"
                action SetVariable("tissu_leni_1", "bleu"), Return(True)
            imagebutton:
                idle "Images/Objets/item_tissu_vert.png"
                hover "Images/Objets/item_tissu_vert_hover.png"
                action SetVariable("tissu_leni_1", "vert"), Return(True)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
