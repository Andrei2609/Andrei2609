
label l2_quest_1:
    if tissu_leni_1 == "":
        show screen User(tenue, "_P")
        with fondu
        user "Leni..?"
        show screen Actor1("l2", "nue", "normal", "sh_1", "sb_1", "normal", "boucle_1", "lunettes", "", "Triste", "EX")
        with fondu
        nar ""
        show screen Actor1("l2", "nue", "normal", "sh_1", "sb_1", "normal", "boucle_1", "lunettes", "", "Triste", "P")
        show screen User(tenue, "I")
        with fondu
        l2 "Lincoln, alors comment ça va ?{w} Pas trop dur le Lycée ?"
        show screen Actor1("l2", "nue", "normal", "sh_1", "sb_1", "normal", "boucle_1", "lunettes", "", "Triste", "")
        show screen User(tenue, "_P")
        with fondu
        user "Oui ça va... Mais toi ça n'a pas l'air d'aller ?"
        show screen Actor1("l2", "nue", "normal", "sh_1", "sb_1", "normal", "boucle_1", "lunettes", "", "Triste", "P")
        show screen User(tenue, "I")
        with fondu
        l2 "Tu rigoles c'est l'horreur... Je suis en pleine séance créative et je retrouve plus mon tissu bleu..."
        l2 "Comment je vais faire !"
        show screen Actor1("l2", "nue", "normal", "sh_1", "sb_1", "normal", "boucle_1", "lunettes", "", "Triste", "EX")
        show screen User(tenue, "_P")
        with fondu
        user "Ne t'inquiète pas je vais m'occuper de tout !"
        show screen Actor1("l2", "nue", "normal", "sh_1", "sb_1", "normal", "boucle_1", "lunettes", "", "Neutre", "P")
        show screen User(tenue, "I")
        with fondu
        l2 "Merci Lincoln, tu es vraiment un amour je ne sais pas quoi dire,"
        l2 "mais si tu m'apportes un tissu bleu, je saurai te remercier !"
        $ sex_points += 10
        $ love_l2_points += 1
        $ tissu_leni_1 = "vide"
        hide screen User
        hide screen Actor1
        with fondu
        jump couloir
    elif tissu_leni_1 == "vide":
        scene BG_lori_leni
        show screen Actor1("l2", "nue", "normal", "sh_1", "sb_1", "normal", "boucle_1", "lunettes", "", "Triste", "P")
        show screen User(tenue, "I")
        with fondu
        l2 "J'ai pas le temps de parler Lincoln... Je dois trouver un tissu bleu !"
        hide screen User
        hide screen Actor1
        with fondu
        jump couloir
    elif tissu_leni_1 <> "bleu" and tissu_leni_1 <> "win":
        scene BG_lori_leni
        show screen Actor1("l2", "nue", "normal", "sh_1", "sb_1", "normal", "boucle_1", "lunettes", "", "Triste", "EX")
        show screen User(tenue, "_P")
        with fondu
        user "Leni, j'ai le tissu qu'il te manque !"
        show screen Actor1("l2", "nue", "normal", "sh_1", "sb_1", "normal", "boucle_1", "lunettes", "", "Joyeux", "P")
        with fondu
        l2 "Montre moi Lincoln !"
        hide screen User
        hide screen Actor1
        with fondu
        if tissu_leni_1 == "rouge":
            show EF_surprise
            show q1_leni_KO_rouge
            with trembleV
            pause
            hide q1_leni_KO_rouge
            hide EF_surprise
        elif tissu_leni_1 == "vert":
            show EF_surprise
            show q1_leni_KO_vert
            with trembleV
            pause
            hide q1_leni_KO_vert
            hide EF_surprise
        show screen User(tenue, "I")
        show screen Actor1("l2", "nue", "normal", "sh_1", "sb_1", "normal", "boucle_1", "lunettes", "", "Colere", "P")
        with fondu
        l2 "heu... C'est pas ça du tout ! {w}\n[tissu_leni_1] ! Vraiment ? Allo quoi !? [tissu_leni_1] c'est grave moche !"

        $ love_l2_points -= 2
        $ tissu_leni_1 = "vide"
        show screen Actor1("l2", "nue", "normal", "sh_1", "sb_1", "normal", "boucle_1", "lunettes", "", "Colere", "")
        show screen User(tenue, "_P")
        with fondu
        user "Désolé Leni... Je vais arranger ça !"
        hide screen Actor1
        hide screen User
        with fondu
        jump couloir
    elif tissu_leni_1 == "bleu":
        scene BG_lori_leni
        show screen Actor1("l2", "nue", "normal", "sh_1", "sb_1", "normal", "boucle_1", "lunettes", "", "Triste", "EX")
        show screen User(tenue, "_P")
        with fondu
        user "Leni j'ai le tissu qu'il te manque !"
        show screen Actor1("l2", "nue", "normal", "sh_1", "sb_1", "normal", "boucle_1", "lunettes", "", "Joyeux", "P")
        show screen User(tenue, "I")
        with fondu
        l2 "Montre moi Lincoln !"
        hide screen User
        hide screen Actor1
        show q1_leni_OK
        with fondu
        l2 "C'est trop bien !{w} Merci Lincoln, genre t'es trop le meilleur frère que j'ai !"
        hide q1_leni_OK
        show screen Actor1("l2", "nue", "normal", "sh_1", "sb_1", "normal", "boucle_1", "lunettes", "", "Joyeux", "")
        show screen User(tenue, "_P")
        with fondu
        user "Je suis le seul frère que tu as..."
        hide I_Leni
        show screen Actor1("l2", "nue", "normal", "sh_1", "sb_1", "normal", "boucle_1", "lunettes", "", "Joyeux", "P")
        show screen User(tenue, "I")
        with fondu
        l2 "C'est bien ce que je dis !"
        show screen Actor1("l2", "nue", "normal", "sh_1", "sb_1", "normal", "boucle_1", "lunettes", "", "Joyeux", "")
        show screen User(tenue, "_P")
        with fondu
        user "Heu... Ravi d'avoir pu t'aider !"
        show screen Actor1("l2", "nue", "normal", "sh_1", "sb_1", "normal", "boucle_1", "lunettes", "", "Rougir", "P")
        show screen User(tenue, "I")
        with fondu
        l2 "Attends !"
        hide screen User
        hide screen Actor1
        with fondu
        show q1_leni_win:
            xanchor 0 yanchor 0
            xpos 0 ypos -1500
            linear 10.0 xpos 0 ypos 0
        nar ""
        hide q1_leni_win
        show screen Actor1("l2", "nue", "normal", "sh_0", "sb_1", "defile", "boucle_1", "lunettes", "", "Exciter", "P")
        with fondu
        l2 "Alors, comment-tu me trouve ?"

        $ sex_points += 50

        show screen Actor1("l2", "nue", "normal", "sh_0", "sb_1", "defile", "boucle_1", "lunettes", "", "Exciter", "")
        show screen User(tenue, "_P")
        with fondu
        user "heu... Vraiment très belle !"
        show screen Actor1("l2", "nue", "normal", "sh_0", "sb_1", "defile", "boucle_1", "lunettes", "", "Exciter", "P")
        show screen User(tenue, "I")
        with fondu
        l2 "Ooooh ! Merci Lincoln !"
        show screen Actor1("l2", "nue", "normal", "sh_0", "sb_1", "defile", "boucle_1", "lunettes", "", "Exciter", "")
        show screen User(tenue, "_P")
        with fondu
        user "Bon, j'y vais maintenant."

        $ love_l2_points += 2
        $ tissu_leni_1 = "win"

        hide screen Actor1
        hide screen User
        with fondu
        jump couloir
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
