
label l4_quest_1_fin:
    $ coco_jambe_1 = "win"
    scene BG_luna_luan
    show screen Actor1("l3", "nue", "normal", "", "", "normal", "boucle_1", "bracelet_1", "collier_1", "Neutre", "")
    with fondu
    show screen User(tenue, "")
    with inL
    user "Luna, tu n'aurais pas vu Luan ?"
    show screen Actor1("l3", "nue", "normal", "", "", "normal", "boucle_1", "bracelet_1", "collier_1", "Neutre", "P")
    show screen User(tenue, "I")
    with fondu
    l3 "Si, elle se prépare pour l'école. {w}Pourquoi ?"
    show screen Actor1("l3", "nue", "normal", "", "", "normal", "boucle_1", "bracelet_1", "collier_1", "Neutre", "")
    show screen User(tenue, "_P")
    with fondu
    user "J'ai retrouvé la jambe de monsieur Coco."
    show screen User(tenue, "I")
    hide screen Actor1
    show screen Actor2("l3", "nue", "normal", "", "", "normal", "boucle_1", "bracelet_1", "collier_1", "Neutre", "")
    with fondu
    show screen Actor1("l4", "nue", "normal", "sh_1", "sb_1", "", "", "", "", "Neutre", "P")
    with inL
    l4 "LA JAMBE DE MONSIEUR COCO !"
    show screen Actor1("l4", "nue", "normal", "sh_1", "sb_1", "", "", "", "", "Neutre", "")
    with fondu
    hide screen Actor1
    hide screen Actor2
    show Luan_zoom_1
    with flash
    nar ""
    hide Luan_zoom_1
    with fondu
    $ sex_points += 5
    show screen Actor1("l4", "nue", "normal", "sh_1", "sb_1", "", "", "", "", "Neutre", "")
    show screen Actor2("l3", "nue", "normal", "", "", "normal", "boucle_1", "bracelet_1", "collier_1", "Neutre", "")
    show screen User(tenue, "_P")
    show coco_jambe:
        xalign 0.34
        yalign 0.5
    with fondu
    user "Oui, la voici. {w}Ça devait pas être le pied pour monsieur Coco!"
    hide coco_jambe
    with fondu
    show screen Actor1("l4", "nue", "normal", "sh_1", "sb_1", "", "", "", "", "Neutre", "P")
    show screen User(tenue, "I")
    with fondu
    l4 "Tu l'as dis. Le pauvre, il s'est réveillé du mauvais pied avec tout ça ! Hahahahaha... {w}T'as compris ?"

    show screen Actor2("l3", "nue", "normal", "", "", "normal", "boucle_1", "bracelet_1", "collier_1", "Colere", "P")
    show screen Actor1("l4", "joyeux", "normal", "sh_1", "sb_1", "", "", "", "", "Rire", "P")
    show screen User(tenue, "_Ha")
    with fondu
    l3 "C'est pas vrai... Maintenant ils sont deux !"
    show screen Actor2("l3", "nue", "normal", "", "", "normal", "boucle_1", "bracelet_1", "collier_1", "Colere", "")
    show screen Actor1("l4", "nue", "normal", "sh_1", "sb_1", "", "", "", "", "Rougir", "P")
    show screen User(tenue, "I")
    l4 "Plus sérieusement, je dois m'habiller ! {w}\nDonc ça veut dire que c'est l'heure de partir pour toi !"

    show screen Actor1("l4", "nue", "normal", "sh_1", "sb_1", "", "", "", "", "Rougir", "")
    show screen User(tenue, "_P")
    user "Oui bien sûr !"

    $ love_l4_points += 10
    $ love_l3_points += 5
    $ sex_l4_points += 5
    $ warn_loud_points -= 5

    $ sex_points += 5

    hide screen Actor2
    hide screen Actor1
    hide screen User
    with outR
    jump couloir
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
