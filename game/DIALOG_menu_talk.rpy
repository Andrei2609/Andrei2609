label talk_debut(idTalk):
    if talkCible == mom or talkCible == l1 or talkCible == l2 or talkCible == l3 or talkCible == l4 or talkCible == l5:
        $ warn = warn_loud_points
    elif talkCible == cristina or talkCible == stella or talkCible == mollie or talkCible == joy or talkCible == jordan or talkCible == chloe or talkCible == emma or talkCible == prof1 or talkCible == prof2 or talkCible == prof3 or talkCible == nurse:
        $ warn = warn_school_points
    elif True:
        $ warn = warn_ville_points

    $ vie_points -= 10

    if idTalk == 1:
        jump talk_1_1
    elif idTalk == 2:
        jump talk_2_1
    elif idTalk == 3:
        jump talk_3_1
    elif idTalk == 4:
        jump talk_4_1
    elif idTalk == 5:
        jump talk_5_1
    elif idTalk == 6:
        jump talk_6_1
    elif idTalk == 7:
        jump talk_7_1
    elif idTalk == 8:
        jump talk_8_1

label talk_end:
    if talkCible == mom or talkCible == l1 or talkCible == l2 or talkCible == l3 or talkCible == l4 or talkCible == l5:
        $ warn_loud_points += warn
    elif talkCible == cristina or talkCible == stella or talkCible == mollie or talkCible == joy or talkCible == jordan or talkCible == chloe or talkCible == emma or talkCible == prof1 or talkCible == prof2 or talkCible == prof3 or talkCible == nurse:
        $ warn_school_points += warn
    elif True:
        $ warn_ville_points += warn

    if talkCible == mom:
        $ love_mom_points += loveCible
        $ sex_mom_points += sexCible
    elif talkCible == l1:
        $ love_l1_points += loveCible
        $ sex_l1_points += sexCible
    elif talkCible == l2:
        $ love_l2_points += loveCible
        $ sex_l2_points += sexCible
    elif talkCible == l3:
        $ love_l3_points += loveCible
        $ sex_l3_points += sexCible
    elif talkCible == l4:
        $ love_l4_points += loveCible
        $ sex_l4_points += sexCible
    elif talkCible == l5:
        $ love_l5_points += loveCible
        $ sex_l5_points += sexCible
    elif talkCible == ronnie:
        $ love_ronnie_points += loveCible
        $ sex_ronnie_points += sexCible
    elif talkCible == jordan:
        $ love_jordan_points += loveCible
        $ sex_jordan_points += sexCible
    elif talkCible == joy:
        $ love_joy_points += loveCible
        $ sex_joy_points += sexCible
    elif talkCible == cristina:
        $ love_cristina_points += loveCible
        $ sex_cristina_points += sexCible
    elif talkCible == stella:
        $ love_stella_points += loveCible
        $ sex_stella_points += sexCible
    elif talkCible == mollie:
        $ love_mollie_points += loveCible
        $ sex_mollie_points += sexCible
    elif talkCible == chloe:
        $ love_chloe_points += loveCible
        $ sex_chloe_points += sexCible
    elif talkCible == emma:
        $ love_emma_points += loveCible
        $ sex_emma_points += sexCible
    elif talkCible == prof1:
        $ love_prof1_points += loveCible
        $ sex_prof1_points += sexCible
    elif talkCible == prof2:
        $ love_prof2_points += loveCible
        $ sex_prof2_points += sexCible
    elif talkCible == prof3:
        $ love_prof3_points += loveCible
        $ sex_prof3_points += sexCible
    elif talkCible == nurse:
        $ love_nurse_points += loveCible
        $ sex_nurse_points += sexCible

    $ talkCible = ""
    $ loveCible = 0
    $ sexCible = 0
    $ warn = 0
    hide screen Actor1
    jump talk_quit

label talk_quit:
    if checkZone == "ch_user":
        jump cham_user
    elif checkZone == "ch_mom":
        jump ch_in_mom
    elif checkZone == "ch_l1_l2":
        jump ch_in_l1_l2
    elif checkZone == "ch_l3_l4":
        jump ch_in_l3_l4
    elif checkZone == "ch_l5_l7":
        jump ch_in_l5_l7
    elif checkZone == "ch_l8_l9":
        jump ch_in_l8_l9
    elif checkZone == "ch_l10_l11":
        jump ch_in_l10_l11
    elif checkZone == "couloir":
        jump couloir
    elif checkZone == "cuisine":
        jump cuisine
    elif checkZone == "manger":
        jump Diningroom
    elif checkZone == "salon":
        jump salon
    elif checkZone == "entree":
        jump entree
    elif checkZone == "porch":
        jump exit
    elif checkZone == "shower":
        jump shower_in
    elif checkZone == "grenier":
        jump grenier
    elif checkZone == "garage":
        jump garage
    elif checkZone == "niche":
        jump niche
    elif checkZone == "cave":
        jump cave
    elif checkZone == "bunker":
        jump bunker_in
    elif checkZone == "donjon":
        jump bunker_sm
    elif checkZone == "jardin":
        jump jardin
    elif checkZone == "bus":
        jump bus
    elif checkZone == "cantine":
        jump cantine
    elif checkZone == "school_couloir_1":
        jump school_couloir_1
    elif checkZone == "school_couloir_2":
        jump school_couloir_2
    elif checkZone == "school_hall":
        jump hall
    elif checkZone == "school_hall":
        jump hall
    elif checkZone == "school_out":
        jump exit_school
    elif checkZone == "infirmerie":
        jump infirmerie
    elif checkZone == "gym":
        jump gym_in
    elif checkZone == "school_room_1":
        jump room_1
    elif checkZone == "school_room_2":
        jump room_2
    elif checkZone == "principal":
        jump principal
    elif checkZone == "school_wc":
        jump wc
    elif checkZone == "school_wc_girl":
        jump wc_filles
    elif checkZone == "school_wc_boy":
        jump wc_garcons
    elif checkZone == "mall_out":
        jump mall
    elif checkZone == "mall_hall":
        jump mall_in
    elif checkZone == "mall_bar":
        jump Bar_shop
    elif checkZone == "mall_general":
        jump General_shop
    elif checkZone == "mall_bd":
        jump BD_shop
    elif checkZone == "mall_bonbon":
        jump Bonbon_shop
    elif checkZone == "mall_electro":
        jump Electro_shop
    elif checkZone == "mall_vet_1":
        jump Vet_shop
    elif checkZone == "mall_vet_2":
        jump Vet_shop_2
    elif checkZone == "flip_out":
        jump flip_2
    elif checkZone == "flip_in":
        jump flip_in
    elif checkZone == "plage":
        jump plage
    elif checkZone == "parc":
        jump parc
    elif checkZone == "eglise":
        jump eglise
    elif checkZone == "hopital":
        jump hopital
    elif checkZone == "dmv_out":
        jump DMV_2
    elif checkZone == "dmv_hall":
        jump DMV_in
    elif checkZone == "dent_hall":
        jump dentiste_in
    elif checkZone == "dent_room":
        jump rita_job_in
    elif checkZone == "theatre_out":
        jump theatre_2
    elif checkZone == "theatre_hall":
        jump theatre_in
    elif checkZone == "casagrande_out":
        jump casagrande
    elif checkZone == "cristina_out":
        jump m_cristina
    elif checkZone == "jordan_out":
        jump m_jordan
    elif checkZone == "joy_out":
        jump m_joy
    elif checkZone == "mollie_out":
        jump m_mollie
    elif checkZone == "sam_out":
        jump m_sam
    elif checkZone == "stella_out":
        jump m_stella
    elif checkZone == "grouse_out":
        jump m_cristina
    elif checkZone == "new_voisin_out":
        jump m_new_voisin
    elif checkZone == "mcbride_out":
        jump mcbride_2
    elif checkZone == "mcbride_hall":
        jump mcbride_in
    elif checkZone == "mcbride_ch_dad":
        jump cham_clyde_dad
    elif checkZone == "mcbride_ch_clyde":
        jump cham_clyde
    elif checkZone == "mcbride_shower":
        jump mcbride_shower
    elif checkZone == "map":
        jump map


label talk_1:
    call talk_debut (1) from _call_talk_debut

label talk_1_1:
    if sex_points >= 50:
        $ sexCible += 2
        $ loveCible += 1
        $ warn += 1
        talkCible "Lincoln, c'est quoi cette bosse !?"
    elif True:
        $ loveCible += 1
        talkCible "C'est agréable de parler avec toi."
    jump talk_end


label talk_2:
    call talk_debut (2) from _call_talk_debut_1

label talk_2_1:
    if sex_points >= 50:
        $ sexCible += 2
        $ loveCible += 1
        $ warn += 1
        talkCible "Lincoln, c'est quoi cette bosse !?"
    elif loveCible > 20:
        $ loveCible += 2
        $ sexCible += 1
        talkCible "C'est agréable de parler avec toi."
    elif True:
        $ loveCible -= 5
        $ warn += 1
        if talkCible == mom:
            mom "Lincoln, pourquoi tu veux parler de mon livre ? {w}C'est curieux..."
        elif talkCible == l1:
            l1 "Lincoln, pourquoi tu veux parler de Bobby ? {w}C'est bizarre..."
        elif talkCible == l2:
            l2 "Lincoln, pourquoi tu veux parler de mode ? {w}C'est bizarre..."
        elif talkCible == l3:
            l3 "Tu veux parler musique Brother ? {w}C'est Zarbe..."
        elif talkCible == l4:
            l4 "Lincoln, pourquoi tu veux me raconter une blague ? {w}C'est étrange..."
        elif talkCible == l5:
            l5 "Tu veux parler de sport, puanteur ? {w}C'est bizarre..."
        elif talkCible == ronnie:
            ronnie "Lincoln, pourquoi tu veux parler de jeux vidéo ? {w}C'est bizarre..."
        elif True:
            talkCible "Lincoln, {w}tes bizarre..."
        nar "Améliorez votre niveau d'affinité avant de réessayer."
    jump talk_end


label talk_3:
    call talk_debut (3) from _call_talk_debut_2

label talk_3_1:
    if sex_points >= 50:
        $ loveCible += 2
        $ sexCible += 2
        talkCible "Lincoln, c'est moi qui te rends comme ça ?"
        menu:
            "Oui" if True:
                $ sexCible += 5
                if talkCible == l2:
                    l2 "Genre... Tu vas me faire rougir !"
                elif True:
                    talkCible "Tu vas me faire rougir !"
            "Non" if True:
                $ loveCible -= 5
                $ sexCible -= 2
    elif loveCible > 50:
        $ loveCible += 3
        $ sexCible += 2
        talkCible "J'aime bien parler avec toi."
    elif True:
        $ loveCible -= 3
        $ sexCible += 1
        $ warn += 5
        talkCible "Lincoln, ça va pas !"
        nar "Améliorez votre niveau d'affinité avant de réessayer."
    jump talk_end


label talk_4:
    call talk_debut (4) from _call_talk_debut_3

label talk_4_1:
    if sex_points >= 50:
        $ loveCible += 2
        $ sexCible += 2
        talkCible "Lincoln, tu es tout excité..."
    elif loveCible > 50:
        $ loveCible += 5
        talkCible "Parler de sexe avec toi me rend toute bizarre..."
    elif True:
        $ loveCible -= 5
        $ warn += 5
        talkCible "Pervers !"
        nar "Améliorez votre niveau d'affinité avant de réessayer."
    jump talk_end


label talk_5:
    call talk_debut (5) from _call_talk_debut_4

label talk_5_1:
    if sex_points >= 50:
        $ sexCible += 2
        $ loveCible += 1
        $ warn += 1
        talkCible "Lincoln, c'est quoi cette bosse !?"
    elif True:
        $ loveCible += 1
        talkCible "Je suis occupée là, on verra plus tard pour les conseils."
    jump talk_end


label talk_6:
    call talk_debut (6) from _call_talk_debut_5

label talk_6_1:
    if sex_points >= 50:
        $ sexCible += 2
        $ loveCible += 1
        $ warn += 1
        talkCible "Lincoln, c'est quoi cette bosse !?"
    elif True:
        $ loveCible += 1
        talkCible "Tiens, mais fais si attention !"
        $ user_coins += 5
    jump talk_end


label talk_7:
    call talk_debut (7) from _call_talk_debut_6

label talk_7_1:
    if sex_points >= 50:
        $ sexCible += 2
        $ loveCible += 1
        $ warn += 1
        talkCible "Lincoln, c'est quoi cette bosse !?"
    elif True:
        $ loveCible += 1
        talkCible "C'est gentil, mais je n'ai rien a te demander pour l'instant mon grand."
    jump talk_end


label talk_TEL:
    call talk_debut (8) from _call_talk_debut_7

label talk_8_1:
    if sex_points >= 50:
        $ sexCible += 2
        $ loveCible += 1
        $ warn += 1
        talkCible "Lincoln, c'est quoi cette bosse !?"
    elif talkCible == ronnie:
        $ loveCible -= 5
        $ warn += 1
        $ ronnie_tel = True
        ronnie "Ok, tiens le voici !"
    elif True:
        $ vie_points -= 10
        ronnie "Hors de question, tu vas me la jouer Lori et Bobby."
        nar "Améliorez votre niveau d'affinité avant de réessayer."
    jump talk_end

label gift:
    jump l2_gift
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
