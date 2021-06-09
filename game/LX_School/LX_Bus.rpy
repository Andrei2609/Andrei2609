label bus:
    $ checkZone = "bus"
    scene BG_bus
    with fondu
    show Clyde_P at right
    with inR
    show screen User(tenue, "I")
    with inL
    clyde "Hey ! Lincoln..."

    menu:
        clyde "Alors, comment ça va aujourd'hui ?"
        "Bien ! Rien de neuf..." if True:
            hide Clyde_P
            hide screen User
            jump bus_1_arrive
        "Non, Pas trop..." if mastu_dream_leni == True:
            hide Clyde_P
            hide screen User
            jump bus_1_ko

label bus_1_ko:
    show Clyde_P at right
    show screen User(tenue, "I")
    with fondu
    menu:
        clyde "Qu'est-ce qui ne va pas ?"
        "Ce matin je suis entré dans la salle de bain alors que Leni prenait sa douche..." if mastu_dream_leni == True:
            hide Clyde_P
            hide screen User
            jump bus_1_leni
        "Oh... Ce n'est rien, laisse tomber..." if True:
            hide Clyde_P
            hide screen User
            jump bus_1_ko_2

label bus_1_ko_2:
    show Clyde_P at right
    show screen User(tenue, "I")
    with fondu
    clyde "Sûrement pas, je suis ton meilleur ami et les amis ça sert à se serrer les coudes !"

    menu:
        clyde "Dis-moi ce qui ne va pas ?"
        "J'ai vu Leni sous la douche et ça m'a donné une gaule d'enfer !" if mastu_dream_leni == True:
            hide Clyde_P
            hide screen User
            jump bus_1_leni
        "Je t'ai dit que tout allait bien !" if True:
            hide Clyde_P
            hide screen User
            jump bus_1_ko_3

label bus_1_ko_3:
    show screen User(tenue, "I")
    show Clyde_T at right
    with fondu
    clyde "Désolé... Je ne voulais pas t'énerver."
    clyde "Tu pourras venir m'en parler plus tard..."

    $ love_clyde_points -= 15

    hide Clyde_T
    hide screen User
    jump bus_1_arrive

label bus_1_leni:
    show screen User(tenue, "I")
    show Clyde_P at right
    with fondu
    clyde "QUOI !!?"
    hide Clyde_P
    show I_Clyde at right
    show screen User(tenue, "_P")
    with fondu
    user "Hey, ne crie pas comme ça !"
    hide I_Clyde
    show Clyde_P at right
    show screen User(tenue, "I")
    with fondu

    menu:
        clyde "Oui c'est vrai désolé... Et alors tu as fait quoi ?"
        "Je me suis masturbé comme un fou dans ma chambre" if True:
            hide Clyde_P
            hide screen User
            jump bus_1_mastu
        "J'ai bien essayé de me masturber dans la salle de bain pendant qu'elle se lavait, mais Lori a tout gâché..." if mastu_dream_lori == True:
            hide Clyde_P
            hide screen User
            jump bus_1_lori

label bus_1_lori:
    show Clyde_X at right
    show screen User(tenue, "I")
    show B_lori_nue behind Clyde_X:
        xalign 0.7
        yalign 1.0
    with fondu
    clyde "LORI ÉTAIT LÀ AUSSI !? ELLE ÉTAIT NUE !?"

    $ sex_clyde_points += 30
    $ love_clyde_points += 10

    hide B_lori_nue
    hide Clyde_X
    show I_Clyde at right
    show screen User(tenue, "_P")
    with fondu
    user "CLYDE ! Calme toi et arrête de crier !"
    hide I_Clyde
    show Clyde_P at right
    show screen User(tenue, "I")
    with fondu
    clyde "Oui c'est vrai désolé Lincoln... Et alors Lori !?"
    hide Clyde_P
    show I_Clyde at right
    show screen User(tenue, "_P")
    with fondu
    user "Lori était habillée et elle m'a juste crié dessus."
    hide I_Clyde
    show Clyde_P at right
    show screen User(tenue, "I")
    with fondu
    clyde "Oh... Dommage... Enfin je veux dire c'est dommage pour toi !{w} Ha !{w} Ha !{w} Ha !"

    $ love_clyde_points -= 10

    hide Clyde_P
    hide screen User
    with fondu
    jump bus_1_mastu_2_1_1

label bus_1_mastu:
    show Clyde_P at right
    show screen User(tenue, "I")
    with fondu

    $ love_clyde_points += 5

    menu:
        clyde "En pensant à Leni sous la douche ?"
        "Heu... Pas tout à fait" if True:
            hide Clyde_P
            hide screen User
            jump bus_1_mastu_2
        "Je veux mon neveu !" if True:
            $ sex_clyde_points += 20
            hide Clyde_P
            hide screen User
            jump bus_1_mastu_leni

label bus_1_mastu_2:
    show Clyde_P at right
    show screen User(tenue, "I")
    with fondu

    menu:
        clyde "Bah à qui alors !? Une fille de la classe ?"
        "Non j'ai pensé à Lori qui me faisait une fellation !" if mastuChoix_1 == 2:
            hide Clyde_P
            hide screen User
            jump bus_1_mastu_2_1
        "Oui c'est ça !" if True:
            hide Clyde_P
            hide screen User
            jump bus_1_mastu_2_2

label bus_1_mastu_2_1:
    show Clyde_A at right
    show screen User(tenue, "I")
    show B_masturbe_dream_lori_suce behind Clyde_X:
    with fondu
    clyde "Le corps si parfait de Lori..."
    hide Clyde_A
label bus_1_mastu_2_1_1:
    show Clyde_X at right
    show B_clyde_lori_fuck behind Clyde_X:
        xalign 0.75
        yalign 1.0
    with fondu
    clyde "Attends c'est trop je craque !"
    hide B_clyde_lori_fuck
    hide B_masturbe_dream_lori_suce
    hide Clyde_X
    hide screen User
    with fondu

    $ sex_clyde_points += 70
    $ love_clyde_points += 30

    jump bus_1_arrive

label bus_1_mastu_2_2:
    show Clyde_P at right
    show screen User(tenue, "I")
    with fondu
    clyde "Et à qui en particulier ?"

    show B_ronnie_anne_show:
        xalign 0.3
        yalign 1.0
    with fondu
    hide Clyde_P
    show I_Clyde at right
    show screen User(tenue, "_P")
    with fondu
    user "Heeuuu... À Ronnie Anne !"
    hide I_Clyde
    show Clyde_P at right
    show screen User(tenue, "I")
    with fondu
    clyde "Logique ! C'est ta petite amie !"
    hide Clyde_P
    show I_Clyde at right
    show screen User(tenue, "_P")
    with fondu
    user "CE N'EST PAS MA PETITE AMIE !!!"
    hide B_ronnie_anne_show
    hide I_Clyde
    hide screen User
    with fondu

    jump bus_1_arrive

label bus_1_mastu_leni:
    show Clyde_P at right
    show screen User(tenue, "I")
    show B_masturbe_dream_leni_douche behind Clyde_X:
        xalign 0.3
        yalign 1.0
    with fondu
    clyde "C'est vrai que Leni est pas mal... \nMais je préfère Lori personnellement !"

    hide B_masturbe_dream_leni_douche
    hide Clyde_P
    show I_Clyde at right
    show screen User(tenue, "_P")
    with fondu
    user "Je ne m'en serais pas douté... \nAttends comment ça Leni est pas mal !?"

    hide I_Clyde
    show Clyde_P at right
    show screen User(tenue, "I")
    with fondu
    clyde "Bah oui, tu vis avec des top modèles ! {w}\nAttends Lori est une vraie déesse, {w}\nLeni à un corps de mannequin, {w}\nLuna à ce côté sauvage qui fait bander les gars, Luan est..."



    hide Clyde_P
    show I_Clyde at right
    show screen User(tenue, "_P")
    with fondu
    user "C'EST BON ! C'est bon ! J'ai compris ! {w}Pas besoin de faire toutes mes soeurs !"
    hide I_Clyde
    show Clyde_P at right
    show screen User(tenue, "I")
    with fondu
    clyde "Mais il n'y a pas que tes soeurs, Lincoln ! C'est normal,{w} elles tiennent leur sex-appeal de votre mère ! {w}\nAvec son incroyable et appétissant postérieur !"


    hide Clyde_P
    show I_Clyde at right
    show screen User(tenue, "_P")
    with fondu
    user "Clyde tu parles de ma mère, là ? ... {w}Et aussi tu surchauffes, et ton pantalon aussi..."
    hide I_Clyde
    show Clyde_P at right
    show screen User(tenue, "I")
    with fondu
    clyde "Oh ! Mince j'ai éjaculé... {w}C'est nul..."

    $ love_clyde_points -= 10
    $ sex_clyde_points = 0

    hide Clyde_P
    show I_Clyde at right
    show screen User(tenue, "_P")
    with fondu
    user "On arrive au lycée ! tu nettoieras ça aux toilettes."
    hide I_Clyde
    hide screen User
    with fondu
    jump bus_1_arrive

label bus_1_arrive:
    scene BG_lycee
    with fondu
    play sound "audio/VOITURE.mp3"
    show bus
    with inL
    nar "Le bus arrive au lycée..."
    nar "La joie des beaux jours et des jupes qui volent au vent... \nQue de bons moments en perspectives..."

    hide bus
    with outR
    stop sound

    show Clyde_P at right
    show screen User(tenue, "I")
    with inL
    clyde "Je te rejoins Lincoln, je vais aux toilettes."
    hide Clyde_P
    show screen User(tenue, "_P")
    show I_Clyde at right
    with fondu
    user "Ok Clyde !"
    hide I_Clyde
    with outR
    hide screen User
    jump exit_school
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
