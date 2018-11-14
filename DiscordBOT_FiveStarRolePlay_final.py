import asyncio
import discord
from discord.ext import commands
from discord import message

FiveStarBot = commands.Bot(command_prefix='!')

@FiveStarBot.event
async def on_ready():
    print('Соединение установлено!')
    print('Имя: ',FiveStarBot.user.name)
    print('ID: ',FiveStarBot.user.id)
    print('© FiveStar Role Play, 2018')
    print(' ')
    print('Команды: ')
    print('!cmd - команды бота')
    print('!globalmessage [текст] - отправляет сообщение всем участникам сервера в ЛС')
    print('!message [имя(nick/ID)] [текст] - отправляет сообщение в ЛС определенному участнику')
    print('!members - отправляет список всех участников сервера и их ID Вам в личные сообщения')

@FiveStarBot.event
async def on_message(message):
    if message.content.startswith('!'):
        if message.author != FiveStarBot.user:
            await FiveStarBot.delete_message(message)

    await FiveStarBot.process_commands(message)

@FiveStarBot.command(pass_context=True)
async def cmd(cxt):
    if cxt.message.author.server_permissions.administrator:
        await FiveStarBot.say('``` Команды: \n\n!cmd - команды бота\n!globalmessage [текст] - отправляет сообщение всем участникам сервера в ЛС\n!message [имя(nick/ID)] [текст] - отправляет сообщение в ЛС определенному участнику\n!members - отправляет список всех участников сервера и их ID Вам в личные сообщения```')

@FiveStarBot.command(pass_context=True)
async def globalmessage(cxt, *, text : str):
    if cxt.message.author.server_permissions.administrator: 
        count : str
        count = 0
        print('\n[Лог использования команды !globalmessage]')
        print('Автор сообщения: ',cxt.message.author ,' Текст: ', text)
        print(' ')
        for member in cxt.message.server.members:
            if member != FiveStarBot.user:
                count += 1
                print('[!globalmessage] Отправлено сообщений:', count)
                try:
                    await FiveStarBot.send_message(member, text)
                except Exception:
                    pass

@FiveStarBot.command(pass_context=True)
async def message(cxt, member: discord.Member, *, text : str):
    if cxt.message.author.server_permissions.administrator:
        print('\n[Лог использования команды !message]')
        print('Отправитель: ', cxt.message.author, ' Получатель: ', member, ' Текст: ', text)
        await FiveStarBot.send_message(member, text)                                    

@FiveStarBot.command(pass_context=True)
async def members(cxt):
    if cxt.message.author.server_permissions.administrator:
        count : str
        count = 0
        print('\n[Лог использования команды !members]')
        print('Пользователь: ', cxt.message.author, ' запросил список участников сервера')
        await FiveStarBot.send_message(cxt.message.author, '//----------------------------------MEMBERS-LIST------------------------------------------\n' + '```Users (IDs): ```')
        for member in cxt.message.server.members:
            await FiveStarBot.send_message(cxt.message.author, '```' + member.name + ' (' + member.id + ') ```')
            count +=1
        await FiveStarBot.send_message(cxt.message.author, '------------------------------------------------------------------------------------------//')
        await FiveStarBot.send_message(cxt.message.author, count)

FiveStarBot.run('NDcwMDE0NDU4MjE1NzkyNjQx.DjXUkw.F8P0lEDEJQwiYtFB_5oUGq5b7aY')
