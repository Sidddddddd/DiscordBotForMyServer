import discord
import random


TOKEN = 'not giving'

client = discord.Client()

@client.event
async def on_ready():
	print('We have logged in as {0.user}' .format(client))


@client.event
async def on_message(message):
	username = str(message.author).split('%')[0]
	user_message = str(message.content)
	channel = str(message.channel.name)
	print(f'{username}: {user_message} ({channel})')


	if message.author == client.user:
		return 

	if message.channel.name == 'staff-cmds':
		command = user_message.lower()
		print(f'recieved command {command}')
		if command == '$help':
			print('Sending Help Thing')
			response = ('If you need the command list, please click this link: https://docs.google.com/document/d/1fmJwHwmkH2R7k0pNvYAaqXYN26LFZa_as8Axw7jaOVQ/edit?usp=sharing')
			await message.channel.send(response)
			return
		if command == '$randomnumber':
			print('Getting a randomnumber')
			response = f'This is your random number: {random.randrange(10000000000)}'
			await message.channel.send(response)
			return
		if command == '$poop':
			print('getting an img of poop')
			response = ('http://assets.stickpng.com/images/580b57fcd9996e24bc43c39c.png')
			await message.channel.send(response)
			return
		if command == '$rule1':
			print('getting rule1')
			response = ('**Rule 1 - No harassment, impersonation, hate speech, or toxic behaviour.Do not spread toxicity or bully other members. Racism, sexism, homophobia, and harassment will not be tolerated in DMs or in this server.**')
			await message.channel.send(response)
			return
		if command == '$rule2':
			print('getting rule2')
			response = ('**Rule 2 - Do not spam.Posting large copypastas or joining in with chains will be counted as spam. We do not allow epileptic/flashing content. Do not spam emojis and stickers. Playing loud noises and use voice changers in VCs is also prohibited.**')
			await message.channel.send(response)
			return
		if command == '$rule3':
			print('getting rule3')
			reponse = ('**Rule 3 - NSFW content, and suspicious activities.Do not post NSFW content such as nudity or gore, and do not engage in discussion about sexual or disturbing topics.**')
			await message.channel.send(response)
			return
		if command == '$rule4':
			print ('getting rule4')
			response = ('**Rule 4 - Religious and political discussions.Do not spread religious or political ideas no matter their intent. Being insensitive towards others and using religious words, phrases, or references as jokes is not allowed.**')
			await message.channel.send(response)
			return
		if command =='$rule5':
			print ('getting rule')
			response = ('**Rule 5 - Use appropriate channels and do not advertise.Do not DM people links to anything without consent. Do not advertise anything outside of the appropriate channels. #server-guide has information about the different channels.**')
			await message.channel.send(response)
			return
		if command == '$rule6':
			print('getting rule6')
			response = ('**Rule 6 - Do not attempt to bypass punishments.Do not attempt to bypass the filters in any way, this includes using spoiler tags to fake a banned word. Adding alt accounts to the server is not allowed.**')
			await message.channel.send(response)
			return
		if command == '$rule7':
			print('getting rule7')
			response = ('**Rule 7 - Hacks, cheats, and exploits.Showcasing or using hacks, and joining servers that distribute hacks will result in a ban. Do not share any exploits in Krunker and do not joke about hacks.**')
			await message.channel.send(response)
			return
		if command == '$rule8':
			print('getting rule8')
			response = ('**Rule 8 - Use an appropriate nickname and avatar.Your username must be 3 or more english letters and must comply with server rules. NSFW profile pictures are against server rules.**')
			await message.channel.send(response)
			return
		if command == '$rule9':
			print('getting rule9')
			response = ('**Rule 9 - Do not ask users for personal information.Do not ask people for their real name, age, location, or any other identifying information.**')
			await message.channel.send(response)
			return
		if command == '$rule10':
			print('getting rule10')
			response = ('**Rule 10 - Discord Community Guidelines and Terms of Service. https://discordapp.com/guidelines / https://discordapp.com/terms**')
			await message.channel.send(response)
			return



	
        




client.run(TOKEN)