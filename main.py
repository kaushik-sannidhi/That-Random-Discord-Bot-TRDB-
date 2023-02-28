import os
import random
import discord
from keep_alive import keep_alive
from discord.ext import commands
import requests

client = commands.Bot(command_prefix = "trdb ")
client.remove_command('help')
selfBot = False
if(selfBot):
  TOKEN = ""
else:
  TOKEN = ""
@client.event
async def on_ready():
    print('We have logged in ')
    print("------------------------")

@client.group(invoke_without_command = True)
async def help(ctx):
  if(selfBot):
    await ctx.send("Help menu: \n"+
                  "Joke: trdb help joke \n"+
                  "Fact: trdb help fact \n"+
                  "Mag8ball: trdb help mag8ball \n"+
                  "Bucketlist: trdb help bucketlist \n"+
                  "Name: trdb help name \n"+
                  "Riddle: trdb help riddle \n"+
                  "Meter: trdb help meter \n"+
                  "Chucknorris: trdb help chucknorris \n"+
                  "Dadjoke: trdb help dadjoke \n"+
                  "Hobbies: trdb help hobbies \n"+
                  "Trivia: trdb help trivia \n")
  else:
    em = discord.Embed(title="Help Menu", description="Use: trdb help to get the help menu")
    em.add_field(name="joke", value = "trdb help joke")
    em.add_field(name="fact", value = "trdb help fact")
    em.add_field(name="mag8ball", value = "trdb help mag8ball")
    em.add_field(name="bucketlist", value = "trdb help bucketlist")
    em.add_field(name="name", value = "trdb help name")
    em.add_field(name="riddle", value = "trdb help riddle")
    em.add_field(name="meter", value = "trdb help meter")
    em.add_field(name="chucknorris", value = "trdb help chucknorris")
    em.add_field(name="dadjoke", value = "trdb help dadjoke")
    em.add_field(name="hobbies", value = "trdb help hobbies")
    em.add_field(name="trivia", value = "trdb help trivia")
    await ctx.send(embed = em)

##help commands
@help.command()
async def joke(ctx):
  if(selfBot):
    await ctx.send("Joke: \n"+
                  "Description: Displays a Joke \n"+
                  "Syntax: trdb joke")
  else:
    em = discord.Embed(title="Joke", description="Displays a joke", inline=False)
    em.add_field(name = "**SYNTAX**", value = "trdb joke")
    await ctx.send(embed = em)
    

@help.command()
async def fact(ctx):
  if(selfBot):
    await ctx.send("Fact: \n"+
                  "Description: Displays a fun fact \n"+
                  "Syntax: trdb fact")
  else:
    em = discord.Embed(title="Fact", description="Displays a fun fact", inline=False)
    em.add_field(name = "**SYNTAX**", value = "trdb fact")
    await ctx.send(embed=em)

@help.command()
async def name(ctx):
  if(selfBot):
    await ctx.send("Name: \n"+
                "Description: Displays a random name \n"+
                "Syntax: trdb name")
  else:
    em = discord.Embed(title="Name", description="Displays a name", inline=False)
    em.add_field(name = "**SYNTAX**", value = "trdb name")
    await ctx.send(embed=em)

@help.command()
async def mag8ball(ctx):
  if(selfBot):
    await ctx.send("Mag8ball: \n"+
                  "Description: Displays a response from a magic 8 ball \n"+
                  "Syntax: trdb mag8ball")
  else:
    em = discord.Embed(title="Mag8ball", description="A magic 8 ball", inline=False)
    em.add_field(name = "**SYNTAX**", value = "trdb mag8ball Should I ....")
    await ctx.send(embed=em)

@help.command()
async def riddle(ctx):
  if(selfBot):
    await ctx.send("Riddle: \n"+
                "Description: Displays a riddle \n"+
                "Syntax: trdb riddle")
  else:
    em = discord.Embed(title="Riddle", description="Displays a riddle", inline=False)
    em.add_field(name = "**SYNTAX**", value = "trdb riddle")
    await ctx.send(embed=em)

@help.command()
async def meter(ctx):
  if(selfBot):
    await ctx.send("Meter: \n"+
                "Description: Displays a percentage \n"+
                "Syntax: trdb meter")
  else:
    em = discord.Embed(title="Meter", description="Displays a percentage", inline=False)
    em.add_field(name = "**SYNTAX**", value = "trdb meter how smart am I")
    await ctx.send(embed=em)

@help.command()
async def bucketlist(ctx):
  if(selfBot):
    await ctx.send("Bucketlist: \n"+
                "Description: Displays a thing to add to your bucket list \n"+
                "Syntax: trdb bucketlist")
  else:
    em = discord.Embed(title="Bucketlist", description="Displays an item you should add to your bucketlist", inline=False)
    em.add_field(name = "**SYNTAX**", value = "trdb bucketlist")
    await ctx.send(embed=em)
    
@help.command()
async def chucknorris(ctx):
  if(selfBot):
    await ctx.send("Chucknorris: \n"+
                "Description: Displays a chuck norris joke \n"+
                "Syntax: trdb chucknorris")
  else:
    em = discord.Embed(title="Chucknorris", description="Displays a chuck norris joke", inline=False)
    em.add_field(name = "**SYNTAX**", value = "trdb chucknorris")
    await ctx.send(embed=em)
    
@help.command()
async def dadjoke(ctx):
  if(selfBot):
    await ctx.send("Dadjoke: \n"+
                "Description: Displays a dad joke \n"+
                "Syntax: trdb dadjoke")
  else:
    em = discord.Embed(title="Chucknorris", description="Displays a chuck norris joke", inline=False)
    em.add_field(name = "**SYNTAX**", value = "trdb chucknorris")
    await ctx.send(embed=em)
    
@help.command()
async def hobbies(ctx):
  if(selfBot):  
    await ctx.send("Hobbies: \n"+
                  "Description: Displays a cool hobbie \n"+
                  "Syntax: trdb hobbies")
  else:
    em = discord.Embed(title="Hobbies", description="Displays a hobby", inline=False)
    em.add_field(name = "**SYNTAX**", value = "trdb hobbies")
    await ctx.send(embed=em)
    
@help.command()
async def trivia(ctx):
  if(selfBot):
    await ctx.send("Trivia: \n"+
                "Description: Displays a trivia question and answer \n"+
                "Syntax: trdb trivia")
  else:
    em = discord.Embed(title="Trivia", description="Displays a trivia", inline=False)
    em.add_field(name = "**SYNTAX**", value = "trdb trivia")
    await ctx.send(embed=em) 
    
#client commands

@client.command()
async def joke(ctx):
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        await ctx.send(f"Here's a joke for you:\n{data['setup']}\n{data['punchline']}")
    else:
        await ctx.send("Oops, something went wrong. Please try again later.")

@client.command()
async def riddle(ctx):
    api_url = 'https://api.api-ninjas.com/v1/riddles'
    response = requests.get(api_url, headers={'X-Api-Key': 'yrrwohytFsUz2YCFNqL2Hw==MxUiXJFgFM8j35Np'})
    if response.status_code == requests.codes.ok:
        await ctx.send("Q: "+response.json()[0]["question"]+"\n"+
                      "A: "+response.json()[0]["answer"])
    else:
        await ctx.send("Error:", response.status_code, response.text)
    

@client.command()
async def bucketlist(ctx):
    api_url = 'https://api.api-ninjas.com/v1/bucketlist'
    response = requests.get(api_url, headers={'X-Api-Key': 'yrrwohytFsUz2YCFNqL2Hw==MxUiXJFgFM8j35Np'})
    if response.status_code == requests.codes.ok:
        await ctx.send(response.json()["item"])
    else:
        await ctx.send("Error:", response.status_code, response.text)

@client.command()
async def name(ctx):
    api_url = 'https://api.api-ninjas.com/v1/babynames?gender=neutral'
    response = requests.get(api_url, headers={'X-Api-Key': 'yrrwohytFsUz2YCFNqL2Hw==MxUiXJFgFM8j35Np'})
    if response.status_code == requests.codes.ok:
        await ctx.send(response.json()[0])
    else:
        await ctx.send("Error:", response.status_code, response.text)

@client.command()
async def fact(ctx):
    api_url = 'https://api.api-ninjas.com/v1/facts?limit=1'
    response = requests.get(api_url, headers={'X-Api-Key': 'yrrwohytFsUz2YCFNqL2Hw==MxUiXJFgFM8j35Np'})
    if response.status_code == requests.codes.ok:
        await ctx.send(response.json()[0]["fact"])
    else:
        await ctx.send("Error:", response.status_code, response.text)
@client.command()
async def meme(ctx):
    api_url = 'https://meme-api.com/gimme/1'
    response = requests.get(api_url, headers={'X-Api-Key': 'yrrwohytFsUz2YCFNqL2Hw==MxUiXJFgFM8j35Np'})
    await ctx.send(response.json()["memes"][0]["url"])
@client.command()
async def meter(ctx):
    await ctx.send(str(random.randint(0,100))+"%")
    
@client.command()
async def mag8ball(ctx):
    answers = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "Outlook not so good.",
        "My sources say no.",
        "Very doubtful."
    ]
    await ctx.send(random.choice(answers))

@client.command()
async def chucknorris(ctx):
    api_url = 'https://api.api-ninjas.com/v1/chucknorris?'
    response = requests.get(api_url, headers={'X-Api-Key': 'yrrwohytFsUz2YCFNqL2Hw==MxUiXJFgFM8j35Np'})
    await ctx.send(response.json()["joke"])

@client.command()
async def dadjoke(ctx):
    api_url = 'https://api.api-ninjas.com/v1/dadjokes?limit=1'
    response = requests.get(api_url, headers={'X-Api-Key': 'yrrwohytFsUz2YCFNqL2Hw==MxUiXJFgFM8j35Np'})
    await ctx.send(response.json()[0]["joke"])

@client.command()
async def hobbies(ctx):
    api_url = 'https://api.api-ninjas.com/v1/hobbies?category=general'
    response = requests.get(api_url, headers={'X-Api-Key': 'yrrwohytFsUz2YCFNqL2Hw==MxUiXJFgFM8j35Np'})
    count = 0
    await ctx.send(response.json()["hobby"]+response.json()["link"])

@client.command()
async def trivia(ctx):
    api_url = 'https://api.api-ninjas.com/v1/trivia?category=general'
    response = requests.get(api_url, headers={'X-Api-Key': 'yrrwohytFsUz2YCFNqL2Hw==MxUiXJFgFM8j35Np'})
    await ctx.send(response.json()[0]["question"]+"\n"+response.json()[0]["answer"])
    
#client events to snipe edited and deleted messages

@client.event
async def on_message_delete(message):
    global snipe_message_content
    global snipe_message_author
    global snipe_message_id
    snipe_message_content = message.content
    snipe_message_author = message.author.id
    snipe_message_id = message.id
    if(snipe_message_author != 728263722598137989):
        await message.channel.send("sniped: " + "`" + snipe_message_content + "`" + "\nFrom: " +   f'<@!{snipe_message_author}>')
    
@client.event
async def on_message_edit(message_before, message_after):
    author = message_before.author.id
    channel = message_before.channel
    if(author != 728263722598137989):
      await channel.send(f"""Pre-edit: `{message_before.content}`\nPost-edit: `{message_after.content}`\nAuthor: <@!{message_before.author.id}>""")


#runs the bot 24/7 for free

keep_alive()
try:
  client.run(TOKEN, bot = not selfBot)
except:
  print("yeeted lmao, restarting")
  os.system("kill 1")
  os.system("python restarter.py")

