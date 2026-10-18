# selfbot_scheduler.py
# Runtime: Python 3.10+
# Deps: pip install discord.py-self

import discord
import asyncio

# ─── CONFIG ──────────────────────────────────────────────
USER_TOKEN   = "MTUwNzgzNjU3MTA3NDY5MTE4Mg.G87uHl.jxuJbgXZvvdwiz-Pi3tvY59VBbC5k3zaCcvZwM"   # Settings > Advanced > copy token
CHANNEL_ID   = 1548768202555658250       # right-click channel > Copy ID
COMMAND      = "/tview username:noahthdrmaps amount:15 length:20"     # whatever you want posted
INTERVAL_MIN = 32                       # minutes between posts
# ─────────────────────────────────────────────────────────

client = discord.Client()

async def scheduler():
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)
    guild   = channel.guild

    print(f"[+] Running. Every {INTERVAL_MIN}m")

    while not client.is_closed():
        try:
            # fetch all slash commands in the guild
            cmds = await guild.application_commands()

            # find tview
            cmd = discord.utils.get(cmds, name="tview")

            if cmd is None:
                print("[!] tview command not found in guild")
            else:
                await cmd(
                    channel,
                    username="noahthdrmaps",
                    amount=15,
                    length=20
                )
                print("[+] Invoked /tview")

        except Exception as e:
            print(f"[!] Error: {e}")

        await asyncio.sleep(INTERVAL_MIN * 60)

@client.event
async def on_ready():
    print(f"[+] Logged in as {client.user}")
    client.loop.create_task(scheduler())

client.run(USER_TOKEN)