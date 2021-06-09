
label l5_sport_matin:
    menu:
        "Lynn fait son sport du matin"
        "La regarder discrètement" if True:
            $ lynn_peek_1 = True
            $ sex_points += 10
            show Lynn_abdo_1
            with fondu
            l5 "29... {w}30... {w}Hein !"
            hide Lynn_abdo_1
            show Lynn_abdo_2
            with fondu
            nar ""
            hide Lynn_abdo_2
            with fondu
            show screen Actor1("l5", "sleep", "normal", "sh_0", "", "sleep", "", "", "", "Colere", "P")
            with inB
            show screen User(tenue, "I")
            with fondu
            l5 "Qu'est-ce qu'il y a puanteur ?"
            show screen Actor1("l5", "sleep", "normal", "sh_0", "", "sleep", "", "", "", "Colere", "")
            hide screen User
            show screen User(tenue, "_P")
            with fondu
            user "Oh rien... Bonne chance pour aujourd'hui !"
            show screen Actor1("l5", "sleep", "normal", "sh_0", "", "sleep", "", "", "", "Neutre", "P")
            hide screen User
            show screen User(tenue, "I")
            with fondu
            l5 "Bonne chance pour quoi ?"
            show screen Actor1("l5", "sleep", "normal", "sh_0", "", "sleep", "", "", "", "Neutre", "")
            hide screen User
            show screen User(tenue, "_P")
            with fondu
            user "Bah pour ta compétition !"
            show screen Actor1("l5", "sleep", "normal", "sh_0", "", "sleep", "", "", "", "Neutre", "P")
            hide screen User
            show screen User(tenue, "I")
            with fondu
            l5 "Tu t'en es souvenu !? Je suis touchée."

            $ love_l5_points += 5

            show screen Actor1("l5", "sleep", "normal", "sh_0", "", "sleep", "", "", "", "Neutre", "")
            hide screen User
            show screen User(tenue, "_P")
            with fondu
            user "Évidemment, sinon quel horrible petit frère je ferais !"
            hide screen Actor1
            hide screen User
            with fondu
            jump salon
        "Mieux vaut ne pas la déranger..." if True:
            jump salon
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
