import discord
import responses

def run_discord_bot(message = None):
    TOKEN = 'MTE3NTA4Nzg0NDM4MTk1NDExOA.GCqN_y.VtHpAir7Vpm2pfqei8dc6cDErC5SRFPANKcY9o'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents = intents)

    @client.event
    async def on_ready():
        await client.wait_until_ready()
        print(f'{client.user} is now running!')
        if message:
            response = responses.handle_response(message)
            await client.get_channel(1175157430678737016).send(response)
        await client.close()

    client.run(TOKEN)

    