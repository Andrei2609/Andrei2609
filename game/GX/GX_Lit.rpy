init:
    $ compt_couette = 0

screen sex_sleep():
    $ fille = "Images/Mini-Jeux/Lit/" + idFille + "/girl.png"
    $ fille_hover = "Images/Mini-Jeux/Lit/" + idFille + "/girl_hover.png"
    $ couette_1 = "Images/Mini-Jeux/Lit/" + idFille + "/couette_1.png"
    $ couette_1_hover = "Images/Mini-Jeux/Lit/" + idFille + "/couette_1_hover.png"
    $ couette_2 = "Images/Mini-Jeux/Lit/" + idFille + "/couette_2.png"
    $ couette_2_hover = "Images/Mini-Jeux/Lit/" + idFille + "/couette_2_hover.png"
    $ couette_3 = "Images/Mini-Jeux/Lit/" + idFille + "/couette_3.png"
    $ couette_3_hover = "Images/Mini-Jeux/Lit/" + idFille + "/couette_3_hover.png"
    $ coussin = "Images/Mini-Jeux/Lit/" + idFille + "/coussin.png"

    add coussin

    if compt_couette == 3:
        imagebutton:
            xalign 0.35
            yalign 1.0
            idle fille
            hover fille_hover
            action Jump("action_lit")
    else:
        add fille

    if compt_couette == 0:
        imagebutton:
            xalign 0.0
            yalign 1.0
            idle couette_1
            hover couette_1_hover
            action SetVariable("compt_couette", 1)
    elif compt_couette == 1:
        imagebutton:
            xalign 0.0
            yalign 1.0
            idle couette_2
            hover couette_2_hover
            action SetVariable("compt_couette", 2)
    elif compt_couette == 2:
        imagebutton:
            xalign 0.0
            yalign 1.0
            idle couette_3
            hover couette_3_hover
            action SetVariable("compt_couette", 3)

    imagebutton:
        xalign 0.01
        yalign 0.1
        idle "Images/Bases/Icones/Faces/face_retour.png"
        hover "Images/Bases/Icones/Faces/face_retour_hover.png"
        action Jump("quit_lit")

screen sex_sleep_girl():
    $ fille = "Images/Mini-Jeux/Lit/" + idFille + "/girl.png"

    add fille

label action_lit:
    show screen sex_sleep_girl
    user "Elle dort profondément..."
    user "ça serais méchant de profiter d'elle ainsi..."
    user "Une prochaine fois !"
    hide screen sex_sleep_girl
    jump quit_lit

label quit_lit:
    $ compt_couette = 0
    if idFille == "l1" or idFille == "l2":
        $ idFille = ""
        jump ch_in_l1_l2
    elif idFille == "l3" or idFille == "l4":
        $ idFille = ""
        jump ch_in_l3_l4
    elif idFille == "l5":
        $ idFille = ""
        jump ch_in_l5_l7
    elif idFille == "mom":
        $ idFille = ""
        jump ch_in_mom
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
