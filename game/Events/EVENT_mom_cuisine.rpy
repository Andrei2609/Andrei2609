
label mom_cuisine_matin:
    $ nakedGO = False
    if heure == 8 and minute == 0 and jour < 6:
        $ go_school = True
        show screen Actor1("mom", "normal", "normal", "sh_1", "sb_1", "normal", "boucle_1", "", "", "Neutre", "P")
        with fondu
        mom "Lincoln, tu vas être en retard pour le bus ! Je dois déjà emmener tes soeurs !"

        show screen Actor1("mom", "normal", "normal", "sh_1", "sb_1", "normal", "boucle_1", "", "", "Neutre", "")
        with fondu
        show screen User(tenue, "_P")
        with inL
        user "Oui maman ! J'arrive !"
        show screen User(tenue, "")
        show screen Actor1("mom", "normal", "normal", "sh_1", "sb_1", "normal", "boucle_1", "", "", "Neutre", "P")
        with fondu
        mom "Tiens Lincoln, un peu d'argent pour ton déjeuner ! À ce soir mon coeur !"
        $ user_coins += 15
        call timer (0, 5) from _call_timer_15
        with fondu
        hide screen User
        with outR
        hide screen Actor1
        with fondu
        jump Diningroom
    elif heure < 8:
        show Rita_sleep_dos at right
        with fondu
        show screen User(tenue, "")
        with inL
        nar "Maman prépare le petit déjeuner... Mieux vaut ne pas la déranger !"
        menu:
            nar "Imaginer votre mère préparer le petite déjeuner nue ?"
            "Oui !" if True:
                hide Rita_sleep_dos
                show Rita_nue_dos at right
                hide screen User
                show screen User(tenue, "_M")
                with fondu
                user "Oh... C'est bon..."
                $ sex_points += 5
                $ nakedGO = True
                hide Rita_nue_dos
                hide screen User
                jump cuisine_mom
            "Non" if True:
                hide Rita_sleep_dos
                hide screen User
                jump cuisine_mom
    elif True:
        show Rita_dos at right
        with fondu
        show screen User(tenue, "")
        with inL
        nar "Maman cuisine... Mieux vaut ne pas la déranger !"
        menu:
            nar "Imaginer votre mère cuisiner nue ?"
            "Oui !" if True:
                hide Rita_dos
                show Rita_nue_dos at right
                hide screen User
                show screen User(tenue, "_M")
                with fondu
                user "Oh... C'est bon..."
                $ sex_points += 5
                $ nakedGO = True
                hide Rita_nue_dos
                hide screen User
                jump cuisine_mom
            "Non" if True:
                hide Rita_dos
                hide screen User
                jump cuisine_mom
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
