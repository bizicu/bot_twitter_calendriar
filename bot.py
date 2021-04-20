import datetime
from datetime import date
from jours_feries_france import JoursFeries
import tweepy


consumer_key =""
consumer_secret_key =""
access_token =""
access_token_secret = ""
auth=tweepy.OAuthHandler(consumer_key,consumer_secret_key)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

date_du_jour = datetime.date.today()
year = date_du_jour.year
zone = 'Métropole'

# fonction pour savoir si il y a un jour ferie dans le mois 
# renvoie le nombre de jour restants et le nom de l'évenement
#ou si il a été passer et revoi le nombre de jour depuis qu'il est passer
def ferie_months(str=0):
    k=0
    res = JoursFeries.for_year(year)
    for clef,valeur in res.items():
        if date_du_jour.month == valeur.month:
            d= valeur - date_du_jour
            if d.days < 0: #pour savoir si il a ete passer
                k = d.days*-1 #pour mettre la valeur en positif
                return print(clef, "a été passer depuis plus de", k ,"jours")
            else:
                print(clef, "arrive dans", z,"jours")

def jours_ferie_proche(str=0):
    z=0
    index=0
    res = JoursFeries.for_year(year)
    for clef,valeur in res.items():
        if date_du_jour.month <= valeur.month: #pour savoir si c est dans le mois sinon c la galere
            if date_du_jour.month == valeur.month:
                z = valeur.day - date_du_jour.day
                if z < 0:
                    pass
                else: #la fonction donne le nombre de jours restant avant le prochain
                    d= valeur - date_du_jour
                    return print(clef,"dans", d.days,"jours")
            else:
                d= valeur - date_du_jour
                return clef ,  d.days

def tweeteer(srt=0):
    tee= pour_le_tweet=jours_ferie_proche()
    fo="Le prochain jour ferié est le", tee[0] ,"qui sera dans",tee[1],"jours"
    tweet = api.update_status(fo)