
label debut_jeu:
    $ renpy.movie_cutscene("Images/Bases/Videos/generique.webm")
    show ch0
    nar ""



    $ game_theme = ""
    $ saison = "ete"
    $ jour = 5
    $ heure = 7
    $ minute = 0
    $ choix_calendrier = "neutre"
    $ choix_periode = "matin"
    $ choix_jour = jour
    $ choix_saison = "ete"
    $ checkZone = "ch_user"
    $ go_school = False
    $ home_in = True
    $ city_in = False
    $ ecole_in = False
    $ school_OK = False
    $ luna_peek_1 = False
    $ lynn_peek_1 = False
    $ luan_peek_1 = False
    $ mastu_dream_lori = False
    $ mastu_dream_leni = False
    $ mastuChoix_1 = 0
    $ user_room = True
    $ tenue = "slip"
    $ flip_job = False
    $ coco_jambe_1 = ""
    $ tissu_leni_1 = ""
    $ maria_sex_web = False
    $ mom_cle = "go"
    $ mom_quest_1 = False
    $ vanzilla = True
    $ talkCible = ""
    $ loveCible = ""
    $ sexCible = ""
    $ compt_porn_TV = 0
    $ plage_g4_compt = 0
    $ theatre_billet = False
    $ permis_test_go = False
    $ review = False
    $ sexName_1 = ""
    $ sexName_2 = ""
    $ jour_Num = 0
    $ INTRO_Actif = 0
    $ TV_count = 0
    $ mall_in = False
    $ loud_peek_count = 0
    $ nakedGO = False
    $ slipGO = False
    $ numInv = "pocheInv"
    $ school_group_ext = False


    scene BG_lincoln
    show screen user_stats
    show screen User(tenue, "_P")
    with fondu
    user "haarrgg... \nUne nouvelle journée qui commence dans la maison des Loud !"

    user "Oh mince je vais être en retard, vite à la douche !"

    hide screen User
    with fondu

    nar "La salle de bain est au bout du couloir, en face de ma chambre"

    call screen bedroom
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
