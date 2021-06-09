label masturbe_ON:
    user "Mhm... C'est parti !"
    hide screen User
    scene BG_fantasme
    with flash
    if mastuChoix_1 == 1:
        jump masturbe_dream_leni_douche
    elif mastuChoix_1 == 2:
        jump masturbe_dream_lori_suce
    elif True:
        jump masturbe_OFF

label masturbe_OFF:
    show masturbe_user
    with flash
    user "Wahou... Ca fait du bien !"
    hide masturbe_user
    with fondu
    $ sex_points = 0
    call timer (0, 10) from _call_timer
    jump cham_user

label masturbe_dream_leni_douche:
    show screen User(tenue, "_P")
    with fondu
    user "C'est Leni qui m'a mis dans cet état,"
    user "c'est donc à elle d'arranger ça..."
    hide screen User
    with flash
    show leni_douche_ouverte_2 at right
    with fondu
    l2 "Lincoln, tu viens me laver le dos ?"
    hide leni_douche_ouverte_2
    show leni_pose_douche at right
    with fondu
    l2 "Tes mains sont si fortes... {w}Et si chaude... {w}Je mouille de partout !"
    l2 "À moins que ce soit l'eau de la douche !?"
    hide leni_pose_douche
    show leni_dos_douche_P at right
    with fondu
    l2 "Regarde mes fesses ne sont pas trop grosses ?"
    hide leni_dos_douche_P
    show leni_dos_douche at right
    show screen User(tenue, "_P")
    with fondu
    user "Non pas du tout !"
    hide leni_dos_douche
    show screen User(tenue, "I")
    show leni_dos_douche_P at right
    with fondu
    l2 "Si je suis sûr que tu n'arriverais même pas"
    l2 "à toucher mon sexe si tu me prends par derrière !?"
    hide leni_dos_douche_P
    show screen User(tenue, "_P")
    show leni_dos_douche at right
    with fondu
    user "Tu vas voir si j'y arrive pas !"
    hide screen User
    hide leni_dos_douche
    with outR
    show leni_fuck at right
    with fondu
    l2 "Ah Lincoln ! C'est si bon... {w}Ton sexe est vraiment trop gros ! {w}Aaaah Oui je jouis !"
    user "Moi aussi !!!!"
    hide leni_fuck
    show leni_fuck_cum at right
    with flash
    l2 "Oooh c'est trop bon..."
    hide leni_fuck_cum
    show leni_dos_P at right
    with fondu
    l2 "Merci Lincoln pour m'avoir aidée à prendre ma douche..."
    hide leni_dos_P
    jump masturbe_OFF

label masturbe_dream_lori_suce:
    show screen User(tenue, "_P")
    with fondu
    user "C'est Lori avec sa grande bouche qui à tout gaché dans la salle de bain..."
    hide screen User
    with flash
    show screen Actor1("l1", "colere", "normal", "sh_0", "", "", "", "", "", "Colere", "P")
    with fondu
    l1 "Lincoln !"
    show screen Actor1("l1", "colere", "normal", "sh_0", "", "", "", "", "", "Colere", "")
    show screen User(tenue, "_P")
    with fondu
    user "Quoi Lori ?"
    show screen User(tenue, "I")
    show screen Actor1("l1", "colere", "normal", "sh_0", "", "", "", "", "", "Colere", "P")
    with fondu
    l1 "Tu es vraiment un garcon énervent !"
    show screen Actor1("l1", "colere", "normal", "sh_0", "", "", "", "", "", "Colere", "")
    show screen User(tenue, "_P")
    with fondu
    user "Pourquoi tu me dis ça ?"
    show screen Actor1("l1", "nue", "normal", "sh_0", "", "", "", "", "", "Exciter", "P")
    show screen User(tenue, "I")
    with fondu
    l1 "Ferme là et viens là !"
    show screen Actor1("l1", "nue", "normal", "sh_0", "", "", "", "", "", "Exciter", "")
    show screen User(tenue, "_P")
    with fondu
    user "Heu... pourquoi !?"
    show screen Actor1("l1", "nue", "normal", "sh_0", "", "", "", "", "", "Exciter", "P")
    show screen User(tenue, "I")
    with fondu
    l1 "J'ai une soif insatiable de sperme... {w}Et tu vas te rendre utile pour une fois !"
    show screen Actor1("l1", "nue", "normal", "sh_0", "", "", "", "", "", "Exciter", "")
    show screen User(tenue, "_P")
    with fondu
    user "Si tu veux me sucer alors donne moi envie !?"
    show screen User(tenue, "I")
    show screen Actor1("l1", "nue", "normal", "sh_0", "", "", "", "", "", "Exciter", "P")
    l1 "Lincoln... {w}Tu en meurs d'envie alors fait pas ton timide et viens te faire sucer par ta grande soeur qui t'aime..."

    hide screen Actor1
    hide screen User
    show lori_BJ_1
    with flash
    user "Oh que c'est excitant..."
    hide lori_BJ_1
    show lori_BJ_2
    with fondu
    nar ""
    user "Ah oui, que c'est bon ! {w}Je vais jouir !"
    hide lori_BJ_2
    show lori_BJ_1
    with fondu
    l1 "Attend remplit moi la bouche ! {w}J'adore le goût du sperme !"
    hide lori_BJ_1
    show lori_BJ_3
    with fondu
    nar ""
    hide lori_BJ_3
    show lori_BJ_cum_1
    with flash
    user "Oooh... Oui que c'est bon ! {w}Tu aimes ça ?"
    hide lori_BJ_cum_1
    show lori_BJ_cum_2
    with fondu
    l1 "GLOUPS !"
    hide lori_BJ_cum_2
    show lori_BJ_1
    with fondu
    l1 "Tu m'étonnes ! {w}Le sperme d'un puceau,"
    l1 "il n'y a rien de plus délicieux !"
    hide lori_BJ_1
    jump masturbe_OFF
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
