image TUTO_loud = "Images/Bases/Tutoriels/loud.png"
image TUTO_ecole = "Images/Bases/Tutoriels/ecole.png"
image TUTO_mall = "Images/Bases/Tutoriels/mall.png"
image TUTO_flip = "Images/Bases/Tutoriels/flip.png"
image TUTO_fleches = "Images/Bases/Tutoriels/fleches.png"
image TUTO_maisons = "Images/Bases/Tutoriels/maisons.png"
image TUTO_eglise = "Images/Bases/Tutoriels/eglise.png"
image TUTO_parc = "Images/Bases/Tutoriels/parc.png"
image TUTO_hopital = "Images/Bases/Tutoriels/hopital.png"
image TUTO_bride = "Images/Bases/Tutoriels/bride.png"
image TUTO_theatre = "Images/Bases/Tutoriels/theatre.png"
image TUTO_permis = "Images/Bases/Tutoriels/permis.png"
image TUTO_temps = "Images/Bases/Tutoriels/temps.png"
image TUTO_menu = "Images/Bases/Tutoriels/menu.png"

image TUTO_couloir_l1_l2 = "Images/Bases/Tutoriels/couloir_1.png"
image TUTO_couloir_l3_l4 = "Images/Bases/Tutoriels/couloir_2.png"
image TUTO_couloir_l5_l7 = "Images/Bases/Tutoriels/couloir_3.png"
image TUTO_couloir_l8_l9 = "Images/Bases/Tutoriels/couloir_4.png"
image TUTO_couloir_l10_l11 = "Images/Bases/Tutoriels/couloir_5.png"
image TUTO_couloir_user = "Images/Bases/Tutoriels/couloir_6.png"
image TUTO_couloir_shower = "Images/Bases/Tutoriels/couloir_7.png"
image TUTO_couloir_recap = "Images/Bases/Tutoriels/couloir_8.png"

label IntroCouloir:
    $ INTRO_Actif = 1
    scene BG_couloir
    hide screen user_stats
    show screen User(tenue, "_P")
    with fondu
    user "Bienvenue chez les Loud"
    user "Voici le premier étage"
    user "vous y trouverez les chambres de mes différentes soeurs"
    hide screen User
    show TUTO_couloir_l1_l2
    with fondu
    nar "La chambre de Lori et Leni"
    nar "Lori n'est là que du vendredi au dimanche"
    hide TUTO_couloir_l1_l2
    show TUTO_couloir_l3_l4
    with fondu
    nar "La chambre de Luna et Luan"
    hide TUTO_couloir_l3_l4
    show TUTO_couloir_l5_l7
    with fondu
    nar "La chambre de Lynn et Lucy"
    hide TUTO_couloir_l5_l7
    show TUTO_couloir_l8_l9
    with fondu
    nar "La chambre des jumelles Lana et Lola"
    hide TUTO_couloir_l8_l9
    show TUTO_couloir_l10_l11
    with fondu
    nar "La chambre de Lisa et Lily"
    nar "Lisa, tiens une boutique de serum dans sa chambre !"
    hide TUTO_couloir_l10_l11
    show TUTO_couloir_user
    with fondu
    nar "La chambre de Lincoln"
    hide TUTO_couloir_user
    show TUTO_couloir_shower
    with fondu
    nar "La salle de bain est au bout du couloir"
    hide TUTO_couloir_shower
    show BG_couloir
    with fondu
    nar "L'accès au grenier et l'escalier vers le rez-de-chaussée sont faciles à trouver"
    pause
    hide BG_couloir
    show TUTO_couloir_recap
    with fondu
    pause
    show screen User(tenue, "_P")
    with fondu
    user "Super avec ces informations, je suis prêt pour l'aventure !"
    hide screen User
    show screen user_stats
    call screen couloir

label IntroVille:
    $ INTRO_Actif = 2
    scene BG_ville
    hide screen user_stats
    show screen User(tenue, "_P")
    with fondu
    user "Bienvenue à Royal Wood !"
    user "Voici la carte principale du jeu,"
    user "vous y trouverez les différents points d'accès aux multiples zones qui composent la ville."

    show TUTO_loud
    with fondu
    hide screen User
    nar "Voici la maison des Loud, c'est l'endroit où votre famille de 10 soeurs, vos parents et vous vivez !"
    nar "C'est ici que vous trouverez, le plus grand nombre d'actions avec votre famille."
    hide TUTO_loud
    show TUTO_bride
    with fondu
    nar "Chez les Mc Bride, c'est la maison de votre meilleur ami."
    nar "Elle n'est actuellemnt pas utilisé et donc reste en cours de développement."
    hide TUTO_bride
    show TUTO_mall
    with fondu
    show screen Actor1("l2", "nue", "normal", "sh_1", "sb_1", "normal", "boucle_1", "lunettes", "", "Joyeux", "P")
    l2 "Le centre commercial !!!!"
    show screen Actor1("l2", "nue", "normal", "sh_1", "sb_1", "normal", "boucle_1", "lunettes", "", "Joyeux", "")
    show screen User(tenue, "_P")
    user "Oui, merci Leni !"
    hide screen Actor1
    hide screen User
    nar "C'est l'endroit où vous trouverez tout ce que votre coeur désire... Ou presque !"
    hide TUTO_mall
    show TUTO_menu
    with fondu
    nar "Attention à votre budget, vous pouvez voir le nombre de $ que vous avez dans votre page d'information"
    nar "en haut a gauche sous votre photo."
    hide TUTO_menu
    show TUTO_flip
    with fondu
    nar "Chez Flip, attention aux arnaques !"
    nar "Il est toujours à la recherche du bon pigeon,"
    nar "une aubenne pour trouver un travail et se faire un petit salaire."
    hide TUTO_flip
    show TUTO_parc
    with fondu
    nar "Le parc un endroit idéal pour se détendre, faire du sport et pourquoi pas espionner les joggeuses."
    nar "C'est ici que vous pourrez augmenter votre force en vous entrainant"
    nar "ou votre ruse en vous cachant dans les buissons."
    hide TUTO_parc
    show TUTO_theatre
    with fondu
    nar "La salle de concert on y fait aussi d'autre évènements comme les conventions d'Ace Savy !"
    nar "Malheureusement, il faudra encore attendre pour découvrir tout ça !"
    hide TUTO_theatre
    show TUTO_fleches
    with fondu
    nar "En haut direction la grande ville de Great Lakes City pour rendre visite a Ronnie Anne et Lori."
    nar "Mais pour cela, il faut d'abord avoir le permis et vanzilla !"
    nar "La grande ville sera disponible dans la version 0.6.0, donc patience."
    nar "En bas direction la plage et les bikinis !"
    nar "Vous avez aussi la possibilité de vous entrainer à la natation"
    nar "et ainsi augmenté votre force."
    hide TUTO_fleches
    show TUTO_eglise
    with fondu
    nar "Besoin de se confesser ?\n Ou une envie de nonnes sexy ?\n C'est ici !"
    nar "Pour l'instant le couvent entier est en séminaire donc il faudra attendre une future mise à jour."
    hide TUTO_eglise
    show TUTO_hopital
    with fondu
    nar "Un problème de santé ?\n Ou juste une envie d'infirmières ?\n Par ici !"
    nar "En raison du Covid-19 l'hôpital est fermé."
    hide TUTO_hopital
    show TUTO_permis
    with fondu
    nar "Ici vous pourrez passer votre permis pour partir vers l'infini et au dela !"
    nar "Attention le permis c'est pas gratuit !"
    hide TUTO_permis
    show TUTO_maisons
    with fondu
    nar "Tant de maisons a découvrir, chacune d'elle abrite une délicieuse créature ou plus..."
    nar "Enfin attention quand même à monsieur Grouse."
    hide TUTO_maisons
    show TUTO_temps
    with fondu
    nar "Chaques déplacements dans la ville te prendras du temps."
    nar "Donc attention à bien jaugé cela."
    pause
    hide TUTO_temps
    with fondu
    show screen user_stats
    show screen User(tenue, "_P")
    user "Bon avec toutes ses informations ça devrait aller !"
    hide screen User
    $ city_in = True
    scene BG_ville
    with fondu
    call screen ville
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
