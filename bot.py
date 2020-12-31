import discord
import os
import time
import csv
from datetime import datetime
intents = discord.Intents.default()
intents.members = True
intents.presences = True

Hailey = ["Moderator","Moderator Permissions","cutie","pink","she/her","Female","Pansexual","Transgender","DM's open","User"]
Erin = ["Moderator","Moderator Permissions","mango","they/them","she/her","Polyamorous","Non-Binary","Pansexual","Asexual","Panromantic","Queer","Lesbian","Plural","DM's open","User"]
Moderators =	{
  339541537690222612 : "Hailey",
  419217666549743637 : "Erin",
}

numbermotes = ["1️⃣ ","2️⃣ ","3️⃣ ","4️⃣ ","5️⃣ ","6️⃣ ","7️⃣ ","8️⃣ ","9️⃣ ","\U0001F51F"]
lettermotes = ["\U0001F1E6","\U0001F1E7","\U0001F1E8","\U0001F1E9","\U0001F1EA","\U0001F1EB","\U0001F1EC","\U0001F1ED","\U0001F1EE","\U0001F1EF","\U0001F1F0","\U0001F1F1","\U0001F1F2","\U0001F1F3","\U0001F1F4","\U0001F1F5","\U0001F1F6","\U0001F1F7","\U0001F1F8","\U0001F1F9","\U0001F1FA","\U0001F1FB","\U0001F1FC","\U0001F1FD","\U0001F1FE","\U0001F1FF"]


def date_difference(date1,date2):
    difference = date2 - date1
    dividers = [365,30,1,3600,60]
    strings = [" year{s}"," month{s}"," day{s}"," hour{s}"," minute{s}"]
    for x,y,z in zip(range(5),dividers,strings):
        if x >= 3: x = difference.seconds
        else: x = difference.days
        if x >= y:
            return str(round(x / y)) + z.format(s = "s" if round(x / y) > 1 else "")

def storage_reader(file):
    outputarray = []
    data = list(csv.reader(open(file, "r")))
    for x in range(len(data)):
            for y in range(len(data[x])):
                if x == 0:
                    outputarray.append([])
                nested_list = outputarray[y]
                nested_list.append(data[x][y])
    return outputarray

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print(client.guilds)


#welcome message handling
@client.event
async def on_member_update(before, after):
    if len(before.roles) < len(after.roles):
        new_role = next(role for role in after.roles if role not in before.roles)
        if new_role.id == 699814532327145590:
            member = after
            pfp = member.avatar_url
            embed=discord.Embed(title=member.name+" has joined!", color=0xf1c40f)
            embed.set_author(name="hello there!", icon_url="https://cdn.discordapp.com/emojis/395628346379206656.png")
            embed.set_thumbnail(url=pfp)
            n = str(len(new_role.members))
            n = int(n)
            ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])
            membercount = ordinal(n)
            embed.set_footer(text=str(member) + " is the " + str(membercount) + " member!")
            channel = client.get_channel(710294117959335947)
            await channel.send(embed=embed)

            
@client.event
async def on_member_join(member):
    await client.wait_until_ready()
    if member.id in Moderators:
        Mod = Moderators[member.id]
        await member.edit(nick=Mod)
        for i in eval(Mod):
            role = discord.utils.get(member.guild.roles, name=i)
            time.sleep(0.1)
            await discord.Member.add_roles(member, role)
    else:
        joinedDate = member.joined_at
        embed=discord.Embed(title="Welcome to Trans Creative!", description="To access the rest of the server, please follow the instructions below:", color=0xf1c40f)
        embed.set_author(name="Hello,"+member.name, icon_url="https://cdn.discordapp.com/emojis/395628346379206656.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/icons/696454936942215181/a_d6e6ce8869cbd20f83051542629f94c0.gif")
        embed.set_footer(icon_url=member.avatar_url, text= member.name+"#"+member.discriminator + f" - {date_difference(member.created_at,datetime.now())} old")
        embed.add_field(name="1️⃣  Read the bot message", value="The bot should have sent you a direct message.\nIf you didn't recieve a message, a moderator will be here to help soon!", inline=True)
        channel = client.get_channel(699814426869760119)
        await channel.send(embed=embed)
        
            


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.author.id in Moderators:
        if message.content.startswith('>roles'):
            embed = discord.Embed(title="Identity Roles", color=0xfe817f)
            embed.add_field(name="React to this message to add roles", value="\U0001F1E6 <@&699897962431512658>\n\U0001F1E7 <@&699897995600068608>\n\U0001F1E8 <@&699898033013260308>\n\U0001F1E9 <@&699898067859538011>\n\U0001F1EA <@&699898104333205564>\n\U0001F1EB <@&699898136818090084>\n\U0001F1EC <@&699898190178287637>\n\nIf any roles are missing, ping a <@&699812268145115137> and they'll assign them for you", inline=False)
            await message.channel.send(embed=embed)
            time.sleep(0.5)
            embed = discord.Embed(title="Orientation Roles", color=0xffc86e)
            embed.add_field(name="React to this message to add roles", value="\U0001F1E6 <@&699889869845168198>\n\U0001F1E7 <@&699889907212222535>\n\U0001F1E8 <@&699889940787494983>\n\U0001F1E9 <@&699889980067151882>\n\U0001F1EA <@&699890018658811964>\n\U0001F1EB <@&699890085969264680>\n\U0001F1EC <@&699890061025738752>\n\U0001F1ED <@&699890443718230016>\n\U0001F1EE <@&699890469810995260>\n\U0001F1EF <@&699890503944241202>\n\U0001F1F0 <@&699890541071958036>\n\U0001F1F1 <@&699890607317057590>\n\U0001F1F2 <@&699890646877601823>\n\U0001F1F3 <@&699890683066056744>\n\U0001F1F4 <@&712744400169730100>\n\U0001F1F5 <@&721393433276710961>\n\U0001F1F6 <@&734468187411710043>\nIf your orientation(s) aren't listed, ping a <@&699812268145115137> and they'll assign them for you", inline=False)
            await message.channel.send(embed=embed)
            time.sleep(1)
            embed = discord.Embed(title="Gender Identity Roles", color=0xffff61)
            embed.add_field(name="React to this message to add roles", value="\U0001F1E6 <@&699885677256507402>\n\U0001F1E7 <@&699885751239835679>\n\U0001F1E8 <@&699885789042966558>\n\U0001F1E9 <@&699885851366391868>\n\U0001F1EA <@&699885897264398366>\n\U0001F1EB <@&699885931439849473>\n\U0001F1EC <@&699886147811147786>\n\U0001F1ED <@&699886187548246057>\n\U0001F1EE <@&699886232691408976>\n\U0001F1EF <@&699886265587335168>\n\U0001F1F0 <@&766684553594667039>\n\U0001F1F1 <@&766971952719855618>\n\U0001F1F2 <@&766684282545504256>\n\U0001F1F3 <@&766684436582367322>\n\U0001F1F4 <@&768930342937165864>\n\U0001F1F5 <@&766685258879860777>\nIf your gender(s) aren't listed, ping a <@&699812268145115137> and they'll assign them for you", inline=False)
            await message.channel.send(embed=embed)
            time.sleep(1)
            embed = discord.Embed(title="Pronoun Roles", color=0x7cfb88)
            embed.add_field(name="React to this message to add roles", value="\U0001F1E6 <@&699878300842983525>\n\U0001F1E7 <@&699878594280816641>\n\U0001F1E8 <@&699878350583365714>\n\U0001F1E9 <@&699880196706140190>\n\U0001F1EA <@&699878641500291072>\n\U0001F1EB <@&699878743463952474>\n\U0001F1EC <@&699878808546705468>\n\U0001F1ED <@&699878835457359934>\n\U0001F1EE <@&699878930999541780>\n\U0001F1EF <@&699878974033231912>\n\U0001F1F0 <@&700133237216772196>\n\U0001F1F1 <@&709408864012992553>\n\U0001F1F2 <@&700131772469477436>\n\nIf your pronouns aren't listed, ping a <@&699812268145115137> and they'll assign them for you", inline=False)
            await message.channel.send(embed=embed)
            time.sleep(1)
            embed = discord.Embed(title="Colour Roles", color=0x74b2ff)
            embed.add_field(name="React to this message to add roles", value="\U0001F1E6 <@&699844873439805441>\n\U0001F1E7 <@&699844894960648222>\n\U0001F1E8 <@&699844915479445624>\n\U0001F1E9 <@&699844922261635123>\n\U0001F1EA <@&699845102473969755>\n\U0001F1EB <@&699845122891841587>\n\U0001F1EC <@&699845182991892570>\n\U0001F1ED <@&699845206312484995>\n\U0001F1EE <@&699847500517081128>\n\U0001F1EF <@&699848093960634418>\n\U0001F1F0 <@&699848846762704947>\n\U0001F1F1 <@&699849297717362698>\n\U0001F1F2 <@&699849584461086763>\n\U0001F1F3 <@&699850050427289620>\n\U0001F1F4 <@&699850191175548969>", inline=False)
            await message.channel.send(embed=embed)
            time.sleep(1)
            embed = discord.Embed(title="Misc Roles", color=0xdb7ffe)
            embed.add_field(name="React to this message to add roles", value="\U0001F1E6 <@&711239368504770600>\n\U0001F1E7 <@&711239278956642337>\n\U0001F1E8 <@&711239427158179930>\n\U0001F1E9 <@&733610027432149022>\n\U0001F1EA <@&762736076586352690>\n\U0001F1EB <@&734945400699617342>\n\U0001F1EC <@&768905152807567452>\n\nYou need to have been in the server for a few hours to assign the <@&733610027432149022> role", inline=False)

            await message.channel.send(embed=embed)
            

        if message.content.startswith('>rules'):
            embed = discord.Embed(title="Rules", color=0xf1c40f)
            x = 0
            rules = storage_reader("data/rules.csv")
            for i in rules[0]:
                embed.add_field(name=numbermotes[x] + rules[0][x], value=rules[1][x] + "\n\n", inline=False)
                x += 1
            await message.channel.send(embed=embed)
            time.sleep(1)
            embed = discord.Embed(title="Info", color=0xf1c40f)
            x = 0
            info = storage_reader("data/info.csv")
            for i in info[0]:
                embed.add_field(name=info[0][x], value=info[1][x] + "\n\n", inline=False)
                x += 1
            await message.channel.send(embed=embed)
            

        if message.content.startswith('>changelog'):
            embed = discord.Embed(title="Changelog", color=0xf1c40f)
            embed.add_field(name="1️⃣  New year: 2021", value="Updated year to 2021, I hope y'all have a better year and everyone is safe and happy, thank you for all making this server great c:", inline=False)
            await message.channel.send(embed=embed)

    if message.content.startswith('>spoiler'):
        try:
            x = message.content
            x  = x.split(">spoiler")[1]
            try:
                x = x.lstrip();
            except:
                pass
        except IndexError:
           x = "See User Message"
        y = "cw: " + x + "\nAuthor: " + message.author.name
        file = message.attachments[0]
        file.filename = f"SPOILER_{file.filename}"
        spoiler = await file.to_file()
        await message.delete()
        await message.channel.send(y,file=spoiler)

client.run(os.environ['BOT_TOKEN'])
