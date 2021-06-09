init:
    $ choix_user_box = ""
    $ userTX = 1
    $ userPTS = 0
    $ playerBM = ""
    $ playerTX = 1
    $ playerPTS = 0

screen mysteryBox():
    imagemap:
        idle "Images/Mini-Jeux/Box/box.png"
        hover "Images/Mini-Jeux/Box/box_hover.png"
        xalign 0.5
        yalign 0.5

        hotspot (31,22,98,69) action Return(True)

        hotspot (61,557,100,100):
            if userPTS == 5 or playerPTS == 5:
                action Jump("box_end")
            else:
                action SetVariable("userTX", 1), Jump("box_main")
        hotspot (167,557,100,100):
            if userPTS == 5 or playerPTS == 5:
                action Jump("box_end")
            else:
                action SetVariable("userTX", 1), Jump("box_balle")
        hotspot (273,557,100,100):
            if userPTS == 5 or playerPTS == 5:
                action Jump("box_end")
            else:
                action SetVariable("userTX", 3), Jump("box_slime")
        hotspot (377,557,100,100):
            if userPTS == 5 or playerPTS == 5:
                action Jump("box_end")
            else:
                action SetVariable("userTX", 1), Jump("box_tissu")
        hotspot (483,557,100,100):
            if userPTS == 5 or playerPTS == 5:
                action Jump("box_end")
            else:
                action SetVariable("userTX", 2), Jump("box_banane")
        hotspot (588,557,100,100):
            if userPTS == 5 or playerPTS == 5:
                action Jump("box_end")
            else:
                action SetVariable("userTX", 3), Jump("box_sex")
    frame:
        xalign 0.9
        yalign 0.01
        background None
        has vbox
        text _("6 points = Victoire") xalign 0.5
        hbox:
            spacing 5
            xalign 0.5
            frame:
                xalign 0.5
                has vbox
                label "Lincoln" xalign 0.5
                text _("pts = [userPTS]") xalign 0.5
            frame:
                xalign 0.5
                has vbox
                label playerBM xalign 0.5
                text _("pts = [playerPTS]") xalign 0.5

label box_end:
    if playerPTS > userPTS:
        user "J'ai perdu..."
    elif playerPTS < userPTS:
        user "J'ai gagner !!!"
    elif playerPTS == userPTS:
        user "Egalité."
    $ userPTS = 0
    $ playerPTS = 0
    $ userPTS = 0
    return

label box_main:
    if talkCible == "mom":
        if playerTX > userTX:
            mom "Une main !"
            user "gagner !"
            $ playerPTS += 1
        elif True:
            mom "un pied !"
            user "perdu !"
            $ userPTS += 1
    elif talkCible == "l1":
        if playerTX > userTX:
            l1 "Une main !"
            user "gagner !"
            $ playerPTS += 1
        elif True:
            l1 "un pied !"
            user "perdu !"
            $ userPTS += 1
    elif talkCible == "l2":
        if playerTX > userTX:
            l2 "Une main !"
            user "gagner !"
            $ playerPTS += 1
        elif True:
            l2 "un pied !"
            user "perdu !"
            $ userPTS += 1
    elif talkCible == "l3":
        if playerTX > userTX:
            l3 "Une main !"
            user "gagner !"
            $ playerPTS += 1
        elif True:
            l3 "un pied !"
            user "perdu !"
            $ userPTS += 1
    elif talkCible == "l4":
        if playerTX > userTX:
            l4 "Une main !"
            user "gagner !"
            $ playerPTS += 1
        elif True:
            l4 "un pied !"
            user "perdu !"
            $ userPTS += 1
    elif talkCible == "l5":
        if playerTX > userTX:
            l5 "Une main !"
            user "gagner !"
            $ playerPTS += 1
        elif True:
            l5 "un pied !"
            user "perdu !"
            $ userPTS += 1
    call screen mysteryBox

label box_balle:
    if talkCible == "mom":
        if playerTX > userTX:
            mom "Une balle !"
            user "gagner !"
            $ playerPTS += 1
        elif True:
            mom "Une paire de chaussettes !"
            user "perdu !"
            $ userPTS += 1
    elif talkCible == "l1":
        if playerTX > userTX:
            l1 "Une balle !"
            user "gagner !"
            $ playerPTS += 1
        elif True:
            l1 "Une paire de chaussettes !"
            user "perdu !"
            $ userPTS += 1
    elif talkCible == "l2":
        if playerTX > userTX:
            l2 "Une balle !"
            user "gagner !"
            $ playerPTS += 1
        elif True:
            l2 "Une paire de chaussettes !"
            user "perdu !"
            $ userPTS += 1
    elif talkCible == "l3":
        if playerTX > userTX:
            l3 "Une balle !"
            user "gagner !"
            $ playerPTS += 1
        elif True:
            l3 "Une paire de chaussettes !"
            user "perdu !"
            $ userPTS += 1
    elif talkCible == "l4":
        if playerTX > userTX:
            l4 "Une balle !"
            user "gagner !"
            $ playerPTS += 1
        elif True:
            l4 "Une paire de chaussettes !"
            user "perdu !"
            $ userPTS += 1
    elif talkCible == "l5":
        if playerTX > userTX:
            l5 "Une balle !"
            user "gagner !"
            $ playerPTS += 1
        elif True:
            l5 "Une paire de chaussettes !"
            user "perdu !"
            $ userPTS += 1
    call screen mysteryBox

label box_slime:
    if talkCible == "mom":
        if playerTX > userTX:
            mom "Du slime !"
            user "gagner !"
            $ playerPTS += 1
        elif True:
            mom "Du sperme !"
            user "perdu !"
            $ userPTS += 1
    elif talkCible == "l1":
        if playerTX > userTX:
            l1 "Du slime !"
            user "gagner !"
            $ playerPTS += 1
        elif True:
            l1 "Du sperme !"
            user "perdu !"
            $ userPTS += 1
    elif talkCible == "l2":
        if playerTX > userTX:
            l2 "Du slime !"
            user "gagner !"
            $ playerPTS += 1
        elif True:
            l2 "Du sperme !"
            user "perdu !"
            $ userPTS += 1
    elif talkCible == "l3":
        if playerTX > userTX:
            l3 "Du slime !"
            user "gagner !"
            $ playerPTS += 1
        elif True:
            l3 "Du sperme !"
            user "perdu !"
            $ userPTS += 1
    elif talkCible == "l4":
        if playerTX > userTX:
            l4 "Du slime !"
            user "gagner !"
            $ playerPTS += 1
        elif True:
            l4 "Du sperme !"
            user "perdu !"
            $ userPTS += 1
    elif talkCible == "l5":
        if playerTX > userTX:
            l5 "Du slime !"
            user "gagner !"
            $ playerPTS += 1
        elif True:
            l5 "Du sperme !"
            user "perdu !"
            $ userPTS += 1
    call screen mysteryBox

label box_tissu:
    if talkCible == "mom":
        if playerTX > userTX:
            mom "Un mouchoir !"
            user "gagner !"
            $ playerPTS += 1
        elif True:
            mom "Une culotte !"
            user "perdu !"
            $ userPTS += 1
    elif talkCible == "l1":
        if playerTX > userTX:
            l1 "Un mouchoir !"
            user "gagner !"
            $ playerPTS += 1
        elif True:
            l1 "Une culotte !"
            user "perdu !"
            $ userPTS += 1
    elif talkCible == "l2":
        if playerTX > userTX:
            l2 "Un mouchoir !"
            user "gagner !"
            $ playerPTS += 1
        elif True:
            l2 "Une culotte !"
            user "perdu !"
            $ userPTS += 1
    elif talkCible == "l3":
        if playerTX > userTX:
            l3 "Un mouchoir !"
            user "gagner !"
            $ playerPTS += 1
        elif True:
            l3 "Une culotte !"
            user "perdu !"
            $ userPTS += 1
    elif talkCible == "l4":
        if playerTX > userTX:
            l4 "Un mouchoir !"
            user "gagner !"
            $ playerPTS += 1
        elif True:
            l4 "Une culotte !"
            user "perdu !"
            $ userPTS += 1
    elif talkCible == "l5":
        if playerTX > userTX:
            l5 "Un mouchoir !"
            user "gagner !"
            $ playerPTS += 1
        elif True:
            l5 "Une culotte !"
            user "perdu !"
            $ userPTS += 1
    call screen mysteryBox

label box_banane:
    if talkCible == "mom":
        if playerTX > userTX:
            mom "Une banane !"
            user "gagner !"
            $ playerPTS += 1
        elif True:
            mom "Une carotte !"
            user "perdu !"
            $ userPTS += 1
    elif talkCible == "l1":
        if playerTX > userTX:
            l1 "Une banane !"
            user "gagner !"
            $ playerPTS += 1
        elif True:
            l1 "Une carotte !"
            user "perdu !"
            $ userPTS += 1
    elif talkCible == "l2":
        if playerTX > userTX:
            l2 "Une banane !"
            user "gagner !"
            $ playerPTS += 1
        elif True:
            l2 "Une carotte !"
            user "perdu !"
            $ userPTS += 1
    elif talkCible == "l3":
        if playerTX > userTX:
            l3 "Une banane !"
            user "gagner !"
            $ playerPTS += 1
        elif True:
            l3 "Une carotte !"
            user "perdu !"
            $ userPTS += 1
    elif talkCible == "l4":
        if playerTX > userTX:
            l4 "Une banane !"
            user "gagner !"
            $ playerPTS += 1
        elif True:
            l4 "Une carotte !"
            user "perdu !"
            $ userPTS += 1
    elif talkCible == "l5":
        if playerTX > userTX:
            l5 "Une banane !"
            user "gagner !"
            $ playerPTS += 1
        elif True:
            l5 "Une carotte !"
            user "perdu !"
            $ userPTS += 1
    call screen mysteryBox

label box_sex:
    if talkCible == "mom":
        if playerTX > userTX:
            if love_mom_points >= 50:
                $ sex_mom_points += 20
                $ love_mom_points += 10
                mom "Ta bite !"
                $ playerPTS += 1
            elif True:
                $ sex_mom_points += 5
                $ love_mom_points -= 10
                $ warn_mom_points += 10
                mom "Nooonnn ! Beurk !"
        elif True:
            mom "une saucisse !"
            user "perdu !"
            $ userPTS += 1
    elif talkCible == "l1":
        if playerTX > userTX:
            if love_l1_points >= 50:
                $ sex_l1_points += 20
                $ love_l1_points += 10
                l1 "Ta bite !"
                $ playerPTS += 1
            elif True:
                $ sex_l1_points += 5
                $ love_l1_points -= 10
                $ warn_l1_points += 10
                l1 "Nooonnn ! Beurk !"
        elif True:
            l1 "une saucisse !"
            user "perdu !"
            $ userPTS += 1
    elif talkCible == "l2":
        if playerTX > userTX:
            if love_l2_points >= 50:
                $ sex_l2_points += 20
                $ love_l2_points += 10
                l2 "Ta bite !"
                $ playerPTS += 1
            elif True:
                $ sex_l2_points += 5
                $ love_l2_points -= 10
                $ warn_l2_points += 10
                l2 "Nooonnn ! Beurk !"
        elif True:
            l2 "une saucisse !"
            user "perdu !"
            $ userPTS += 1
    elif talkCible == "l3":
        if playerTX > userTX:
            if love_l3_points >= 50:
                $ sex_l3_points += 20
                $ love_l3_points += 10
                l3 "Ta bite !"
                $ playerPTS += 1
            elif True:
                $ sex_l3_points += 5
                $ love_l3_points -= 10
                $ warn_l3_points += 10
                l3 "Nooonnn ! Beurk !"
        elif True:
            l3 "une saucisse !"
            user "perdu !"
            $ userPTS += 1
    elif talkCible == "l4":
        if playerTX > userTX:
            if love_l4_points >= 50:
                $ sex_l4_points += 20
                $ love_l4_points += 10
                l4 "Ta bite !"
                $ playerPTS += 1
            elif True:
                $ sex_l4_points += 5
                $ love_l4_points -= 10
                $ warn_l4_points += 10
                l4 "Nooonnn ! Beurk !"
        elif True:
            l4 "une saucisse !"
            user "perdu !"
            $ userPTS += 1
    elif talkCible == "l5":
        if playerTX > userTX:
            if love_l5_points >= 50:
                $ sex_l5_points += 20
                $ love_l5_points += 10
                l5 "Ta bite !"
                $ playerPTS += 1
            elif True:
                $ sex_l5_points += 5
                $ love_l5_points -= 10
                $ warn_l5_points += 10
                l5 "Nooonnn ! Beurk !"
        elif True:
            l5 "une saucisse !"
            user "perdu !"
            $ userPTS += 1
    call screen mysteryBox
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
