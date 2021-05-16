from discord.ext import commands
import discord
import tweepy
from keys import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

imp = 558800844343214090

class Twitter(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def tweet(self, ctx, *, tweet):
    if ctx.author.id == imp:
      api.update_status(tweet)
      tweet = api.user_timeline(
        user_id=1278923464808767493,
        count=1
      )
      await ctx.send(F"Tweet Sent! https://twitter.com/ImpassiveMoon/status/{tweet[0].__dict__['id']}")
    else:
      await ctx.send('You cannot tweet from this account!')

  @commands.command()
  async def name(self, ctx, *, name):
    if ctx.author.id == imp:
      if name is None:
        return await ctx.send('No!')
      api.update_profile(name=name)
      await ctx.send('Name Updated!')
    else:
      await ctx.send('You do not have access to this account!')

  @commands.command()
  async def description(self, ctx, *, description):
    if ctx.author.id == imp:
      api.update_profile(description=description)
      await ctx.send('Profile Description Updated!')
    else:
      await ctx.send('You do not have access to this account!')
  
  @commands.command()
  async def dms(self, ctx):
    dms = api.list_direct_messages()
    dms.reverse()
    
    for i in dms:
      if i.__dict__['message_create']['sender_id'] == '1278923464808767493':
        print('irrelevant')
      else:
        embed = discord.Embed(
          title = F"DM From {api.get_user(user_id = i.__dict__['message_create']['sender_id']).screen_name}",
          colour = 0x00acee,
          description = i.__dict__['message_create']['message_data']['text']
        )
        await ctx.send(embed=embed)


  @commands.command()
  async def rates(self, ctx):
    limit = api.rate_limit_status()
    for i in limit['resources'].keys():
      if i != 'rate_limit_context':
        for f in limit['resources'][i].keys():
          if limit['resources'][i][f]['limit'] > limit['resources'][i][f]['remaining']:
            embed = discord.Embed(
              title = f,
              colour = 0x00acee,
              description = F"Limit - {limit['resources'][i][f]['limit']}\nRemaining - {limit['resources'][i][f]['remaining']}"
            )
            await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Twitter(client))