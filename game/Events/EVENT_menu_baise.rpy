label fucktime:
    hide screen Actor1
    if talkCible == mom:
        hide screen mom_talk
        hide screen mom_menu_sex
        scene BG_rita
    elif talkCible == l1 or talkCible == l2:
        hide screen l1_talk
        hide screen l1_menu_sex
        hide screen l2_talk
        hide screen l2_menu_sex
        scene BG_lori_leni
    elif talkCible == l3 or talkCible == l4:
        hide screen l3_talk
        hide screen l3_menu_sex
        hide screen l4_talk
        hide screen l4_menu_sex
        scene BG_luna_luan
    elif talkCible == l5:
        hide screen l5_talk
        hide screen l5_menu_sex
        scene BG_lynn_lucy
    elif True:
        scene BG_lincoln
    with fondu
    $ vie_points -= 50
    call screen Sex_Action(talkCible, "")
    $ sex_points = 0
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
