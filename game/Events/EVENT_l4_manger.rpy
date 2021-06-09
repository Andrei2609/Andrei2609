
label l4_table_1:
    scene BG_manger
    with fondu
    menu:
        nar "Y'a du bruit sous la table ?"
        "Regarder discrètement" if True:
            $ luan_peek_1 = True
            $ sex_points += 10
            show PEEK_nappe_back
            show Luan_ass_sleepA at left
            show PEEK_nappe
            with fondu
            nar ""
            hide PEEK_nappe
            with outT
            nar ""
            hide Luan_ass_sleepA
            hide PEEK_nappe_back
            scene BG_manger
            with trembleV
            with fondu
            show screen Actor1("l4", "nue", "normal", "sh_0", "sb_1", "sleep", "", "", "", "Rougir", "P")
            with inB
            show screen User(tenue, "I")
            with fondu
            l4 "Lincoln qu'est-ce que tu regardes ?"
            show screen Actor1("l4", "nue", "normal", "sh_0", "sb_1", "sleep", "", "", "", "Rougir", "")
            show screen User(tenue, "_P")
            with fondu
            user "Heu..."
            show screen Actor1("l4", "joyeux", "normal", "sh_0", "sb_1", "sleep", "", "", "", "Joyeux", "P")
            show screen User(tenue, "I")
            with fondu
            l4 "La pleine lune ! Hahahaha... {w}T'as compris ?"
            show screen Actor1("l4", "joyeux", "normal", "sh_0", "sb_1", "sleep", "", "", "", "Rire", "P")
            with fondu
            l4 "Ha! Ha! Ha! Ha!"
            show screen Actor1("l4", "joyeux", "normal", "sh_0", "sb_1", "sleep", "", "", "", "Joyeux", "P")
            with fondu
            l4 "Mais plus sérieusement, tu n'aurais pas vu la jambe de monsieur Coco ?"
            show screen Actor1("l4", "nue", "normal", "sh_0", "sb_1", "sleep", "", "", "", "Joyeux", "")
            show screen User(tenue, "_P")
            with fondu
            user "Non désolé Luan... {w}J'ai rien vu !"
            show screen Actor1("l4", "nue", "normal", "sh_0", "sb_1", "sleep", "", "", "", "Joyeux", "P")
            show screen User(tenue, "I")
            with fondu
            l4 "Bah si tu tombes dessus, te fais pas trop mal ! Hahahaha... {w}T'as compris ?"
            show screen Actor1("l4", "nue", "normal", "sh_0", "sb_1", "sleep", "", "", "", "Joyeux", "")
            show screen User(tenue, "_P")
            with fondu
            user "Oui très drôle !"
            show screen User(tenue, "_M")
            user "Peut être que si je lui retrouve la jambe de monsieur Coco Luan sera contente !?"

            $ sex_l4_points += 5
            $ warn_loud_points += 5
            $ coco_jambe_1 = "perdue"

            hide screen User
            with outR
            hide screen Actor1
            with fondu
            jump Diningroom
        "Ne rien faire" if True:
            jump Diningroom
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
