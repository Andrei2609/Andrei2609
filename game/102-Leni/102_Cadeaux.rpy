label l2_gift:
    hide screen l2_menu_talk
    user "Tiens Leni, j'ai un cadeau pour toi !"
    l2 "C'est quoi ! C'est quoi ! C'est quoi !"
    nar "en construction..."
    hide screen actor1
    menu:
        "Un Smoothie : [smoothie]" if smoothie <> "":
            jump gift_l2_smoothie
        "Du Chocolat" if chocolat > 0:
            jump gift_l2_chocolat
        "Des Fleurs" if fleur > 0:
            jump gift_l2_fleur
        "Un Mouchoir" if mouchoir > 0:
            jump gift_l2_mouchoir
        "Des Boucles d'oreilles" if boucle > 0:
            jump gift_l2_boucle
        "De la Lingerie" if lingerie_sexy > 0:
            jump gift_l2_lingerie
    jump gift_l2_KO

label gift_l2_KO:
    $ love_l2_points -= 1
    l2 "C'est pas drôle..."
    return

label gift_l2_smoothie:
    show leni_smoothie_drink
    with fondu
    pause
    hide leni_smoothie_drink
    if smoothie == "special L":
        $ l2_cum += 1
        if l2_cum >= 5:
            show leni_smoothie_OK
            with fondu
            $ love_l2_points += 5
            l2 "Un vrai délice... J'adore le goût qu'il me laisse en bouche."
            hide leni_smoothie_OK
        elif True:
            show leni_smoothie_KO
            with trembleV
            $ warn_loud_points += 5
            $ love_l2_points -= 5
            l2 "Il a un drôle de goût..."
            hide leni_smoothie_KO
    elif smoothie == "beurk":
        show leni_smoothie_KO
        with trembleV
        $ love_l2_points -= 5
        l2 "Heurk... C'est horrible ! {w}Genre beaucoup trop de... Je ne sais pas quoi !"
        hide leni_smoothie_KO
    elif True:
        show leni_smoothie_OK
        with fondu
        $ love_l2_points += 5
        l2 "Miam ! Délicieux..."
        hide leni_smoothie_OK
    $ smoothie = ""
    jump Diningroom

label gift_l2_chocolat:
    $ chocolat -= 1
    $ love_l2_points += 5
    l2 "Mhmmm... Du chocolat !{w} Le meilleur ami des filles ! \nMerci Lincoln !"

    return

label gift_l2_fleur:
    $ fleur -= 1
    $ love_l2_points += 5
    $ sex_l2_points -= 10
    l2 "Merci Lincoln, c'est trop mignon...{w} \nTu m'offres un bouquet de fleurs comme quand tu étais petit."

    return

label gift_l2_mouchoir:
    $ mouchoir -= 1
    l2 "Un mouchoir..? {w}Attends ça veux dire que mon maquillage coule !?"
    menu:
        "Oui" if True:
            jump gift_l2_mouchoir_1
        "Non" if True:
            jump gift_l2_mouchoir_2

label gift_l2_mouchoir_1:
    l2 "Je suis hideuse !{w} Aaaaah !"
    $ love_l2_points -= 15
    user "Mauvaise idée..."
    return

label gift_l2_mouchoir_2:
    l2 "Alors pourquoi m'offrir un mouchoir...?{w} C'est que j'ai le nez qui coule !? {w}\nC'est horrible ! Aaaaaah !"

    $ love_l2_points -= 10
    user "Mauvaise idée..."
    return

label gift_l2_boucle:
    $ boucle -= 1
    $ love_l2_points += 10
    $ sex_l2_points += 2
    l2 "Lincoln... {w}Elles sont trop belles... Genre c'est trop des saphirs !"
    return

label gift_l2_lingerie:
    if love_l2_points >= 50:
        $ lingerie_sexy -= 1
        $ love_l2_points += 10
        $ sex_l2_points += 10
        l2 "Lincoln... C'est trop... Merci !"
    elif True:
        $ love_l2_points -= 10
        $ warn_loud_points += 5
        l2 "Lincoln !"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
