label ronnie_talk_2:
    if sex_points >= 50:
        $ sex_ronnie_points += 5
        $ warn_ronnie_points += 10
        $ vie_points -= 10

        ronnie "Lincoln, tu bandes !"
    elif love_ronnie_points > 20:
        $ love_ronnie_points += 15
        $ vie_points -= 10

        ronnie "C'est agréable de parler avec toi."
    elif True:
        $ love_ronnie_points -= 5
        $ warn_ronnie_points += 10
        $ vie_points -= 10

        ronnie "Lincoln, pourquoi tu veux parler de jeux vidéo ? {w}C'est bizarre..."
        nar "Améliorez votre niveau d'affinité avant de réessayer."
    return

label ronnie_tel:
    nar "en construction"
    if sex_points >= 50:
        $ sex_ronnie_points += 5
        $ warn_ronnie_points += 10
        $ vie_points -= 10

        ronnie "Lincoln, tu bandes !"

    elif love_ronnie_points >= 10:
        $ vie_points -= 10
        $ ronnie_tel = True

        ronnie "Ok, tiens le voici !"
    elif True:

        $ vie_points -= 10

        ronnie "Hors de question, tu vas me la jouer Lori et Bobby."
        nar "Améliorez votre niveau d'affinité avant de réessayer."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
