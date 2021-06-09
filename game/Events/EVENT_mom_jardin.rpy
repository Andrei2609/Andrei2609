
label mom_quest_1_Review:
    hide screen Menu_collection
    $ review = True
    $ mom_cle = "go"
    jump mom_quest_1

label mom_quest_1:
    if mom_cle == "go":
        $ mom_cle = "wait"
        if mom_quest_1 == False:
            $ mom_quest_1 = True
            show Rita_niche_ass_1 at left
            with fondu
        elif True:
            show Rita_niche_ass at left
            with fondu
        nar ""
        show Rita_niche_miniass:
            xalign 0.2
            yalign 0.3
        with trembleV
        nar ""
        show Rita_niche_minilincoln:
            xalign 0.8
            yalign 0.7
        with trembleV
        nar ""
        hide Rita_niche_miniass
        hide Rita_niche_minilincoln
        with fondu
        menu:
            "Lui toucher les fesses" if True:
                hide Rita_niche_ass
                hide Rita_niche_ass_1
                jump mom_niche_touch_ass
            "Tousser" if True:
                hide Rita_niche_ass
                hide Rita_niche_ass_1
                jump mom_niche_signal
            "Partir" if True:
                hide Rita_niche_ass
                hide Rita_niche_ass_1
                jump jardin
    elif True:
        jump niche

label mom_niche_signal:
    show Rita_niche_face_1
    with trembleV
    mom "Lincoln !? {w}c'est toi ?"
    hide Rita_niche_face_1
    show Rita_niche_face_2
    with fondu
    user "Oui, tu fais quoi !?"
    hide Rita_niche_face_2
    show Rita_niche_face_1
    with fondu
    mom "Je suis bloquée..."
    mom "Charles a encore pris mes clés et en les reprenant dans sa niche je suis rester coincée..."
    mom "Peux-tu m'aider ?"
    hide Rita_niche_face_1
    show Rita_niche_face_2
    with fondu
    user "Bien sûr, maman !"
    $ love_mom_points += 5
    hide Rita_niche_face_2
    show screen User(tenue, "I")
    with fondu
    show screen Actor1("mom", "normal", "normal", "sh_1", "sb_1", "normal", "boucle_1", "", "", "Neutre", "P")
    with inB
    mom "Merci, Lincoln... Je ne sais pas ce que j'aurais fait sans toi !"
    show screen Actor1("mom", "normal", "normal", "sh_1", "sb_1", "normal", "boucle_1", "", "", "Neutre", "")
    show screen User(tenue, "_P")
    with fondu
    user "C'était un plasir maman !"
    hide screen Actor1
    with outR
    show screen User(tenue, "_M")
    with fondu
    user "Je peux peut être m'arranger pour voler de nouveau les clés de maman"
    user "et les cacher dans la niche de Charles pour en profiter d'avantage..."
    hide screen User
    jump jardin

label mom_niche_touch_ass:
    if sex_mom_points >=50:
        $ love_mom_points += 10
        $ sex_mom_points += 10
        show Rita_niche_touch_OK_1
        with fondu
        nar ""
        menu:
            "Baisser son pantalon" if True:
                hide Rita_niche_touch_OK_1
                jump mom_niche_touch_ass_2
            "S'arrêter là" if True:
                hide Rita_niche_touch_OK_1
                jump mom_niche_signal
    elif True:
        $ love_mom_points -= 10
        $ sex_mom_points += 5
        $ warn_loud_points += 1
        show Rita_niche_touch_KO_1
        with fondu
        nar ""
        hide Rita_niche_touch_KO_1
        jump mom_niche_signal

label mom_niche_touch_ass_2:
    show Rita_niche_touch_KO_2_1
    with fondu
    nar ""
    if sex_mom_points >=80:
        $ love_mom_points += 10
        $ sex_mom_points += 10
        hide Rita_niche_touch_KO_2_1
        show Rita_niche_touch_OK_2
        with fondu
        nar ""
        menu:
            "Baisser sa culotte" if True:
                hide Rita_niche_touch_OK_2
                jump mom_niche_touch_ass_3
            "S'arrêter là" if True:
                hide Rita_niche_touch_OK_2
                jump mom_niche_signal
    elif True:
        $ love_mom_points -= 10
        $ sex_mom_points += 5
        $ warn_loud_points += 1
        hide Rita_niche_touch_KO_2_1
        show Rita_niche_touch_KO_2_2
        with fondu
        nar ""
        hide Rita_niche_touch_KO_2_2
        jump mom_niche_signal

label mom_niche_touch_ass_3:
    if sex_mom_points >=90:
        $ love_mom_points += 10
        $ sex_mom_points += 10
        show Rita_niche_touch_KO_3_a
        with fondu
        nar ""
        hide Rita_niche_touch_KO_3_a
        show Rita_niche_touch_OK_3_1
        with fondu
        nar ""
        hide Rita_niche_touch_OK_3_1
        show Rita_niche_touch_OK_3_2
        with fondu
        menu:
            "La sodomiser" if True:
                hide Rita_niche_touch_OK_3_2
                jump mom_niche_touch_fuck_time
            "S'arrêter là" if True:
                hide Rita_niche_touch_OK_3_2
                jump mom_niche_signal
    elif True:
        $ love_mom_points -= 10
        $ sex_mom_points += 5
        $ warn_loud_points += 1
        show Rita_niche_touch_KO_3
        with fondu
        nar ""
        hide Rita_niche_touch_KO_3
        jump mom_niche_signal

label mom_niche_touch_fuck_time:
    show Rita_niche_touch_KO_4
    with fondu
    nar ""
    if sex_mom_points >=100:
        $ love_mom_points += 10
        $ sex_mom_points += 10
        hide Rita_niche_touch_KO_4
        show Rita_niche_touch_OK_4_1
        with fondu
        nar ""
        hide Rita_niche_touch_OK_4_1
        show Rita_niche_touch_OK_4_2
        with fondu
        nar ""
        hide Rita_niche_touch_OK_4_2
        show Rita_niche_touch_OK_4_anim
        with fondu
        nar ""
        hide Rita_niche_touch_OK_4_anim
        show Rita_niche_fuck_1
        with flash
        nar ""
        hide Rita_niche_fuck_1
        show Rita_niche_fuck_2
        with fondu
        nar ""
        menu:
            "Jouir dedans" if True:
                hide Rita_niche_fuck_2
                jump mom_niche_cum_in
            "Jouir dehors" if True:
                hide Rita_niche_fuck_2
                jump mom_niche_cum_out
    elif True:
        $ love_mom_points -= 10
        $ sex_mom_points += 5
        $ warn_loud_points += 1
        hide Rita_niche_touch_KO_4
        jump mom_niche_signal

label mom_niche_cum_in:
    show Rita_niche_cum_in_1
    with flash
    nar ""
    hide Rita_niche_cum_in_1
    show Rita_niche_cum_in_1
    with flash
    nar ""
    hide Rita_niche_cum_in_1
    show Rita_niche_cum_in_1
    with flash
    nar ""
    hide Rita_niche_cum_in_1
    jump mom_niche_sex_end

label mom_niche_cum_out:
    show Rita_niche_cum_out_1
    with flash
    nar ""
    hide Rita_niche_cum_out_1
    show Rita_niche_cum_out_1
    with flash
    nar ""
    hide Rita_niche_cum_out_1
    show Rita_niche_cum_out_2
    with flash
    nar ""
    hide Rita_niche_cum_out_2
    jump mom_niche_sex_end

label mom_niche_sex_end:
    show Rita_niche_face_1
    with fondu
    mom "Lincoln... C'est bien toi ?"
    hide Rita_niche_face_1
    show Rita_niche_face_2
    with fondu
    user "Oui, un coup de main !?"
    hide Rita_niche_face_2
    show Rita_niche_face_1
    with fondu
    mom "Après ce coup de queue, j'en ai bien besoin..."
    hide Rita_niche_face_1
    show Rita_niche_face_2
    with fondu
    user "Un instant."
    $ love_mom_points += 5
    hide Rita_niche_face_2
    show screen User(tenue, "I")
    with fondu
    show screen Actor1("mom", "normal", "normalA", "sh_0", "sb_1", "normal", "boucle_1", "", "", "Neutre", "P")
    with inB
    mom "Merci, Lincoln... Je ne sais pas ce que j'aurais fait sans toi !"
    show screen Actor1("mom", "normal", "normalA", "sh_0", "sb_1", "normal", "boucle_1", "", "", "Neutre", "")
    show screen User(tenue, "_P")
    with fondu
    user "C'était un plasir maman !"
    hide screen Actor1
    with outR
    show screen User(tenue, "_M")
    with fondu
    user "J'aime bien ce petit moment avec ma mère. {w}\nFaudrait qu'on s'en refasse un à l'occasion..."

    hide screen User
    if review == True:
        $ review = False
        return
    elif True:
        $ mom_dog_house = True
        jump jardin
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
