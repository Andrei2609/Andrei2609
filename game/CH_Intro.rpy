label start:
    scene BG_maison_J
    with fondu
    show k_P at left
    with inL
    k "Bienvenue dans le jeu hentai de{w}\nBienvenue chez les Loud !"
    hide k_P
    show I_k at left
    with fondu
    show B_18:
        xalign 0.5
        yalign 0.5
    with fondu
    nar "{color=#FF0000}{u}{b}Attention :{/b}{/u} ce jeu est un jeu pornographique.{/color}"
    hide B_18
    hide I_k
    show k_P at left
    with fondu
    menu:
        k "Avant de commencer, avez-vous plus de 18 ans (ou de 21 ans, selon votre pays) ?"
        "Je suis majeur (+18)" if True:
            jump go
        "Je suis mineur (-18)" if True:
            jump end

label end:
    hide k_P
    show k_Oeil at left
    with fondu
    k "Désolé, revenez quand vous aurez l'âge !"
    hide k_Oeil
    with outR
    return

label go:
    scene BG_salon
    with fondu
    show Intro_Lincoln_salut at right
    with inL
    hide k_P
    show I_k at left
    with fondu
    user "Attends ! Attends ! C'est un jeu porno dans lequel va apparaître toute ma famille !?"
    hide Intro_Lincoln_salut
    with outB
    hide I_k
    show k_P at left
    with fondu
    k "C'est vrai, ça me fait penser que ce jeu est une parodie"
    k "de l'oeuvre de {color=#FF5733}Nickelodéon{/color}(Viacom)"
    k "Bienvenue chez les Loud,"
    k "de ce fait les personnages et les lieux"
    k "présents dans cette oeuvre sont la propriété intellectuelle"
    k "de {color=#FF5733}Nickelodéon{/color}(Viacom)."
    show Intro_Lincoln_P at right
    with inB
    hide k_P
    show I_k at left
    with fondu
    user "Ce n'est pas vraiment ce que je voulais dire..."
    hide Intro_Lincoln_P
    with outB
    hide I_k
    show k_P at left
    with fondu
    show B_incest:
        xalign 0.3
        yalign 0.2
    with fondu
    pause 0.2
    show B_pedophilie:
        xalign 0.4
        yalign 0.3
    with fondu
    pause 0.2
    show B_zoophilie:
        xalign 0.55
        yalign 0.2
    with fondu
    pause 0.2
    show B_etc:
        xalign 0.63
        yalign 0.35
    with fondu
    k "Ce jeu ne prône en aucun cas l'{color=#FF0000}inceste{/color},"
    k "la {color=#FF0000}pédophilie{/color}, la {color=#FF0000}zoophilie{/color},"
    k "ou toute autre pratique éthiquement discutable pouvant figurer dans ce jeu."
    hide k_P
    show I_k behind d_P:
        xalign 0.0 yalign 2.0
        linear 1.0 xalign 0.1
    with fondu
    show d_P at left
    with inL
    d "L'équipe tien a précisez clairement que l'ensemble des personnages jouables"
    d "et des PNJ a caractères sexuelles ont toutes 18 ans ou plus !"
    d "et que l'ensemble des personnages mineurs dans ce jeu"
    d "n'aurons {color=#FF0000}JAMAIS{/color} un rôle sexuel à jouer dans l'histoire"
    hide B_incest
    hide B_pedophilie
    hide B_zoophilie
    hide B_etc
    hide d_P
    show I_d behind I_k:
        xalign 0.2
    show I_k at left
    with fondu
    show Intro_Lincoln_S at right
    with inB
    user "ZOOPHILIE !!! heuuu..."
    hide Intro_Lincoln_S
    with outB
    hide I_k
    show k_P at left
    with fondu
    k "Et pour cela nous allons faire un bond de quelques années dans le futur !"
    hide k_P
    show I_k at left
    with fondu
    show Intro_Lincoln_P at right
    with inR
    user "QUOI !?"
    hide Intro_Lincoln_P
    show Intro_Lincoln_vieux_P at right
    with flash
    user "Qu'est-ce qui vient de se passer !?"
    hide I_k
    show k_P at left
    with fondu
    hide Intro_Lincoln_vieux_P
    with outR
    k "On vient de voyager dans le temps !{w} \nUne dernière chose, les 5 dernières soeurs Loud"

    hide k_P
    hide I_d
    show I_k behind d_P:
        xalign 0.1
    show d_P at left
    with fondu
    show Lucy_jeune behind k_P:
        xalign 0.45 yalign 1.0
    with inB
    d "Lucy"
    show Lana_jeune behind K_P:
        xalign 0.7 yalign 1.0
    with inB
    d "Lana"
    show Lola_jeune behind K_P:
        xalign 0.8 yalign 1.0
    with inB
    d "Lola"
    show Lisa_jeune behind K_P:
        xalign 0.95 yalign 1.0
    with inB
    d "Lisa"
    show Lily_jeune behind K_P:
        xalign 1.0 yalign 1.0
    with inB
    d "et Lily"
    d "n'auront pas de chapitre propre à elle,"
    d "elles n'auront que des rôles de figurantes sans scènes pornographiques à cause de leur age."
    hide Lucy_jeune
    hide Lana_jeune
    hide Lola_jeune
    hide Lisa_jeune
    hide Lily_jeune
    hide d_P
    hide I_k
    show I_d behind k_Oeil:
        xalign 0.2
    show k_Oeil at left
    with fondu
    k "Bon jeu et bonne bourre a tous !"
    hide k_Oeil
    with outL
    hide I_d
    show d_P at left
    with fondu
    d "Et amusez vous comme des petits fous !"
    hide d_P
    with outL
    jump debut_jeu
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
