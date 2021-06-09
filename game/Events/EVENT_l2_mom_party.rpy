
image l2_mom_party_1 = "Images/CG/01-Personnages/102-Leni/quest_2/1.png"
image l2_mom_party_2 = "Images/CG/01-Personnages/102-Leni/quest_2/2.png"
image l2_mom_party_3:
    "Images/CG/01-Personnages/102-Leni/quest_2/3.png"
    pause .5
    "Images/CG/01-Personnages/102-Leni/quest_2/4.png"
    pause .5
    repeat
image l2_mom_party_5 = "Images/CG/01-Personnages/102-Leni/quest_2/5.png"
image l2_mom_party_6 = "Images/CG/01-Personnages/102-Leni/quest_2/6.png"
image l2_mom_party_7 = "Images/CG/01-Personnages/102-Leni/quest_2/7.png"
image l2_mom_party_8 = "Images/CG/01-Personnages/102-Leni/quest_2/8.png"
image l2_mom_party_9 = "Images/CG/01-Personnages/102-Leni/quest_2/9.png"
image l2_mom_party_10 = "Images/CG/01-Personnages/102-Leni/quest_2/10.png"
image l2_mom_party_11 = "Images/CG/01-Personnages/102-Leni/quest_2/11.png"
image l2_mom_party_12:
    "Images/CG/01-Personnages/102-Leni/quest_2/12.png"
    pause .5
    "Images/CG/01-Personnages/102-Leni/quest_2/11.png"
    pause .5
    repeat
image l2_mom_party_13 = "Images/CG/01-Personnages/102-Leni/quest_2/13.png"
image l2_mom_party_14 = "Images/CG/01-Personnages/102-Leni/quest_2/14.png"
image l2_mom_party_15 = "Images/CG/01-Personnages/102-Leni/quest_2/15.png"
image l2_mom_party_16 = "Images/CG/01-Personnages/102-Leni/quest_2/16.png"
image l2_mom_party_17 = "Images/CG/01-Personnages/102-Leni/quest_2/17.png"
image l2_mom_party_18:
    "Images/CG/01-Personnages/102-Leni/quest_2/18.png"
    pause .3
    "Images/CG/01-Personnages/102-Leni/quest_2/17.png"
    pause .3
    repeat
image l2_mom_party_19:
    "Images/CG/01-Personnages/102-Leni/quest_2/19.png"
    pause .3
    "Images/CG/01-Personnages/102-Leni/quest_2/20.png"
    pause .3
    repeat
image l2_mom_party_21 = "Images/CG/01-Personnages/102-Leni/quest_2/21.png"
image l2_mom_party_22 = "Images/CG/01-Personnages/102-Leni/quest_2/22.png"
image l2_mom_party_23 = "Images/CG/01-Personnages/102-Leni/quest_2/23.png"
image l2_mom_party_24 = "Images/CG/01-Personnages/102-Leni/quest_2/24.png"
image l2_mom_party_25 = "Images/CG/01-Personnages/102-Leni/quest_2/25.png"
image l2_mom_party_26 = "Images/CG/01-Personnages/102-Leni/quest_2/26.png"
image l2_mom_party_27 = "Images/CG/01-Personnages/102-Leni/quest_2/27.png"
image l2_mom_party_28 = "Images/CG/01-Personnages/102-Leni/quest_2/28.png"
image l2_mom_party_29 = "Images/CG/01-Personnages/102-Leni/quest_2/29.png"
image l2_mom_party_30 = "Images/CG/01-Personnages/102-Leni/quest_2/30.png"

init:
    $ mom_party_21 = False

label mom_party_2021_Review:
    hide screen Menu_collection
    $ review = True
    scene BG_salon
    with fondu
    jump mom_party_2021

label mom_party_2021:

    $ mom_party_21 = True

    show l2_mom_party_1
    with fondu
    l2 "Je vais préparé la plus belle des fêtes !"
    l2 "La ! La ! La !"
    pause
    hide l2_mom_party_1
    with fondu
    show screen Actor1("l2", "nue", "normal", "", "", "normal", "boucle_1", "lunettes", "", "Joyeux", "")
    show screen User(tenue, "_P")
    user "Tu fais quoi Leni ?"
    show screen Actor1("l2", "nue", "normal", "", "", "normal", "boucle_1", "lunettes", "", "Joyeux", "P")
    show screen User(tenue, "I")
    l2 "Je prépare la fête des mères pour Maman !"
    show screen Actor1("l2", "nue", "normal", "", "", "normal", "boucle_1", "lunettes", "", "Joyeux", "")
    show screen User(tenue, "_P")
    user "Tu veux que je t'aide ?"
    show screen Actor1("l2", "nue", "normal", "", "", "normal", "boucle_1", "lunettes", "", "Joyeux", "P")
    show screen User(tenue, "I")
    l2 "Volontiers Lincoln, j'ai besoin d'accrocher des déco aux mur et ces trop haut"
    l2 "J'ai peur de tombée..."
    show screen Actor1("l2", "nue", "normal", "", "", "normal", "boucle_1", "lunettes", "", "Joyeux", "")
    show screen User(tenue, "_P")
    user "Mais ça sera avec plaisir que je t'accompagnerai pour cette tache !"
    show screen Actor1("l2", "pensif", "normal", "", "", "normal", "boucle_1", "lunettes", "", "Pensif", "P")
    show screen User(tenue, "I")
    l2 "Heu.. Que tu me quoi !?"
    show screen Actor1("l2", "pensif", "normal", "", "", "normal", "boucle_1", "lunettes", "", "Pensif", "")
    show screen User(tenue, "_P")
    user "Je veux dire que ça me ferai plaisir de t'aider !"
    hide screen Actor1
    hide screen User
    show l2_mom_party_2
    with fondu
    pause
    hide l2_mom_party_2
    show l2_mom_party_3
    with fondu
    pause
    hide l2_mom_party_3
    show l2_mom_party_5
    with fondu
    pause
    hide l2_mom_party_5
    show l2_mom_party_6
    with fondu
    pause
    hide l2_mom_party_6
    show l2_mom_party_7
    with fondu
    pause
    l2 "Je l'ai presque..."
    hide l2_mom_party_7
    show l2_mom_party_8
    with fondu
    l2 "Juste un petit effort..."
    pause
    hide l2_mom_party_8
    show l2_mom_party_9
    with fondu
    pause
    user "Mhm... Jolie..."
    user "Attends !"
    hide l2_mom_party_9
    show l2_mom_party_10
    with fondu
    user "Leni, j'ai une idée je vais t'aider à l'attraper en te poussant !"
    hide l2_mom_party_10
    show l2_mom_party_11
    with fondu
    l2 "Très bonne idée Lincoln, prend appuis sur mes fesses."
    user "Mais qu'elle bonne idée Leni."
    pause
    hide l2_mom_party_11
    show l2_mom_party_12
    with fondu
    user "Je vais pousser par petits coups, ok ?"
    l2 "Oui comme ça j'aurais aucun mal à l'attraper !"
    pause
    l2 "ça ne marche pas..."
    user "Je vais essayer autre chose."
    hide l2_mom_party_12
    show l2_mom_party_13
    with fondu
    pause
    hide l2_mom_party_13
    show l2_mom_party_14
    with fondu
    l2 "Lincoln, qu'est ce que tu fais ?"
    user "Je prend un meilleur appuis pour te pousser"
    user "Donc j'utilise ta culotte comme poignée"
    l2 "Ah ! C'est logique !"
    pause
    hide l2_mom_party_14
    show l2_mom_party_15
    with fondu
    pause
    hide l2_mom_party_15
    show l2_mom_party_16
    with fondu
    pause
    hide l2_mom_party_16
    show l2_mom_party_17
    with fondu
    l2 "Oh ! c'est tout chaud."
    user "Prêt je vais pousser un peu plus fort ?"
    l2 "Oui, va y de toute tes forces, il faut qu'on la récupère à tout prix !"
    pause
    menu:
        "vue 1" if True:
            hide l2_mom_party_17
            jump l2_mom_party_sex_1
        "vue 2" if True:
            hide l2_mom_party_17
            jump l2_mom_party_sex_2

label l2_mom_party_sex_1:
    show l2_mom_party_18
    with fondu
    pause
    menu:
        "vue 2" if True:
            hide l2_mom_party_18
            jump l2_mom_party_sex_2
        "jouir" if True:

            hide l2_mom_party_18
            jump l2_mom_party_cum

label l2_mom_party_sex_2:
    show l2_mom_party_19
    with fondu
    pause
    menu:
        "vue 1" if True:
            hide l2_mom_party_19
            jump l2_mom_party_sex_1
        "jouir" if True:

            hide l2_mom_party_19
            jump l2_mom_party_cum

label l2_mom_party_cum:
    show l2_mom_party_21
    with fondu
    pause
    hide l2_mom_party_21
    show l2_mom_party_22
    with flash
    pause
    show l2_mom_party_22
    with flash
    pause
    show l2_mom_party_22
    with flash
    pause
    hide l2_mom_party_22
    show l2_mom_party_23
    with flash
    pause
    hide l2_mom_party_23
    show l2_mom_party_24
    with fondu
    pause
    hide l2_mom_party_24
    show l2_mom_party_25
    with fondu
    user "Hop !"
    l2 "Lincoln, Je l'ai ! Je l'ai !"
    pause
    hide l2_mom_party_25
    show l2_mom_party_26
    with fondu
    mom "Je suis rentrée les enfants !"
    sis_loud "SURPRISE !!!"
    sis_loud "Bonne Fête Maman !"
    mom "Ooooh ! Que c'est gentil..."
    mom "La déco est vraiment incroyable !"
    pause
    hide l2_mom_party_26
    show l2_mom_party_27
    with fondu
    user "Bonne fête maman !"
    pause
    hide l2_mom_party_27
    show l2_mom_party_28
    with fondu
    mom "Oh, merci mon ange !"
    user "C'est un réel plasir."
    pause
    hide l2_mom_party_28
    show l2_mom_party_29
    with fondu
    l2 "Maman ! Bonne fête des mères !"
    mom "Merci Leni, tu t'es surpasser pour la déco."
    pause
    hide l2_mom_party_29
    show l2_mom_party_30
    with fondu
    l2 "C'est grace à Lincoln"
    l2 "Sans lui je n'aurais jamais fini comme ça !"
    user "A qui le dis-tu !"
    pause
    hide l2_mom_party_30

    if review == True:
        $ review = False
        return
    elif True:
        $ sex_points += 50
        $ sex_l2_points += 10
        $ love_l2_points += 5
        $ love_mom_points += 5
        $ l2_mom_party_2021 = True
        $ heure += 1
        jump salon
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
