label JV:
    $ vie_points -= 30
    if talkCible == "mom":
        $ sex_mom_points += 5
    elif talkCible == "l1":
        $ sex_l1_points += 5
    elif talkCible == "l2":
        $ sex_l2_points += 5
    elif talkCible == "l3":
        $ sex_l3_points += 5
    elif talkCible == "l4":
        $ sex_l4_points += 5
    elif talkCible == "l5":
        $ sex_l5_points += 5
    nar "vous jouez aux jeux vidéo"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
