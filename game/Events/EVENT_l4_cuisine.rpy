
image l4_tarte_1 = "Images/CG/01-Personnages/104-Luan/quest_1/poissonavril_1.png"
image l4_tarte_2 = "Images/CG/01-Personnages/104-Luan/quest_1/poissonavril_2.png"
image l4_tarte_3 = "Images/CG/01-Personnages/104-Luan/quest_1/poissonavril_3.png"
image l4_tarte_cum_1 = "Images/CG/01-Personnages/104-Luan/quest_1/poissonavril_cum.png"
image l4_tarte_cum_2 = "Images/CG/01-Personnages/104-Luan/quest_1/poissonavril_cum1.png"
image l4_tarte_yum = "Images/CG/01-Personnages/104-Luan/quest_1/poissonavril_luan.png"
image l4_tarte_yum_OK = "Images/CG/01-Personnages/104-Luan/quest_1/poissonavril_luan2.png"
image l4_tarte_yum_KO = "Images/CG/01-Personnages/104-Luan/quest_1/poissonavril_luan1.png"
image l4_tarte_choix = "Images/CG/01-Personnages/104-Luan/quest_1/poissonavril_tarte.png"

init:
    $ tarte_OK = False
    $ l4_tarte = 0

label l4_cuisine_tarte_GO:
    show screen Actor1("l4", "joyeux", "normal", "sh_1", "sb_1", "cuisine", "", "", "", "Pensif", "")
    menu:
        "Lui parler" if True:
            show screen Actor1("l4", "nue", "normal", "sh_1", "sb_1", "cuisine", "", "", "", "Pensif", "P")
            with fondu
            l4 "Salut Lincoln..."
            show screen Actor1("l4", "nue", "normal", "sh_1", "sb_1", "cuisine", "", "", "", "Pensif", "")
            call screen l4_talk
            hide screen Actor1
        "L'aider" if l4_tarte <> 3:
            if l4_tarte == 0:
                $ l4_tarte = 1
                show screen User(tenue, "_P")
                show screen Actor1("l4", "nue", "normal", "sh_1", "sb_1", "cuisine", "", "", "", "Pensif", "")
                user "Salut Luan !"
                user "Alors ça gaze ?"
                show screen User(tenue, "I")
                show screen Actor1("l4", "nue", "normal", "sh_1", "sb_1", "cuisine", "", "", "", "Pensif", "P")
                l4 "Non... Pas vraiment ! Je suis entrain de préparer des tartes"
                show screen User(tenue, "_P")
                show screen Actor1("l4", "nue", "normal", "sh_1", "sb_1", "cuisine", "", "", "", "Pensif", "")
                user "Je me demande bien pourquoi..."
                show screen User(tenue, "I")
                show screen Actor1("l4", "nue", "normal", "sh_1", "sb_1", "cuisine", "", "", "", "Pensif", "P")
                l4 "Lincoln !"
                show screen User(tenue, "_P")
                show screen Actor1("l4", "nue", "normal", "sh_1", "sb_1", "cuisine", "", "", "", "Pensif", "")
                user "Désolé... Continue."
                show screen User(tenue, "I")
                show screen Actor1("l4", "nue", "normal", "sh_1", "sb_1", "cuisine", "", "", "", "Pensif", "P")
                l4 "Je prépare des tartes comme je te disais"
                l4 "Mais je n'ai plus de crème..."
                show screen User(tenue, "_P")
                show screen Actor1("l4", "nue", "normal", "sh_1", "sb_1", "cuisine", "", "", "", "Pensif", "")
                user "Je m'occupe de tout, rassure toi, je te trouverais la meilleur des crème !"
            if l4_tarte == 2:
                show screen User(tenue, "_P")
                show screen Actor1("l4", "nue", "normal", "sh_1", "sb_1", "cuisine", "", "", "", "Pensif", "")
                user "Luan, J'ai trouvez la crème parfaite !"
                user "Bien épaisse et crémeuse."
                show screen User(tenue, "I")
                show screen Actor1("l4", "nue", "normal", "sh_1", "sb_1", "cuisine", "", "", "", "Neutre", "P")
                l4 "C'est pas vrai ! C'est trop cool ça !"
                hide screen User
                hide screen Actor1
                show l4_tarte_2
                pause
                hide l4_tarte_2
                show screen User(tenue, "I")
                show screen Actor1("l4", "nue", "normal", "sh_1", "sb_1", "cuisine", "", "", "", "Joyeux", "P")
                l4 "Elle est parfaite ! Merci Lincoln !"
                $ love_l4_points += 3
                $ tarte_OK = True
            elif True:
                show screen User(tenue, "I")
                show screen Actor1("l4", "nue", "normal", "sh_1", "sb_1", "cuisine", "", "", "", "Pensif", "P")
                l4 "Je n'ai pas le temps de jouer Lincoln"
                l4 "Si mes tartes à la crême sont sans crême"
                l4 "C'est tarte tout ça..."
                show screen Actor1("l4", "nue", "normal", "sh_1", "sb_1", "cuisine", "", "", "", "Rire", "P")
                l4 "T'as compris ?"
                l4 "Ha ! Ha ! Ha !"
            hide screen User
    hide screen Actor1
    jump cuisine

label user_mastu_creme:
    $ l4_tarte = 2
    hide screen User
    show l4_tarte_1
    pause
    hide l4_tarte_1
    show l4_tarte_cum_1
    pause
    hide l4_tarte_cum_1
    show l4_tarte_cum_2
    with flash
    pause
    hide l4_tarte_cum_2
    call timer (0, 30) from _call_timer_46
    jump cham_user

label l4_cuisine_tarte_END:
    show l4_tarte_choix
    with fondu
    menu:
        "Lui jeter dessus ?"
        "oui" if True:
            hide l4_tarte_choix
            show screen User(tenue, "_P")
            show screen Actor1("l4", "nue", "normal", "sh_1", "sb_1", "cuisine", "", "", "", "Neutre", "")
            user "Luan !"
            show screen User(tenue, "I")
            show screen Actor1("l4", "nue", "normal", "sh_1", "sb_1", "cuisine", "", "", "", "Neutre", "P")
            l4 "Lincoln !?"
            show screen User(tenue, "_P")
            show screen Actor1("l4", "nue", "normal", "sh_1", "sb_1", "cuisine", "", "", "", "Surpris", "")
            user "Tu as faim ?"
            show screen User(tenue, "I")
            show screen Actor1("l4", "nue", "normal", "sh_1", "sb_1", "cuisine", "", "", "", "Surpris", "EX")
            l4 "Hein ?"
            hide screen User
            hide screen Actor1
            $ l4_cum += 1
            show l4_tarte_3
            with flash
            pause
            hide l4_tarte_3
            show l4_tarte_yum
            with fondu
            pause
            hide l4_tarte_yum
            if l4_cum >= 5:
                show l4_tarte_yum_OK
                with fondu
                pause
                l4 "Cette crème laisse un gout en bouche... Miam !"
                $ sex_l4_points +=1
                hide l4_tarte_yum_OK
            elif True:
                show l4_tarte_yum_KO
                with fondu
                pause
                l4 "Cette crème est rance ! Beurk !"
                hide l4_tarte_yum_KO
            $ tarte_OK = False
            $ l4_tarte = 3
            call timer (0, 30) from _call_timer_55
            jump cuisine
        "non" if True:
            hide l4_tarte_choix
            with fondu
            jump cuisine
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
