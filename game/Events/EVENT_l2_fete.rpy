
image Leni_fete_1 = "Images/CG/01-Personnages/102-Leni/soiree/soiree_1.png"
image Leni_fete_2 = "Images/CG/01-Personnages/102-Leni/soiree/soiree_2.png"
image Leni_fete_3 = "Images/CG/01-Personnages/102-Leni/soiree/soiree_3.png"
image Leni_fete_4 = "Images/CG/01-Personnages/102-Leni/soiree/soiree_4.png"
image Leni_fete_5_1 = "Images/CG/01-Personnages/102-Leni/soiree/soiree_5_1.png"
image Leni_fete_5_2 = "Images/CG/01-Personnages/102-Leni/soiree/soiree_5_2.png"
image Leni_fete_5_3 = "Images/CG/01-Personnages/102-Leni/soiree/soiree_5_3.png"
image Leni_fete_5 = "Images/CG/01-Personnages/102-Leni/soiree/soiree_5.png"
image Leni_fete_6 = "Images/CG/01-Personnages/102-Leni/soiree/soiree_6.png"
image Leni_fete_7 = "Images/CG/01-Personnages/102-Leni/soiree/soiree_7.png"
image Leni_fete_8 = "Images/CG/01-Personnages/102-Leni/soiree/soiree_8.png"
image Leni_fete_9 = "Images/CG/01-Personnages/102-Leni/soiree/soiree_9.png"
image Leni_fete_10 = "Images/CG/01-Personnages/102-Leni/soiree/soiree_10.png"
image Leni_fete_11 = "Images/CG/01-Personnages/102-Leni/soiree/soiree_11.png"

image Leni_fete_table_1 = "Images/CG/01-Personnages/102-Leni/soiree/table_1.png"
image Leni_fete_table_2 = "Images/CG/01-Personnages/102-Leni/soiree/table_2.png"

image Leni_fete_user_1 = "Images/CG/01-Personnages/102-Leni/soiree/user_1.png"
image Leni_fete_user_2 = "Images/CG/01-Personnages/102-Leni/soiree/user_2.png"
image Leni_fete_user_3 = "Images/CG/01-Personnages/102-Leni/soiree/user_3.png"
image Leni_fete_user_4 = "Images/CG/01-Personnages/102-Leni/soiree/user_4.png"

init:
    $ fete_hot = 0

label l2_fiesta_Review:
    hide screen Menu_collection
    $ review = True
    scene BG_cave
    with fondu
    jump l2_fiesta

label l2_fiesta:

    $ fete_hot = 0

    show Leni_fete_1
    with fondu
    nar ""
    user "Leni prépare souvent des fêtes le samedi soir"
    user "avec ses amies toutes plus sexy les une que les autres..."
    hide Leni_fete_1
    show Leni_fete_table_1
    with fondu
    pause
    hide Leni_fete_table_1
    show Leni_fete_user_1
    with fondu
    user "mhm... C'est barbant..."
    hide Leni_fete_user_1
    show Leni_fete_user_2
    with trembleV
    user "J'ai une idée !"
    hide Leni_fete_user_2
    show Leni_fete_table_1
    with fondu
    menu:
        "Corsé un peu le punch ?"
        "Oui" if alcool >= 1:
            $ fete_hot += 1
            $ sex_l2_points += 5
            hide Leni_fete_table_1
            show Leni_fete_table_2
            with fondu
            user "Avec ça la fête n'en sera que meilleure !"
            hide Leni_fete_table_2
        "Non" if True:
            hide Leni_fete_table_1
    show Leni_fete_2
    with fondu
    nar ""
    hide Leni_fete_2
    show Leni_fete_3
    with fondu
    l2 "Chin !"
    hide Leni_fete_3
    show Leni_fete_4
    with fondu
    nar ""
    nar "La soirée passe..."
    hide Leni_fete_4
    if fete_hot == 1:
        show BG_musique
        show Leni_fete_user_1
        with fondu
        nar "La musique entrainante, les filles se laissent aller sans retenue"
        hide Leni_fete_user_1
        show Leni_fete_5_1:
            xanchor 0 yanchor 0
            xpos 0 ypos -1200
            linear 10.0 xpos 0 ypos 0
        with fondu
        nar ""
        mandee "C'est trop cool !"
        hide Leni_fete_5_1
        show Leni_fete_5_2:
            xanchor 0 yanchor 0
            xpos 0 ypos -1200
            linear 10.0 xpos 0 ypos 0
        with fondu
        nar ""
        l2 "Hhiiiii !!! J'ai l'impression de volée !"
        hide Leni_fete_5_2
        show Leni_fete_5_3:
            xanchor 0 yanchor 0
            xpos 0 ypos -1200
            linear 10.0 xpos 0 ypos 0
        with fondu
        nar ""
        jackie "La musique est franchement top !"
        hide Leni_fete_5_3
        show Leni_fete_5
        with fondu
        nar ""
        hide Leni_fete_5
        hide BG_musique
        show Leni_fete_user_4
        with fondu
        user "J'adore voir les filles danser comme ça..."
        hide Leni_fete_user_4
        show Leni_fete_1
        with fondu
        nar ""
        l2 "Cette danse était genre trop entrainante !"
        mandee "Tu la dis... Je suis toute déshydratée"
        jackie "Moi aussi !"
        l2 "Et moi j'ai trop soif !"
        hide Leni_fete_1
        show Leni_fete_table_1
        with fondu
        menu:
            "Corsont un peu plus le punch, pour voir ?"
            "Oui" if alcool >= 1:
                $ fete_hot += 1
                $ sex_l2_points += 5
                hide Leni_fete_table_1
                show Leni_fete_table_2
                with fondu
                user "Avec ça la fête va passé au niveau supérieur !"
                hide Leni_fete_table_2
            "Non" if True:
                hide Leni_fete_table_1
        show Leni_fete_2
        with fondu
        nar ""
        hide Leni_fete_2
        show Leni_fete_3
        with fondu
        l2 "Chin !"
        hide Leni_fete_3
        show Leni_fete_4
        with fondu
        nar ""
        hide Leni_fete_4
        show Leni_fete_user_1
        with fondu
        user "mhm... Il se passe pas grand chose..."
        hide Leni_fete_user_1
        if fete_hot == 2:
            show Leni_fete_user_4
            with fondu
            user "Quoique !!!"
            hide Leni_fete_user_4
            show Leni_fete_user_3
            with fondu
            nar "Lincoln regardais la soirée de Leni se transformer petit à petit en orgie lesbienne"
            hide Leni_fete_user_3
            show Leni_fete_6
            with fondu
            nar "Très rapidement elles enlevèrent leur vêtements..."
            hide Leni_fete_6
            show Leni_fete_7
            with fondu
            nar ""
            hide Leni_fete_7
            show Leni_fete_8
            with fondu
            jackie "Leni... J'adore ça..."
            l2 "Tu crois que si je te suce les seins assez fort y il aura du lait ?"
            jackie "Heu..."
            l2 "Mandee ! Qu'est ce que tu fais ?"
            mandee "Tu mouille tellement..."
            mandee "Je ne peux pas y résistée !"
            nar ""
            hide Leni_fete_8
            show Leni_fete_9
            with flash
            jackie "Les filles !"
            show Leni_fete_10
            with flash
            mandee "Je jouis !"
            show Leni_fete_11
            with flash
            l2 "Aaaaahh !!!"
            nar ""
            nar "Les trois demoiselles, une fois l'extase ateint s'endormirent sur le sol de la cave..."
            hide Leni_fete_9
            hide Leni_fete_10
            hide Leni_fete_11
            show Leni_fete_user_3
            with fondu
            user "J'adore les fêtes de Leni !"
            hide Leni_fete_user_3
            with fondu
        elif True:
            jump l2_fiesta_bad_end
    elif True:
        jump l2_fiesta_bad_end
    if review == True:
        $ review = False
        return
    elif True:
        $ sex_points += 50
        $ sex_l2_points += 10
        $ love_l2_points += 5
        $ l2_fiesta = True
        $ heure += 1
        jump cave

label l2_fiesta_bad_end:
    show Leni_fete_user_1
    with fondu
    user "La fête se termine déjà... La prochaine fois il faudra que je trouve de quoi la pimenté !"
    hide Leni_fete_user_1
    with fondu
    $ heure += 1
    jump cave
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
