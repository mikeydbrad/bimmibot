from discord.ext import commands
from discord.ui import Button, View
from datetime import datetime

import discord
import requests

currency = "\u20BD"
greaterorequal = '\u2265'

# uses https://tarkov.dev/api/
# practice queries here https://api.tarkov.dev/
# example bot on github https://github.com/Mateusz-Latka/Fence-Flea-Market-Keeper/blob/main/bot.py

def run_tarkov_dev_query(query):
  headers = {"Content-Type": "application/json"}
  response = requests.post('https://api.tarkov.dev/graphql', headers=headers, json={"query": query})
  return response.json()

def get_item_data(search):
  query = f""" 
  {{
      items(name: "{search}") {{
        shortName
        avg24hPrice
        iconLink
        wikiLink
        link
        types
        width
        height
        updated
      }}
  }}
  """
  
  try:
    result = run_tarkov_dev_query(query)
    items = result['data']['items']
    
    if not items:
      raise ValueError(f"Item '{search}' not found in the database.")

    item_data = items[0]
    return {
      'shortName': item_data['shortName'],
      'avg24hPrice': item_data['avg24hPrice'],
      'iconLink': item_data['iconLink'],
      'wikiLink': item_data['wikiLink'],
      'link': item_data['link'],
      'types': item_data['types'],
      'width': item_data['width'],
      'height': item_data['height'],
      'updated': item_data['updated']
    }
  except requests.exceptions.RequestException as e:
    raise Exception(f"Failed to connect to the Tarkov API: {e}")
  except (KeyError, IndexError):
    raise Exception("Failed to parse the API response.")

def get_tier(search):
    if search >= 40000:
        return ':star:Legendary'
    elif search >= 30000:
        return ':green_circle:Great'
    elif search >= 20000:
        return ':yellow_circle:Average'
    elif search >= 10000:
        return ':red_circle:Poor'
    else:
        return ':x:Trash'  

def get_color(search):
    if search >= 40000:
        return 0xFF8C00
    elif search >= 30000:
        return 0x00FF00
    elif search >= 20000:
        return 0xFFFF66
    elif search >= 10000:
        return 0xFF0000
    else:
        return 0x800000

class Tarkov(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def tarkov(self, ctx, arg):
    try:
      item_data = get_item_data(arg)
      item_name = item_data['shortName']
      print(item_name)
      item_price = item_data['avg24hPrice']
      item_icon = item_data['iconLink']
      item_wiki_link = item_data['wikiLink']
      item_dev_link = item_data['link']
      item_types = item_data['types']
      item_width = item_data['width']
      item_height = item_data['height']
      item_update = item_data['updated']

      # TODO fix date, format from API results in something like "2024-02-11T01:52:35.000Z"
      # date = datetime.fromisoformat(item_update)
      # formatted_date = date.strftime("%d %B %Y, %H:%M:%S")

      slots = item_width*item_height
      price_perslot = item_price//slots
      slots1 = "slots"
      format_price = format(item_price,',')
      format_priceperslot = format(price_perslot, ',')
      if slots == 1:
        slots1 = "slot"
      button_wiki = Button(label="Wiki", style=discord.ButtonStyle.green, url=item_wiki_link)
      button_dev = Button(label="Dev", style=discord.ButtonStyle.green, url=item_dev_link)
      view = View()
      view.add_item(button_wiki)
      view.add_item(button_dev)
      embed = discord.Embed(title=f"{item_name}", color=get_color(price_perslot))
      embed.set_thumbnail(url=item_icon)
      embed.add_field(name="Price:", value=f' > {format_price}{currency}\n > (lowest price)', inline=True)
      embed.add_field(name="Per Slot:", value=f' > {format_priceperslot}{currency}\n > ({slots} {slots1})', inline=True)
      embed.add_field(name="Tier:", value=get_tier(price_perslot), inline=False)
      # embed.add_field(name="Last update:", value=formatted_date, inline=False)
      embed.set_footer(text="Data povided by: https://tarkov.dev/api/")
      await ctx.send(embed=embed, view=view)
    except Exception as e:
      embed = discord.Embed(title="Error", description=str(e), color=0xFF0000)
      await ctx.send(embed=embed)

async def setup(bot):
  await bot.add_cog(Tarkov(bot))