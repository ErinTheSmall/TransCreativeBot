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
            ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n/10%10!=1)*(n%10<4)*n%10::4])
            membercount = ordinal(n)
            embed.set_footer(text=str(member) + " is the " + str(membercount) + " member!")
            channel = client.get_channel(710294117959335947)
            await channel.send(embed=embed)





client.run(os.environ['BOT_TOKEN'])
