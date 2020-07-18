import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print(client.guilds);


#welcome message handling
@client.event
async def on_member_update(before, after):
    if len(before.roles) < len(after.roles):
        new_role = next(role for role in after.roles if role not in before.roles)
        print(new_role);
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
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('>roles'):
        embed = discord.Embed(title="Identity Roles", color=0xfe817f)
        embed.add_field(name="React to this message to add roles", value="\U0001F1E6 <@&699897962431512658>\n\U0001F1E7 <@&699897995600068608>\n\U0001F1E8 <@&699898033013260308>\n\U0001F1E9 <@&699898067859538011>\n\U0001F1EA <@&699898104333205564>\n\U0001F1EB <@&699898136818090084>\n\U0001F1EC <@&699898190178287637>\n\nIf any roles are missing, ping a <@&699812268145115137> and they'll assign them for you", inline=False)
        await message.channel.send(embed=embed)
        time.sleep(0.5)
        embed = discord.Embed(title="Orientation Roles", color=0xffc86e)
        embed.add_field(name="React to this message to add roles", value="\U0001F1E6 <@&699889869845168198>\n\U0001F1E7 <@&699889907212222535>\n\U0001F1E8 <@&699889940787494983>\n\U0001F1E9 <@&699889980067151882>\n\U0001F1EA <@&699890018658811964>\n\U0001F1EB <@&699890085969264680>\n\U0001F1EC <@&699890061025738752>\n\U0001F1ED <@&699890443718230016>\n\U0001F1EE <@&699890469810995260>\n\U0001F1EF <@&699890503944241202>\n\U0001F1F0 <@&699890541071958036>\n\U0001F1F1 <@&699890607317057590>\n\U0001F1F2 <@&699890646877601823>\n\U0001F1F3 <@&699890683066056744>\n\U0001F1F4 <@&712744400169730100>\n\U0001F1F5 <@&721393433276710961>\n\nIf your orientation(s) aren't listed, ping a <@&699812268145115137> and they'll assign them for you", inline=False)
        await message.channel.send(embed=embed)
        time.sleep(0.5)
        embed = discord.Embed(title="Gender Identity Roles", color=0xffff61)
        embed.add_field(name="React to this message to add roles", value="\U0001F1E6 <@&699885677256507402>\n\U0001F1E7 <@&699885751239835679>\n\U0001F1E8 <@&699885789042966558>\n\U0001F1E9 <@&699885851366391868>\n\U0001F1EA <@&699885897264398366>\n\U0001F1EB <@&699885931439849473>\n\U0001F1EC <@&699886147811147786>\n\U0001F1ED <@&699886187548246057>\n\U0001F1EE <@&699886232691408976>\n\U0001F1EF <@&699886265587335168>\n\nIf your gender(s) aren't listed, ping a <@&699812268145115137> and they'll assign them for you", inline=False)
        await message.channel.send(embed=embed)
        time.sleep(0.5)
        embed = discord.Embed(title="Pronoun Roles", color=0x7cfb88)
        embed.add_field(name="React to this message to add roles", value="\U0001F1E6 <@&699878300842983525>\n\U0001F1E7 <@&699878594280816641>\n\U0001F1E8 <@&699878350583365714>\n\U0001F1E9 <@&699880196706140190>\n\U0001F1EA <@&699878641500291072>\n\U0001F1EB <@&699878743463952474>\n\U0001F1EC <@&699878808546705468>\n\U0001F1ED <@&699878835457359934>\n\U0001F1EE <@&699878930999541780>\n\U0001F1EF <@&699878974033231912>\n\U0001F1F0 <@&700133237216772196>\n\U0001F1F1 <@&709408864012992553>\n\U0001F1F2 <@&700131772469477436>\n\nIf your pronouns aren't listed, ping a <@&699812268145115137> and they'll assign them for you", inline=False)
        await message.channel.send(embed=embed)
        time.sleep(0.5)
        embed = discord.Embed(title="Colour Roles", color=0x74b2ff)
        embed.add_field(name="React to this message to add roles", value="\U0001F1E6 <@&699844873439805441>\n\U0001F1E7 <@&699844894960648222>\n\U0001F1E8 <@&699844915479445624>\n\U0001F1E9 <@&699844922261635123>\n\U0001F1EA <@&699845102473969755>\n\U0001F1EB <@&699845122891841587>\n\U0001F1EC <@&699845182991892570>\n\U0001F1ED <@&699845206312484995>\n\U0001F1EE <@&699847500517081128>\n\U0001F1EF <@&699848093960634418>\n\U0001F1F0 <@&699848846762704947>\n\U0001F1F1 <@&699849297717362698>\n\U0001F1F2 <@&699849584461086763>\n\U0001F1F3 <@&699850050427289620>\n\U0001F1F4 <@&699850191175548969>", inline=False)
        await message.channel.send(embed=embed)
        time.sleep(0.5)
        embed = discord.Embed(title="Misc Roles", color=0xdb7ffe)
        embed.add_field(name="React to this message to add roles", value="\U0001F1E6 <@&711239368504770600>\n\U0001F1E7 <@&711239278956642337>\n\U0001F1E8 <@&711239427158179930>\n\U0001F1E9 <@&733610027432149022>\n\nYou need to have been in the server for a few hours to assign the <@&733610027432149022> role", inline=False)
        await message.channel.send(embed=embed)



client.run(os.environ['BOT_TOKEN'])
