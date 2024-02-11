from discord.ext import commands

import requests

def run_tarkov_dev_query(query):
  # headers = {"Content-Type": "application/json"}
  # response = requests.post('https://api.tarkov.dev/graphql', headers=headers, json={"query": query})
  # return response.json()

  response = requests.post('https://api.tarkov.dev/graphql', json={'query': query})
  response.raise_for_status()
  return response.json()

class Tarkov(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def tarkov(self, ctx, arg):
    name = arg
    query = f""" 
    {{
        items(name: "{name}") {{
          shortName
          avg24hPrice
          iconLink
          wikiLink
          link
          types
        }}
    }}
    """
    
    try:
      result = run_tarkov_dev_query(query)
      items = result['data']['items']
      
      if not items:
        raise ValueError(f"Item '{name}' not found in the database.")

      item_data = items[0]
      return {
        'shortName': item_data['shortName'],
        'avg24hPrice': item_data['avg24hPrice'],
        'iconLink': item_data['iconLink'],
        'wikiLink': item_data['wikiLink'],
        'link': item_data['link'],
        'types': item_data['types']
      }
    except requests.exceptions.RequestException as e:
      raise Exception(f"Failed to connect to the Tarkov API: {e}")
    except (KeyError, IndexError):
      raise Exception("Failed to parse the API response.")
      
    
    # try:
    #     result = run_tarkov_dev_query(query)
    #     items = result['data']['items']

    #     if not items:
    #         raise ValueError(f"Item '{name}' not found in the database.")

    #     item_data = items[0]
    #     return {
    #         'name': item_data['name'],
    #         'low24hPrice': item_data['low24hPrice'],
    #         'iconLink': item_data['iconLink'],
    #         'wikiLink': item_data['wikiLink'],
    #         'width': item_data['width'],
    #         'height': item_data['height'],
    #         'changeLast48hPercent': item_data['changeLast48hPercent'],
    #         'updated': item_data['updated']
    #     }
    # except requests.exceptions.RequestException as e:
    #     raise Exception(f"Failed to connect to the Tarkov API: {e}")
    # except (KeyError, IndexError):
    #     raise Exception("Failed to parse the API response.")
    

    await ctx.send(result)

async def setup(bot):
  await bot.add_cog(Tarkov(bot))