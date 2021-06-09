screen Actor1(acteur, bras, cheveux, slip1, slip2, tenue, acc1, acc2, acc3, exp, position):
    zorder 200
    if cheveux <> "":
        add "Images/Personnages/[acteur]/Cheveux/[cheveux]_B.png" xalign 1.0 yalign 1.0
    if nakedGO == True or slipGO == True:
        add "Images/Personnages/[acteur]/Bras/nue_D.png" xalign 1.0 yalign 1.0
    else:
        add "Images/Personnages/[acteur]/Bras/[bras]_D.png" xalign 1.0 yalign 1.0
    add "Images/Personnages/[acteur]/corps.png" xalign 1.0 yalign 1.0
    if nakedGO == True:
        add "Images/Personnages/[acteur]/Slip/sh_0.png" xalign 1.0 yalign 1.0
    elif slip1 <> "":
        add "Images/Personnages/[acteur]/Slip/[slip1].png" xalign 1.0 yalign 1.0
    if nakedGO == True:
        null
    elif slip2 <> "":
        add "Images/Personnages/[acteur]/Slip/[slip2].png" xalign 1.0 yalign 1.0
    if nakedGO == True or slipGO == True:
        null
    elif tenue <> "":
        add "Images/Personnages/[acteur]/Tenue/[tenue].png" xalign 1.0 yalign 1.0
    if nakedGO == True or slipGO == True:
        add "Images/Personnages/[acteur]/Bras/nue_G.png" xalign 1.0 yalign 1.0
    else:
        add "Images/Personnages/[acteur]/Bras/[bras]_G.png" xalign 1.0 yalign 1.0
    if position == "P" or position == "p":
        add "[acteur]_[exp]_talk" xalign 1.0 yalign 1.0
    elif position == "EX" and exp == "Joyeux":
        add "[acteur]_[exp]_rire" xalign 1.0 yalign 1.0
    elif position == "EX":
        add "Images/Personnages/[acteur]/Expression/[exp]/2.png" xalign 1.0 yalign 1.0
    else:
        add "Images/Personnages/[acteur]/Expression/[exp]/0.png" xalign 1.0 yalign 1.0
    if cheveux <> "":
        add "Images/Personnages/[acteur]/Cheveux/[cheveux]_H.png" xalign 1.0 yalign 1.0
    if exp == "Triste":
        if position <> "EX":
            add "Images/Personnages/[acteur]/Expression/[exp]/S.png" xalign 1.0 yalign 1.0
    elif exp <> "Colere":
        add "Images/Personnages/[acteur]/Expression/[exp]/S.png" xalign 1.0 yalign 1.0
    if acc1 <> "":
        add "Images/Personnages/[acteur]/Accessoire/[acc1].png" xalign 1.0 yalign 1.0
    if acc2 <> "":
        add "Images/Personnages/[acteur]/Accessoire/[acc2].png" xalign 1.0 yalign 1.0
    if acc3 <> "":
        add "Images/Personnages/[acteur]/Accessoire/[acc3].png" xalign 1.0 yalign 1.0

screen Actor2(acteur, bras, cheveux, slip1, slip2, tenue, acc1, acc2, acc3, exp, position):
    if cheveux <> "":
        add "Images/Personnages/[acteur]/Cheveux/[cheveux]_B.png" xalign 0.7 yalign 1.0
    add "Images/Personnages/[acteur]/Bras/[bras]_D.png" xalign 0.7 yalign 1.0
    add "Images/Personnages/[acteur]/corps.png" xalign 0.7 yalign 1.0
    if slip1 <> "":
        add "Images/Personnages/[acteur]/Slip/[slip1].png" xalign 0.7 yalign 1.0
    if slip2 <> "":
        add "Images/Personnages/[acteur]/Slip/[slip2].png" xalign 0.7 yalign 1.0
    if tenue <> "":
        add "Images/Personnages/[acteur]/Tenue/[tenue].png" xalign 0.7 yalign 1.0
    add "Images/Personnages/[acteur]/Bras/[bras]_G.png" xalign 0.7 yalign 1.0
    if position == "P" or position == "p":
        add "[acteur]_[exp]_talk" xalign 0.7 yalign 1.0
    elif position == "EX" and exp == "Joyeux":
        add "[acteur]_[exp]_rire" xalign 0.7 yalign 1.0
    elif position == "EX":
        add "Images/Personnages/[acteur]/Expression/[exp]/2.png" xalign 0.7 yalign 1.0
    else:
        add "Images/Personnages/[acteur]/Expression/[exp]/0.png" xalign 0.7 yalign 1.0
    if cheveux <> "":
        add "Images/Personnages/[acteur]/Cheveux/[cheveux]_H.png" xalign 0.7 yalign 1.0
    if exp == "Triste":
        if position <> "EX":
            add "Images/Personnages/[acteur]/Expression/[exp]/S.png" xalign 0.7 yalign 1.0
    elif exp <> "Colere":
        add "Images/Personnages/[acteur]/Expression/[exp]/S.png" xalign 0.7 yalign 1.0
    if acc1 <> "":
        add "Images/Personnages/[acteur]/Accessoire/[acc1].png" xalign 0.7 yalign 1.0
    if acc2 <> "":
        add "Images/Personnages/[acteur]/Accessoire/[acc2].png" xalign 0.7 yalign 1.0
    if acc3 <> "":
        add "Images/Personnages/[acteur]/Accessoire/[acc3].png" xalign 0.7 yalign 1.0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
