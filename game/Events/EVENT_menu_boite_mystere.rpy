label BM:
    $ vie_points -= 30
    if talkCible == "mom":
        $ playerBM = "Rita"
        $ playerTX = 3
        $ sex_mom_points += 5
        scene BG_rita
        show Rita_M at right
        with fondu
        hide screen mom_menu_talk
        hide screen mom_menu_sex
        call screen mysteryBox
        hide Rita_M
        with fondu
    elif talkCible == "l1":
        $ playerBM = "Lori"
        $ playerTX = 3
        $ sex_l1_points += 5
        scene BG_lori_leni
        show Lori_M at right
        with fondu
        hide screen l1_menu_talk
        hide screen l1_menu_sex
        call screen mysteryBox
        hide Lori_M
        with fondu
    elif talkCible == "l2":
        $ playerBM = "Leni"
        $ playerTX = 1
        $ sex_l2_points += 5
        scene BG_lori_leni
        show screen Actor1("l2", "nue", "normal", "", "sb_1", "normal", "", "", "", "Pensif", "")
        with fondu
        hide screen l2_menu_talk
        hide screen l2_menu_sex
        call screen mysteryBox
        hide screen Actor1
        with fondu
    elif talkCible == "l3":
        $ playerBM = "Luna"
        $ playerTX = 2
        $ sex_l3_points += 5
        scene BG_luna_luan
        show Luna_M at right
        with fondu
        hide screen l3_menu_talk
        hide screen l3_menu_sex
        call screen mysteryBox
        hide Luna_M
        with fondu
    elif talkCible == "l4":
        $ playerBM = "Luan"
        $ playerTX = 2
        $ sex_l4_points += 5
        scene BG_luna_luan
        show Luan_M at right
        with fondu
        hide screen l4_menu_talk
        hide screen l4_menu_sex
        call screen mysteryBox
        hide Luan_M
        with fondu
    elif talkCible == "l5":
        $ playerBM = "Lynn"
        $ playerTX = 4
        $ sex_l5_points += 5
        scene BG_lynn_lucy
        show Lynn_M at right
        with fondu
        hide screen l5_menu_talk
        hide screen l5_menu_sex
        call screen mysteryBox
        hide Lynn_M
        with fondu
    nar "En construction..."
    $ sex_points += 10
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
