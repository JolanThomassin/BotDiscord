##################### Import #####################
import discord 
from discord.ext import commands 
import asyncio 
import random

### Youtube ###
import urllib.request
import re

######################################################################################################################################################

##################### Préfixe #####################
client = commands.Bot(command_prefix='+',help_command = None) 

##################### Lancement du bot #####################
@client.event 
async def on_ready() : 
    print('______________________________________________')
    print("[CDS] AnimeBot est en ligne (à nouveau).")
    print('______________________________________________')

##################### Page du +help #####################
@client.command(pass_context=True,name="help")
async def help(ctx):
	embed=discord.Embed(
		title="Page d'aide :",
		description="Vous trouverez ici toutes les commandes du bot !",
		color=0x8B0000
	)
	embed.add_field(
		inline=False,
		name="+hug @someone",
		value=">    Câline la personne que tu aimes ! 💞"
	)
	embed.add_field(
		inline=False,
		name="+hit @someone",
		value=">    Frappe la personne qui t'as énervé. 👊"
	)
	embed.add_field(
		inline=False,
		name="+kiss @someone",
		value=">    Rien de mieux qu'un baiser pour exprimer son amour ! ❤"
	)
	embed.add_field(
		inline=False,
		name="+lick @someone",
		value=">    Hmmm... délicieux. 👅"
	)
	embed.add_field(
		inline=False,
		name="+pat @someone",
		value=">    C'est... tout doux ! ✋"
	)
	embed.add_field(
		inline=False,
		name="+dismoi question",
		value=">    La boule de cristal vous répondra. 🔮 "
	)
	embed.add_field(
		inline=False,
		name="+roll nombre_de_dé nombre_de_face",
		value=">    Et là y a un énorme dragon qui vous fonce dessus ! Je fais mes jets de dégâts ! T'est mort ! T'est mort ! T'est mort ! AAAAAAAAAAAAAAAAH ! 🎲"
	)
	embed.add_field(
		inline=False,
		name="+répulsion",
		value=">    L'amour... 👁"
	)
	embed.add_field(
		inline=False,
		name="+youtube recherche",
		value=">    Les recherches YouTube c'est bien, mais flemme d'aller sur l'application 🎥"
	)

	await ctx.send(embed=embed)

##################### Fonction +hug #####################
@client.command(pass_context=True, name = "hug", aliases =["calin"])
async def hug(ctx,member : discord.Member):
	utilisateur = fonctionSeul(ctx, member)	

	if utilisateur == "Seul" :
		embed=discord.Embed(
			description="Désolé de te voir seul..." ,
			color=0x8B0000
		)
		gif = ("https://i.pinimg.com/originals/3b/f1/8f/3bf18f8244b321318bd4b137d5c620c8.gif") 
	else :
		embed=discord.Embed(
			description= "**" + utilisateur[1] + "**" + ", tu as reçus un calin de " + "**" + utilisateur[0] + "**",
			color=0x8B0000
		)
		gif = getHug()

	embed.set_image(url=gif)
	await ctx.send(embed=embed)

##################### Fonction +hit #####################
@client.command(pass_context=True, name = "hit", aliases =["frappe", "punch"])
async def hit(ctx,member : discord.Member):
	utilisateur = fonctionSeul(ctx, member)

	if utilisateur == "Seul" :
		embed=discord.Embed(
			description="Désolé de te voir seul..." ,
			color=0x8B0000
		)
		gif = ("https://i.pinimg.com/originals/3b/f1/8f/3bf18f8244b321318bd4b137d5c620c8.gif") 
	else :
		embed=discord.Embed(
			description= "**" + utilisateur[0] + "**" + " a décidé de frapper " + "**" + utilisateur[1] + "**",
			color=0x8B0000
		)
		gif = getHit()

	embed.set_image(url=gif)
	await ctx.send(embed=embed)

##################### Fonction +kiss #####################
@client.command(pass_context=True, name = "kiss", aliases =["embrasse", "bisous"])
async def kiss(ctx,member : discord.Member):
	utilisateur = fonctionSeul(ctx, member)

	if utilisateur == "Seul" :
		embed=discord.Embed(
			description="Désolé de te voir seul..." ,
			color=0x8B0000
		)
		gif = ("https://i.pinimg.com/originals/3b/f1/8f/3bf18f8244b321318bd4b137d5c620c8.gif") 
	else :
		embed=discord.Embed(
			description= "**" + utilisateur[0] + "**" + " embrase amoureusement " +  "**" + utilisateur[1] + "**",
			color=0x8B0000
		)
		gif = getKiss()

	embed.set_image(url=gif)
	await ctx.send(embed=embed)

##################### Fonction +lick #####################
@client.command(pass_context=True, name = "lick", aliases =["lèche", "leche"])
async def lick(ctx,member : discord.Member):
	utilisateur = fonctionSeul(ctx, member)

	if utilisateur == "Seul" :
		embed=discord.Embed(
			description="Désolé de te voir seul..." ,
			color=0x8B0000
		)
		gif = ("https://i.pinimg.com/originals/3b/f1/8f/3bf18f8244b321318bd4b137d5c620c8.gif") 
	else :
		embed=discord.Embed(
			description= "**" + utilisateur[1] + "**" + " a été léché par " + "**" + utilisateur[0] + "**",
			color=0x8B0000
		)
		gif = getLick()

	embed.set_image(url=gif)
	await ctx.send(embed=embed)

##################### Fonction +pat #####################
@client.command(pass_context=True, name = "pat", aliases =["caresse"])
async def pat(ctx, member:discord.Member):
	utilisateur = fonctionSeul(ctx, member)

	if utilisateur == "Seul" :
		embed=discord.Embed(
			description="Désolé de te voir seul..." ,
			color=0x8B0000
		)
		gif = ("https://i.pinimg.com/originals/3b/f1/8f/3bf18f8244b321318bd4b137d5c620c8.gif") 
	else :
		embed=discord.Embed(
		description= "**" + utilisateur[0] + "**" + " caresse " + "**" + utilisateur[1] + "**",
		color=0x8B0000
		)
		gif = getPat()

	embed.set_image(url=gif)
	await ctx.send(embed=embed)

##################### Fonction +dismoi #####################
@client.command(pass_context=True, name = "dismoi", aliases =["dm"])
async def dismoi(ctx):
	imageEtTexte = getDismoi()
	embed=discord.Embed(
	title= imageEtTexte[0], # Texte retourné de la fonction aléatoire
	color=0x8B0000
	)
	gif = imageEtTexte[1] # Image retourné de la fonction aléatoire

	embed.set_image(url=gif)
	await ctx.send(embed=embed)

##################### Fonction +Répulsion #####################
@client.command(pass_context=True, name = "répulsion")
async def répulsion(ctx):
	embed=discord.Embed(
		title="*L'amour engendre le sacrifice, qui lui-même engendre la haine... Et après la souffrance entre en jeu...*",
		description="Répulsion céleste !" ,
		color=0x8B0000
	)
	embed.set_image(url="https://thumbs.gfycat.com/DiscreteWellinformedGrouper-size_restricted.gif")
	await ctx.send(embed=embed)

##################### Fonction SEUL #####################
def fonctionSeul(envoyeur, receveur) :
	if str(envoyeur.message.author.id) == str(receveur.id) :
		return ("Seul")
	else :
		if str(envoyeur.message.author.nick) == "None" :
			envoyeur = str(envoyeur.message.author.name)
		else :
			envoyeur = str(envoyeur.message.author.nick)
		if str(receveur.nick) == "None" :
			receveur = str(receveur.name)
		else :
			receveur = receveur.nick
		return(str(envoyeur), str(receveur))

##################### Banque de Gif #####################
def getHug():
	banque = [
	"https://c.tenor.com/9e1aE_xBLCsAAAAC/anime-hug.gif",
	"https://i.imgur.com/r9aU2xv.gif?noredirect",
	"https://i.pinimg.com/originals/bb/84/1f/bb841fad2c0e549c38d8ae15f4ef1209.gif",
	"https://c.tenor.com/pcULC09CfkgAAAAC/hug-anime.gif",
	"https://thumbs.gfycat.com/BlueDecimalAardwolf-max-1mb.gif",
	"https://64.media.tumblr.com/988a4660509af669515a40fd2ee38ada/b6806f9e566d4b2e-1d/s1280x1920/e0827aed786d0eeed23689dc320940b108c4305a.gifv",
	"https://cutewallpaper.org/21/hugs-anime/Anime-hug-GIFs-Get-the-best-GIF-on-GIPHY.gif",
	"https://lh6.googleusercontent.com/proxy/rGVigru1Kivmm7xfWownzOeurzGiKjGVhVygLWDHD-pSryq9pMx_OLI-4CI9Gf_wYf0=s0-d",
	"https://data.whicdn.com/images/334153915/original.gif",
	"https://c.tenor.com/ah1gTzIiOT0AAAAd/anime-hug.gif"
	]
	aléatoire = random.randint(0, 9) 
	choix = banque[aléatoire]
	return choix

def getHit():
	banque = [
	"https://c.tenor.com/VrWzG0RWmRQAAAAC/anime-punch.gif",
	"https://c.tenor.com/xJyw7SRtDRoAAAAC/anime-punch.gif",
	"https://media2.giphy.com/media/arbHBoiUWUgmc/200.gif",
	"https://i.pinimg.com/originals/8d/50/60/8d50607e59db86b5afcc21304194ba57.gif",
	"https://i.pinimg.com/originals/66/76/7a/66767af902113b20978f5880593b29af.gif",
	"https://c.tenor.com/HsnuQ0vN1s8AAAAC/naruto-sasuke.gif",
	"https://i.imgur.com/hGuGQcA.gif",
	"https://c.tenor.com/1JDwbOVIDjwAAAAd/fire-force-benimaru.gif",
	"https://c.tenor.com/1T5bgBYtMgUAAAAC/head-hit-anime.gif",
	"https://c.tenor.com/vbu26BjT938AAAAC/rocklee-attack.gif",
	"https://c.tenor.com/2l13s2uQ6GkAAAAC/kick.gif",
	"https://c.tenor.com/PrIvkVyaAacAAAAC/the-god-of-highschool-anime.gif",
	"https://c.tenor.com/kvxt9X-gXqQAAAAC/anime-clannad.gif",
	"https://c.tenor.com/aDZHwZaw9t4AAAAC/anime-kick.gif"
	]
	aléatoire = random.randint(0, 13) 
	choix = banque[aléatoire]
	return choix

def getKiss():
	banque = [
	"https://c.tenor.com/wDYWzpOTKgQAAAAC/anime-kiss.gif",
	"https://aniyuki.com/wp-content/uploads/2021/07/aniyuki-anime-gif-kiss-27.gif",
	"https://acegif.com/wp-content/uploads/anime-kissin-15.gif",
	"https://64.media.tumblr.com/e32206d2d51424eeb3c017c1ef0e80ad/fbe2f7e1b2143d0b-6a/s500x750/0280bd77e01a03bac8994f7a3c1aafa267abad0a.gifv",
	"https://giffiles.alphacoders.com/188/188348.gif",
	"https://data.whicdn.com/images/200294594/original.gif",
	"https://media1.giphy.com/media/ZRSGWtBJG4Tza/giphy.gif",
	"https://i.kym-cdn.com/photos/images/newsfeed/001/372/173/dea.gif",
	"https://img.wattpad.com/65c04624976b0581464a819d0e28820fa3efd016/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f41562d55397a51746b48506d47513d3d2d33352e313533393062613965373639343039313731373933313537303735302e676966",
	"https://64.media.tumblr.com/53f25ab73acf07734ee43d4139027ea8/546adb9317fafdd9-64/s540x810/051063944dc8165d5bd15044287752c53662432e.gifv"
	]
	aléatoire = random.randint(0, 9) 
	choix = banque[aléatoire]
	return choix

def getLick():
	banque = [
	"https://c.tenor.com/jyv9sexi1fYAAAAC/anime-lick.gif",
	"https://i.pinimg.com/originals/56/42/0d/56420de595681d55e4ea2cc9dcc48db9.gif",
	"https://c.tenor.com/bgGMTIJhEvEAAAAC/anime-lick-lick.gif",
	"https://c.tenor.com/g1HYBQGPEVYAAAAC/anime-lick.gif",
	"https://c.tenor.com/S5I9g4dPRn4AAAAC/omamori-himari-manga.gif",
	"https://c.tenor.com/Go7wnhOWjSkAAAAC/anime-lick-face.gif",
	"https://c.tenor.com/Eny2Z4-8rGkAAAAd/bruno-bucciarati-giorno-giovanna.gif",
	"https://c.tenor.com/NaL5lsLX1-cAAAAC/anime-lick.gif",
	"https://c.tenor.com/OlzH7_NG640AAAAC/anime-girl.gif",
	"https://c.tenor.com/cPPGnJqYiJYAAAAC/kanna-kamui.gif"
	]
	aléatoire = random.randint(0, 9) 
	choix = banque[aléatoire]
	return choix

def getPat():
	banque = [
	"https://c.tenor.com/E6fMkQRZBdIAAAAC/kanna-kamui-pat.gif",
	"https://c.tenor.com/rZRQ6gSf128AAAAC/anime-good-girl.gif",
	"https://c.tenor.com/6dLDH0npv6IAAAAC/nogamenolife-shiro.gif",
	"https://c.tenor.com/wLqFGYigJuIAAAAC/mai-sakurajima.gif",
	"https://c.tenor.com/tYS5DBIos-UAAAAd/kyo-ani-musaigen.gif",
	"https://c.tenor.com/TDqVQaQWcFMAAAAC/anime-pat.gif",
	"https://c.tenor.com/0mdj-zud0RAAAAAC/tohru-kobayashi.gif",
	"https://c.tenor.com/muVzMQS6mW0AAAAC/pat-anime.gif",
	"https://c.tenor.com/OTqETZ7YjaMAAAAC/anime-anime-couple.gif",
	"https://c.tenor.com/S3pfBHXIDYQAAAAC/ijiranaide-nagatoro-anime-pat.gif"
	]
	aléatoire = random.randint(0, 9) 
	choix = banque[aléatoire]
	return choix

def getDismoi():
	banque = [
	"https://c.tenor.com/1i61l5MoH8sAAAAM/no-nope.gif",
	"https://i.gifer.com/TOfD.gif"
	]
	texte = [
	"C'est un non",
	"C'est un oui"
	]
	aléatoire = random.randint(0, 1) 
	return (texte[aléatoire], banque[aléatoire])

##################### Fonction Roll #####################
@client.command(pass_context=True, name = "roll")
async def roll(ctx, nbrDé:int, nbrFace:int):

	resultat = 0
	for i in range(0, nbrDé) :
		lancer = random.randint(1, nbrFace)
		resultat = resultat + lancer

	embed=discord.Embed(
		title = f"Tirage de `{nbrDé}` dé(s), dé de `{nbrFace}` face(s)",
		description = f"Résultat du/des lancer(s) : `{resultat}` ! ",
		color = 0x8B0000
	)
	embed.set_author(name = ctx.message.author.name, url = "https://crdev.xyz/",icon_url = ctx.message.author.avatar_url) 
	await ctx.send(embed=embed) 

##################### Fonction +Youtube #####################
@client.command(pass_context=True, name = "youtube", aliases =["ytb"])
async def youtube(ctx, *args):
	tousMots = ""
	for i in range(0, len(args)) :
		tousMots = tousMots + "+" + args[i]

	lienRechercheVideo = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + tousMots)
	lienVideo = re.findall(r"watch\?v=(\S{11})", lienRechercheVideo.read().decode())
	résultat = "https://www.youtube.com/watch?v=" + lienVideo[0]

	embed=discord.Embed(
		title="Voici le résultat de votre recherche : ",
		description= résultat,
		color=0x8B0000
	)
	embed.set_author(name = ctx.message.author.name, url = "https://crdev.xyz/",icon_url = ctx.message.author.avatar_url) 
	await ctx.send(embed=embed) 


######################################################################################################################################################
client.run("Token")


