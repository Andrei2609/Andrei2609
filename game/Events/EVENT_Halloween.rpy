
image Leni_horror_2020 = "Images/Personnages/102-Leni/Event/l2_horror_2020.png"
image Leni_horror_2020_P:
    "Images/Personnages/102-Leni/Event/l2_horror_2020_P.png"
    pause .5
    "Images/Personnages/102-Leni/Event/l2_horror_2020.png"
    pause .5
    repeat
image Leni_horror_2020_H = "Images/Personnages/102-Leni/Event/l2_horror_2020_H.png"

image horror_2020_go = "Images/CG/01-Personnages/102-Leni/horror_2020/go.png"
image horror_2020_win = "Images/CG/01-Personnages/102-Leni/horror_2020/win.png"

image BG_couloir_horror_2020 = "Images/Backgrounds/couloir_horror_2020.png"

screen Horror_couloir_2020():
    add "Images/Backgrounds/couloir_horror_2020.png"
    imagebutton:
        xalign 0.6
        yalign 0.5
        idle "Images/Plans/Minis/flecheG.png"
        hover "Images/Plans/Minis/flecheG_hover.png"
        action Jump("horror_cham_2020")

label Halloween_2020_Review:
    hide screen Menu_collection
    $ review = True
    scene BG_grenier
    show Lucy_voyante_P at right
    with fondu
    jump Halloween_2020_Go

label Halloween_2020_Go:
    l7 "Tu te souviens d'Halloween dernier ? {w}\nL'invasion d'araignées dans la chambre de Leni..."

    scene BG_couloir_horror_2020
    with fondu
    l2 "Aaaaahh !!!"
    call screen Horror_couloir_2020

label horror_cham_2020:
    $ tenue = "normal"
    scene BG_lori_leni
    with fondu
    l2 "Aaaaahh !!!"
    show horror_2020_go
    with trembleV
    l2 "Des araignées !"
    hide horror_2020_go
    scene BG_couloir_horror_2020
    show screen Actor1("l2", "nue", "normal", "sh_0", "ev_1", "", "", "", "", "Triste", "P")
    show screen User(tenue, "I")
    with fondu
    l2 "Lincoln... Y'en à partout ! Sauve-moi !!!"
    show screen Actor1("l2", "nue", "normal", "sh_0", "ev_1", "", "", "", "", "Triste", "EX")
    show screen User(tenue, "_P")
    with fondu
    user "Calme toi Leni, je m'occupe de tout !"
    hide screen User
    hide screen Actor1
    scene BG_lori_leni
    with fondu
    $ spider_cont = 5
    call screen spider_game

label horror_cham_2020_victory:
    scene BG_couloir_horror_2020
    show screen Actor1("l2", "nue", "normal", "sh_0", "ev_1", "", "", "", "", "Triste", "EX")
    show screen User(tenue, "_P")
    with fondu
    user "c'est bon Leni je les ai toutes eue !"
    hide screen Actor1
    hide screen User
    show horror_2020_win
    with flash
    l2 "Genre, tes trop un héros !"
    nar ""
    hide horror_2020_win
    scene BG_grenier
    show screen User(tenue, "_P")
    show I_Lucy_voyante at right
    with fondu
    user "Oui, je m'en souviens très bien..."
    $ sex_points += 50
    hide I_Lucy_voyante
    hide screen User
    $ l2_halloween_2020 = True
    if review == True:
        $ review = False
        return
    elif True:
        jump grenier
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
