import marimo

__generated_with = "0.19.4"
app = marimo.App(width="medium", css_file="../assets/custom.css")


with app.setup(hide_code=True):

    def page_():
        from here import Embed

        return Embed(__file__, globals()["app"], "Digestive problems")


@app.cell(hide_code=True)
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    lang_selector = mo.Html(
        """
        <input type="radio" name="language" id="english" class="lang-toggle" checked>
        <input type="radio" name="language" id="french" class="lang-toggle">

        <nav class="tabs">
          <label for="english" class="tab-label">English</label>
          <label for="french" class="tab-label">Français</label>
        </nav>
        """
    )

    def multilang(english_content, french_content):
        en_html = mo.as_html(english_content).text
        fr_html = mo.as_html(french_content).text
        return mo.Html(f"""
        <article id="doc-en" class="document">
        {en_html}
        </article>

        <article id="doc-fr" class="document">
        {fr_html}
        </article>
        """)

    return lang_selector, multilang


@app.cell(hide_code=True)
def _(mo):
    en = mo.md("""
    TL;DR: I have digestive problems. They greatly impact my life, so I explain them here.

    **disclaimer**: this page contains sensible health information. I trust you, as a reader, to treat them responsibly.

    Some disabilities are visible, other are hidden. Hidden disabilities tend to crate confusion and tensions, because outsiders misinterpret the behaviour of the handicapped person. This is the case in particular for social interactions and at work: a friend or a collegue can interpret a behaviour as rude / depressed / dumb / irresponsible, because he lacks the context of the handicap.

    It has been the case for me. For quite some time now, I suffer from digestive issues, and they are a major challenge in my life. This page aims at providing context on the subject.

    They are 2 other reasons why I decided to write this document. First, I think it might help me to relieve some of the psychological pressure I associate with this condition. If more people know it and accept it's a real ~health~ problem, I can start treating it as such, without having to hide my symptoms. Second, I think my condition is more widespread than one might think. You may even know other people who suffer from similar problems, and if it's the case I hope what you will read here will be a good start to help them.

    # Symptoms (they suck)

    A doctor would say that I suffer from chronic upper-abdominal discomfort, severe bloating and slow transit.

    Although it's true, it's not very helpful to understand what the experience looks like. And if you want to understand the problems I face, you really have to understand the experience.

    1. **abdominal discomfort**. Imagine the sensation when you eat too much too quickly. It's slightly painful, it can hinder some of your actions, and it's especially unpleasant. You can't really pinpoint where the pain is: it's a diffuse sensation of discomfort. My main symptom is exactly that, except that it can persist all day long (not just after meals), that it can be a concern to fall asleep, and that your body constantly tries to find a posture that causes less discomfort. This last one creates muscle tensions, and more broadly back pain.

    2. **severe bloating**. This is the cause of abdominal discomfort. My intestines holds more food, gas and liquid than the average person, which increases the pressure. My abdomen is not flat, but inflated.

    3. **slow transit**. Some days, I can't use the toilet. Generally, food takes more time than average to traverse my digestive track

    4. **chronic**. The symptoms I described are not constant, fortunately, or at least not the worst version of them. But I have lived with it for a very long time, probably since 2023, 3 years ago. The symptoms appear in phases. I can feel ok for 2 weeks, then worse for 1 week, and suffer terribly for 3 days.


    The symptoms I described impact my whole life. I would say that the first consequence is the difficulty to focus. My whole brain directs its attention to the discomfort, and I have almost no way to counter this. This makes working, learning, and even playing games harder. Then, there is overall mood. After a few days of discomfort and not being able to focus properly, my mood go down rapidly. After this comes sleep, and then physical performances. I stayed slightly underweight for 3 years, not as a decision but as a consequence of my digestive issues.

    I don't want you to feel sorry for me. I want to give the most detailed explanation, so that you understand the context.

    # Solutions (and non-solutions)

    After multiple years of symptoms, diet changes and tests, I have a better idea of what improve my symptoms, and what worsen them.

    Let's start with the triggers

    ## Negative impact

    - no fiber
    - some foods (lentils, onions, chickpeas, too much bread)

    ## Neutral impact

    - relaxation
    - antispasmodics
    - drinking more or less
    - activities to get out of my head
    - more sport (although, maybe a small)

    ## Positive impact

    - avoiding the negative (diet in the next section)
    - heating pad
    - walking

    ## Diet

    TODO


    # Theories

    One of the hardest things for me in this situation is not having a good theory of what I have.

    I have studied the problem with more or less competent medical professionals, and I still don't have a clear diagnostic.

    - It's not gluten intolerance or celiac disease. I have tested gluten free diet without much effect and I tested negative for celliac in my blood tests.
    - It's not genetics. I was great 3 years ago, and my family don't have such problems.
    - It's probably not just intolerance. I have tested to exclude almost every aliment during weeks, and symptom s never resolve.
    - It's not just a bad habit like "not enough sport", "not enough fiber" or "too much stress". I am very mindful about doing enough sport, eating a lot of vegetables and doing meditation / relaxation.
    - It's not psychological. I clearly have food triggers, even when I feel really good.


    Below is my current best theory. It can be completely wrong, but I would say I'm 20% confident this is exactly what I have, and 80% confident at least half of it is true.



    But there are still things I can't explain, like why I had an horrible phase around 2 years ago, followed by very few symptoms for months ? Hoh did I handle lentils, onions and beans (food that trigger a lot of symptoms currently) during one week when I was hiking with friends ?

    # Next steps

    # Conclusion
    """)
    return (en,)


@app.cell(hide_code=True)
def _(mo):
    fr = mo.md("""
    Résumé: J'ai de sérieux problèmes digestifs. Ils impactent ma vie de manière significative, donc je les explique ici.

    **avertissement**: ce poste contient des données de santé sensibles. Je fais confiance au lecteur pour les considérer comme telles, de manière responsable.

    Certains handicaps sont visibles, d'autres non. Les handicaps invisiblent ont tendance à créer des conflits et de la confusion, parce que des personnes non informées interpretent mal le comportement de la personne handicapée. C'est le cas plus particulièrement lors d'interactions sociales, avec des amis ou au travail. Sans le contexte du handicap, ils est facile de penser qu'un comportement reflète une rudesse, de l'incompétence ou un trouble mental.

    Cela a été le cas pour moi. Depuis maintenant un certain temps, je souffre de problèmes digestifs. Cette page vise à donner du contexte sur le sujet, pour éviter des incompréhensions et confusions.

    Il y a 2 autres raisons pour lesquelles je me suis décidé à écrire ce document. D'abord, c'est un moyen pour moi de réduire la pression psychologique que j'associe avec mon état de santé. Si d'avantage de personnes dans mon entourage en sont informés et acceptent que c'est un problème de santé légitime, je peux considérer mes symptomes comme un véritable problème de santé, sans avoir besoin de les cacher. Ensuite, je pense que ce dont je souffre est plus répandu que l'on pourrait penser. Il est même possible que vous, lecteur, connaissiez une personne qui souffre de problèmes similaires. Si c'est le cas, j'éspère que ce document peut être un point de départ pour aider cette personne.

    # Symptômes (ça craint)

    Un docteur dirait de mon cas que « Je souffre d'un inconfort dans l'abdomen supérieur, avec des ballonements sévères et un transit ralenti ».

    Et bien que valide, ce diagnostic ne vous aide pas forcément à comprendre comment cela se traduit en expérience sensible. Et pour comprendre les difficultés que je dois affronter, cette compréhension subjective est selon moi indispensable.

    1. **inconfort abdominal**. Imaginez la sensation présente lorsque vous mangez beaucoup (vraiment beaucoup) en trop peu de temps. Au bout d'une heure environ, c'est légèrement douloureux, cela peut géner certains mouvements, et c'est surtout désagréable, comme une gène qui reste en arrière-plan. Impossible de situer une douleur: c'est une sensation le plus souvent diffuse. C'est cela, l'inconfort abdominal que je subis. À la différence près que la sensation peut durer toute la journée, peut m'empécher de dormir, et que le corps essaie de compenser en modifiant sa posture, ce qui créée des tensions et même un mal de dos.

    2. **Ballonements sévères**: C'est la cause de l'inconfort. Mes intestins retiennent plus de nourriture, d'eau et de gaz, ce qui augmente la pression interne. Mon abdomen est gonflé en permanence.

    3. **transit ralenti**: Parfois, je ne peux pas aller aux toilettes. Ma digestion est plus lente que la moyenne, tout simplement

    4. **chronique**: Les symptômes décrits ne sont pas constants, encore heureux. Cependant, je vis avec depuis très longtemps, probablement depuis 2023 (il y a 3 ans). Les symptômes apparaissent en phases plus ou moins sévères (crises), qui peuvent durer de quelques jours à plusieurs semaines. Cela a un impact psychologique très fort, car pendant longtemps je n'ai pas pu prévoir quand sera la prochaine crise et combien de temps elle durera. C'est moins le cas aujourd'hui (j'y reviendrais).


    Et comme vous pouvez vous en douter, ces symptômes ont un impact très fort sur différents aspects de ma vie. La première conséquence, et la plus handicapante, est la difficulté de se concentrer. Mon cerveau semble diriger toute son attention vers la sensation d'inconfort, et après plusieurs années je n'ai pas l'impression de progresser sur le sujet. Travailler, apprendre, et même jouer à des jeux devient plus difficile. Ensuite, il y a l'humeur générale. Après plusieurs jours d'inconfort, de frustration de de pas pouvoir manger à ma faim et de ne pas arriver à me concentrer, je suis très morose. Les dernières conséquences sont plus annexes, mais pas négligeables: difficulté à dormir, performances sportives décevantes. Je suis resté en sous-poids pendant 2 ans, sans que cela soit une décision délibérée.

    Je ne veux surtout pas créer de la pitié avec cette description. Je veux donner la description la plus précise possible, pour que mon lecteur ai le contexte nécessaire à comprendre mon comportement.

    # Déclencheurs, solutions (et non-solutions)

    Après tout ce temps d'accomodation de mes symptômes et d'investigations, je commence à avoir des pistes sur ce qui peut soulager mes symptômes, et ce qui les empire. Cela reste des pistes: ce ne sont ni des certitudes (je comprend assez peu mes symptômes, voir la section suivante), ni des solutions (difficile à garder sur le long terme).

    Commençons avec les déclencheurs

    ## Impact négatif

    De loin, le paramètre qui a le plus d'impact est mon alimentation.

    Si certains repas provoquent des symptômes à cause de l'équilibre de mon repas (trop de féculents, pas assez de fibres), la plupart des phases de crise sont provoquées par des aliments particuliers.

    Par exemple: lentilles, oignons, blé en grande quantité, lactose ...

    Les aliments que je ne supporte pas correspondent approximativement à la liste des "[FODMAPS](https://fr.wikipedia.org/wiki/FODMAP)". Ce sont les aliments qui contiennent des sucres, comme le Galactose ou les Fructanes, qui ne peuvent pas être digérés dans l'intestin. Je ne réagis pas automatiquement à ces ingrédients. Parfois je les supporte, mais dans les phases de crises, j'y réagis (au bout de 12 - 24h).

    > J'ai indiqué en annexes plus de détails sur les aliments.

    Le stress peut également être un déclencheur, mais de manière bien moins importante.


    ## Impact neutre

    On m'a conseillé de nombreux traitements / habitudes qui n'ont presque aucun impact. Parmi elles:
    - les exercices de relaxation (peuvent m'aider à me détendre mais n'ont aucun impact sur ma digestion)
    - des antispasmodiques
    - boire plus, boire moins, boire différemment
    - mastiquer davantage
    - faire plus de sport (cela peut aider, mais impact très marginal)

    ## Impact positif

    De loin, la solution la plus efficace est de contrôler ce que je mets dans mon assiette, de manière stricte.

    Les quelques autres astuces qui fonctionnent (les améliorations restent marginales):
    - appliquer une bouillote sur l'abdomen
    - des longues séances de marche
    - les probiotiques (des bactéries spécifiquement cultivées, en pillules)


    # Diagnostic et thérories

    Comme je l'ai mentionné plus haut, je n'ai toujours pas de bonne explication de ma condition médicale.

    Il reste beaucoup d'incertitudes scientifiques sur l'intestin, si bien que la plupart des médecins et spécialistes donnent par défaut un diagnostic très générique:

    *Le sydrôme de l'intestin irritable*

    Et la plupart des traitements et des solutions que l'on m'a proposé ont été inefficaces.

    J'ai tout de même progressé, petit à petit. Je sais que:
    - ce n'est pas une allergie (aucun symptôme rapide)
    - ce n'est pas juste une intolérance. En éliminant tous les ingrédients un par un, pas d'amélioration claire. Les symptômes ont toujours été associés à des grands groupes d'aliments.
    - ce n'est pas une intolérance au gluten (test négatif et régime sans gluten infructueux)
    - ce n'est pas psychologique. Je réagis parfois à la nourriture seule, sans problème de moral

    La théorie que je trouve la plus probable aujourd'hui, est issue de recherches relativement récentes (10 dernières années) et n'est pas du tout connue et acceptée par la comunauté médicale française. Pourtant, je pense qu'il y a 25% de chances qu'elle soit complètement correcte, et 80% de chance que la majeure partie soit correcte. La voici.

    > Suite à une intoxication alimentaire (vomissements intenses, gastro), j'ai été exposé à une polupation de bactéries qui produit une toxine appelée [Cdt-B](https://en.wikipedia.org/wiki/Cytolethal_distending_toxin). Mon système immunitaire a réagit en créant des anticorps spécifiques. Cependant, une protéine présente dans les parois cellulaires, la [vinculine](https://en.wikipedia.org/wiki/Vinculin), a un profil moléculaire très proche. Certains de ces anticorps peuvent réagir avec la vinculine, et par un processus de séléction, ils deviennent bientôt majoritaires. C'est une réaction auto-immune: mon système immunitaire réagit en attaquant un élément interne. Cette réaction auto-immune continue pendant des mois, potentiellement des années. Ce phénomène n'a pas beaucoup d'impact dans le reste du corps, mais détruit certaines cellules dans l'intestin: des cellules de Cajal et une partie du plexus myenteric. En conséquence, le mécanisme permettant le bon fonctionnement de mon petit intestin est altéré, ce qui cause un transit très lent. Enfin, ce transit très lent et peu efficace fait que des populations de bactéries (et autres microbes) s'installent dans mon intestin grêle, se nourrissant des sucres non digestibles (les fameux FODMAPs présents dans lentilles, choux et blé), créant des gaz et ralentissant d'autant plus mon transit.
    > Cette intoxication alimentaire a pu avoir lieu plusieurs fois, redéclenchant tout le processus avec des effets plus forts.

    > On parle de [Post-infectious IBS](https://aboutibs.org/what-is-ibs/post-infectious-ibs/). Sources principales:
    > - [Tracking Anti‑cytolethal Distending Toxin B and Anti‑vinculin Over
    Time and Their Roles in Symptoms](https://pmc.ncbi.nlm.nih.gov/articles/PMC12185622/pdf/10620_2025_Article_9068.pdf)
    > - [Autoimmunity Links Vinculin to the Pathophysiology of Chronic
    Functional Bowel Changes Following Campylobacter jejuni
    Infection in a Rat Model](assets/sibo_vinculin_rat.pdf)


    Pour être honnête, il y a toujours des choses que je peux pas expliquer. Pourquoi est-ce que les phases les plus terribles étaient une fois il y a 2 ans, et une autre il y a quelques mois ? Pourquoi je ne peux aujourd'hui plus consommer de lentilles et de pain, alors que j'en ai mangé pendant une semaine lors d'une randonnée dans les Alpes ? Mystère

    # Prochaines étapes

    J'aimerais beaucoup effectuer des tests pour confirmer ou infirmer la théorie ci-dessus. Malheuresement, il n'y a presque aucun test de ce genre en France, il est possible de se procurer des kits des États-Unis, mais ils coutent cher.

    Le traitement est également sous-développé en France.

    Le prochain mois, j'envisage de suivre un régime antibiotique assez strict, basé sur des plantes antibiotiques accessibles dans des herboristeries. Il est probable que cela s'accompagne d'une amélioration notable, même provisoire.

    Si cela ne fonctionne pas, j'essaieraie d'autres traitements, comme des prokinetiques (qui stimulent la digestion) ou des régimes spécifiques encore plus strics (mais provisoires, ils durent au maximum 2 semaines).

    Si cela ne fonctionne toujours pas, j'ai l'intetion d'effectuer une fibroscopie pour comprendre mieux ce qui se passe à l'interieur de mes intestins.

    Et si toutes ces pistes échouent, je ferais en sorte de consolider mon régime actuel, pour garder une bonne nutrition tout en évitant ce qui me cause des symptômes.

    Dans tous les cas, j'ai l'intention d'écrire un blog sur le média [LessWrong](https://www.lesswrong.com/) pour expliquer les erreurs à ne pas faire lorsque on cherche à résoudre ses problèmes digestifs.

    # Conclusion

    Si vous avez eu le courage de lire jusqu'ici, vous avez probablement une meilleure idée de ce avec quoi j'ai du composer pendant ces dernières années, et potentiellement dans le futur. Merci.

    Malgré le ton de cet article, je suis plutôt optimiste sur la suite. N'hésitez pas à évoquer le sujet dans la "vraie" vie, cela ne pourra que me faire du bien.

    Je vous souhaite une bonne journée (et autant que possible, la santé).
    """)

    return (fr,)


@app.cell
def _(lang_selector):
    lang_selector
    return


@app.cell(hide_code=True)
def _(en, fr, multilang):
    multilang(en, fr)
    return


@app.cell(hide_code=True)
def _(mo, multilang):
    multilang(
        mo.md("""
    # Annexes: diet
    """),
        mo.md("""
    # Annexes: alimentation
    """),
    )
    return


if __name__ == "__main__":
    app.run()
