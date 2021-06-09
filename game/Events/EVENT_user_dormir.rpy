label dormir:
    $ home_in = True
    $ city_in = False
    $ warn_loud_points -= 5
    $ warn_school_points -= 5
    $ warn_ville_points -= 5
    $ school_group_ext = False
    if tenue == "slip" or tenue == "slipA" or tenue == "nu":
        user "Aller au lit !"
        hide screen User
        show sleep_user
        nar "Lincoln dort paisiblement toute la nuit..."
        hide sleep_user
        with fondu
        $ vie_points = 100
        $ lynn_peek_1 = False
        $ l4_tarte = 0
        $ go_school = False
        if jour_Num > 120:
            $ saison = "ete"
            $ jour_Num = 0
        elif jour_Num > 60:
            $ saison = "hiver"
            $ jour_Num += 1
        elif True:
            $ jour_Num += 1
        if heure > 3:
            $ jour += 1
        scene BG_lincoln
        show screen User(tenue, "_P")
        with trembleV
        nar "DRIIINNG !!!!"
        if jour > 7:
            $ heure = 6
            $ minute = 30
            $ school_OK = False
            $ jour = 1
            user "haarrgg... \nUne nouvelle semaine qui commence ! \nAllez, vite à la douche !"


        elif jour == 6 or jour == 7:
            $ heure = 7
            $ minute = 0
            $ school_OK = True
            user "Haarrgg... Le Week end..."
        elif True:
            $ heure = 6
            $ minute = 30
            $ school_OK = False
            user "Haarrgg... \nUne nouvelle journée qui commence dans la maison des Loud ! \nUne bonne douche me fera du bien !"


        hide screen User
        call screen bedroom
    elif True:
        show screen User(tenue, "_P")
        with fondu
        user "Je ne peux pas dormir comme ça !"
        hide screen User
        call screen bedroom
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
