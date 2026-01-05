
import marimo
app = marimo.App(width="medium")
with app.setup(hide_code=True):
    import marimo as mo
    
    def page_():
        from here import Embed
        return Embed(__file__, globals()["app"], "# Vous reprendrez bien un peu de Noël ?", [])

    

@app.cell(hide_code=True)
def _():
    mo.md(rf"""
# Vous reprendrez bien un peu de Noël ?

> Since my mother language is French, and I do not master English enough to share the emotional content I would like to, I decided to switch for this one post. Just the once won't hurt, and today's theme is worth it.

Noël est fini, ça y est.

Le sapin, bien qu'encore présent dans le salon de la maison familiale, est bien sec. Il se meurt.

Je ne fais pas partie de ces gens qui attendent Noël et le réveillon avec impatience. Au contraire, je garde des souvenirs mitigés de la période de fin d'année. Comme si la remise à zéro du calendrier nous forçait à tout recommencer. Comme si le froid nous forçait à nous séparer de tout artifice et à perdre nos convictions, comme les arbres perdent leurs feuilles. Comme si la nouvelle année venait nous juger.

Mais si je n'attend pas les fêtes avec impatience, je les apprécie. Si quelque chose n'est pas une légende dans ce moment magique, c'est son atmosphere légendaire. Ce mélange d'émotions est bien réel lui, dans cette ambiance irréelle. Avec ma famille, ce moment de mise à nu est le plus honnête qui soit. Je pense que nous avons su conserver l'âme profonde de cette fête, qui chez certains n'a gardé que le superficiel. Autour du couvert, emmitouflés mais sans artifices, nous nous découvrons. Nous partageons le plus précieux: ce qui nous manque.

Tout est fini, disais-je. Une fois les fêtes passés, il faut retourner à la vraie (fausse) vie. Pour moi, cela signifie retour à Paris. Ville ou personne ne sait s'il est content, pour ne rien changer. Sans grande énergie, je retourne à Rosny. Le lendemain, les transports en commun. À 9h30, réu urgente, mais où on n'apprend rien. Tâche définie, projet infini, je travaille seul, en autonomie. De toute façon, personne ne vient au bureau: je me contente des visios. Un écran souss les yeux, je ne suis pas malheureux. Mais quand même, c'était bien sous le sapin !

Cela aurait pu être l'histoire de cette rentrée. Et pour ne rien vous cacher, je n'aurai pas écrit ce compte-rendu semi-déprimant pour partager autour de moi cette absence totale d'émotions. Mais voilà: à 16h frappantes, le ciel a frappé.

![neige_osp.jpg](../assets/neige_osp_1767635510523_0.jpg)

Le retour de la neige ! Ô neige, Ô tapis blanc qui recouvre tout ! Magie de Noël en poudre, que personne (sauf les stations de ski) ne peut commercialiser ! Ô pluie de bonheur qui cette année, avait attendu le  soir du 25 décembre pour se manifester: comme pour nous faire croire au père Noël encore un petit peu. Tu es revenue en gros flocons, et a tapissé le goudron sale de la capitale. Tu as choisi ta meilleure consistance, celle qui fait ce bruit impossible à décrire sous les chaussures et qui transforme une petite boule en bonhome de neige en moins de temps qu'il faut pour dire "luge". Oserais-je un émoticone dans ce récit plein de poésie ? Oui, et même deux: 💖❄️

Pourtant, Paris reste Paris. La RATP et la SNCF restent fidèles à eux-mêmes, comme s'ils avaient besoin de neige pour perturber leur propre traffic. Tout de même, je suis rentré avant la nuit, et ce genre de paysage m'attendait:

![image.png](../assets/image_1767633608034_0.png)

Rien de Laponique ni de Sibérien dans cette photographie, certes. Demain, il ne restera peut-être plus que verglas, flaques et RER supprimés. Mais pour moi, cette image restera le souvenir d'un esprit des fêtes qui est revenu pour demander: "Alors, qui reprendra un peu de Noël ?"

Oui, une petite part pour moi !

![image.png](../assets/image_1767633617931_0.png)
""")
