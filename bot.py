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
    index = 0
    k=0
    res = JoursFeries.for_year(year)
    for clef,valeur in res.items():
        if date_du_jour.month == valeur.month:
            d= valeur - date_du_jour
            if date_du_jour.month == 5: #car dans ce moit plusieur jour ferie 
                if d.days < 0:
                    index+=1
                    if index == 3:
                        return d.days , clef
                    pass
                if d.days >= 0:
                    return d.days , clef
            elif date_du_jour.month == 11:
                if d.days < 0:
                    index+=1
                    if index == 2:
                        return d.days , clef
                    pass
                if d.days >= 0:
                    return d.days , clef
            elif d.days < 0: #pour savoir si il a ete passer
                return d.days , clef  #ca ete passer
            else:
                return d.days , clef
    index = 87000
    return index
def jours_ferie_proche(str=0):
    z=0
    res = JoursFeries.for_year(year)
    for clef,valeur in res.items():
        if date_du_jour.month <= valeur.month: #pour savoir si c'est dans le mois
            if date_du_jour.month == valeur.month: 
                z = valeur.day - date_du_jour.day
                if z < 0: #vu qu'on voit si c'est dans le mois faut voir si sa n'est pas déjà passer 
                    pass
                else: #donne le nombre de jour restant avant le prochain jour ferié
                    d= valeur - date_du_jour
                    return clef, d.days
            else:
                d= valeur - date_du_jour
                return clef ,  d.days

def tweeteer(srt=0):
    if srt == 0 :
        tee = pour_le_tweet=jours_ferie_proche()
        a = str(tee[0])        
        z=str("Le prochain jour ferié est le " + tee[1] + " qui sera dans " + a + " jours")
        tweet = api.update_status(z)
    if srt ==  1:
        tee = ferie_months()
        if tee[0]< 0:
            fj = tee[0] *-1
            a = str(fj)
            z=str("Le jour ferie de ce mois ci est passe depuis plus de " + a+ " jours " + "c'était le "+tee[1])
            tweet = api.update_status(z)
        elif tee[0] == 87000:
            z=str("Il n'y a pas de jour ferie ce mois ci")
            tweet = api.update_status(z)
        else:
            a = str(tee[0])
            z=str("Il y a un jour ferie ce mois si et il est dans "+ a + "jours"+ "et c'est le "+ tee[1])
            tweet = api.update_status(z)


