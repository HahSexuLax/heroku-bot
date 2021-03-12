
import discord
import random
from discord.ext.commands import Bot
import asyncio
from discord.ext import commands
import functools
import itertools
import math
from async_timeout import timeout
import numbers
import os
from discord.utils import get
from time import sleep 
import re
import datetime
import sqlite3
import requests
from bs4 import BeautifulSoup
from discord import FFmpegPCMAudio
import ffmpeg
import youtube_dl
from Cybernator import Paginator 
import json
import requests
from PIL import Image, ImageFont, ImageDraw
import io
from random import choice
import time
import neko
import datetime
import json
from discord.ext import tasks

def get_prefix(bot, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]


bot = commands.Bot(command_prefix = get_prefix)
bot.remove_command('help')



players = {}

@bot.event
async def on_ready():
    guilds = await bot.fetch_guilds(limit = None).flatten()
    await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name=f'Yume • -хелп  | Я смотрю за {len(guilds)}, СЕРВЕРАМИ! '))
    print(f'Если шо меня {len(guilds)} серверов меня юзают!')

@bot.event
async def on_guild_join(guild):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = "-"

    with open("prefixes.json", "w") as f:
        json.dump(prefixes,f)

@bot.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
@bot.event
async def on_member_join( member ):

    channel = bot.get_channel( 782690096632954880 )

    role = discord.utils.get( member.guild.roles, id = None)

    await member.add_roles( role )
    await channel.send(
        embed = discord.Embed(
        icon_url = bot.user.avatar_url,
        title = '**Новый пользователь!**',
        description = f'**{member.name} Приветствуем на {server.name}**',
        footer = f'{bot.user.name} © 2020 | Все права защищены'))

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    with open('C:\\Users\\User\\Desktop\\бот\\lvl.json','r') as f:
        users = json.load(f)
    async def update_data(users,user):
        if not user in users:
            users[user] = {}
            users[user]['exp'] = 0
            users[user]['lvl'] = 1
    async def add_exp(users,user,exp):
        users[user]['exp'] += exp
    async def add_lvl(users,user):
        exp = users[user]['exp']  
        lvl = users[user]['lvl']
        if exp > lvl:
            lvl = lvl + 1
            exp = 0 
            await message.channel.send(f'{message.author.mention}, Повысил свой уровень! {lvl}')
            users[user][exp] = 0
            users[user]['lvl'] = lvl - 1 
    await update_data(users,str(message.author.id))
    await add_exp(users,str(message.author.id),0.1)
    await add_lvl(users,str(message.author.id))
    with open('C:\\Users\\User\\Desktop\\\\lvl.json','w') as f:
         json.dump(users,f)
    await bot.process_commands(message)
@bot.event
async def on_message(message): # Основной ивент, триггериться на сообщение.
    if "Идея:" in message.content: # Проверяет есть ли в сообщении "лол"
        await message.add_reaction("👍") # Добавляет Like
        await message.add_reaction("👎") # Добавляет Dislike
    await bot.process_commands(message) # Обрабатывает команды, которые были в сообщении, чтобы избежать проблем с командами.
    
@bot.event 
async def on_message_edit(message, after): # Побочный ивент, триггериться на изменение сообщения.
    if "Привет" in after.content: # Проверяет есть ли в сообщении "лол"
        await message.add_reaction("👍") 
        await message.add_reaction("👎") 



@bot.event
async def on_command_error(ctx, error):
    pass

@bot.command(pass_context=True)
async def хелп(ctx):
    with open('prefixes.json', 'r') as f:
         prefixes = json.load(f)

         prefix = prefixes[str(ctx.guild.id)]

    embed = discord.Embed(
        colour = discord.Colour.red()

    )
    embed.set_author(name='Список команд:', icon_url = bot.user.avatar_url)
    embed.add_field(name=f'{prefix}хелп', value='Список команд', inline=True)
    embed.add_field(name=f'{prefix}кик', value='Команда кика', inline=True)
    embed.add_field(name=f'{prefix}бан', value='Команда бана', inline=True)
    embed.add_field(name=f'{prefix}аватар', value='Показывает аватар игрока', inline=True)
    embed.add_field(name=f'{prefix}шар', value='Тут нечего писать :D', inline=True)
    embed.add_field(name=f'{prefix}очистить', value='Очистка чата', inline=True)
    embed.add_field(name=f'{prefix}админы_бота', value='Администраторы бота.', inline=True)
    embed.add_field(name=f'{prefix}инфо', value='Посмотреть информацию о боте.', inline=True)
    embed.add_field(name=f'{prefix}юзеринфо', value='Посмотреть информацию о человеке.', inline=True)
    embed.add_field(name=f'{prefix}число', value='Рандомное число', inline=True)
    embed.add_field(name=f'{prefix}дискорд_бота', value='Сервер бота!', inline=True)

    embed.set_footer(icon_url = ctx.author.avatar_url, text = f'Кастомный префикс: {prefix} Станdаpd префикс: -')
    await ctx.send(embed=embed)

@bot.command()
async def дискорд_бота(ctx):

    embed = discord.Embed(
        colour = discord.Colour.blue()
    )
    embed.set_author(name='Дискорд сервер бота:')
    embed.add_field(name='> https://discord.gg/UXejtw9hAp', value='Сервер бота!')       

@bot.command()
@commands.has_permissions(administrator=True)

async def кик(ctx,member:discord.Member,*,reason=None):
    await ctx.channel.purge(limit=1)

    await member.kick(reason=reason)
    await ctx.send(f'Вы кикнули данного человека! ----> {member.mention}, Причина: {reason}. ')


@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)

async def бан(ctx,member:discord.Member,*,reason=None):
    await ctx.channel.purge(limit=1)

    await member.ban(reason=reason)
    await ctx.send(f'Вы забанили данного человека! ----> {member.mention}, Причина: {reason}. ')
 
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)

async def унбан(ctx,member:discord.Member):
    await ctx.channel.purge(limit=1)

    await member.unban
    await ctx.send(f'Вы разбанили данного человека! ----> {member.mention}. ')
    
@bot.command()
async def аватар(ctx, member : discord.Member = None):

    user = ctx.message.author if (member == None) else member

    embed = discord.Embed(title=f'Аватар пользователя {user}', color= 0x0c0c0c)
    embed.set_image(url=user.avatar_url)

    await ctx.send(embed=embed)
@bot.command()
async def шар (ctx):
    responses=['Частично да :D',
               'Неудачная попытка попробуйте ещё раз!',
               'Да..',
               'Нет!']

    await ctx.send(f'\n{random.choice(responses)}')

@bot.command()
@commands.has_permissions(manage_messages = True)
async def очистить(ctx,amount:int = None):
        await ctx.channel.purge(limit=int(amount))
        await ctx.send(f"Удалено {amount} сообщений")


@bot.command(pass_context=True)
async def инфо(ctx):

    embed = discord.Embed(
        colour = discord.Colour.blue()

    )

    embed.set_author(name='Инфо', icon_url = bot.user.avatar_url) 
    embed.add_field(name='Версия:', value='> v1.0.3', inline=False)
    embed.add_field(name='Версия Python', value='> Последняя', inline=False)
    embed.add_field(name='Скорость включения бота:', value='> 7 Секунд')

    embed.set_footer( icon_url = bot.user.avatar_url, text = 'Все права защищены [Сообщение от さようなら私の人生: Приятного дня и использования!]')

    await ctx.send(embed=embed)

@bot.command()
async def secret(ctx):
    embed1 = discord.Embed(title="Страница 1", description='ВЫ НАШЛИ СЕКРЕТКУ!')
    embed2 = discord.Embed(title="Страница 2", description='ПОДАРОК - Секретная роль.')

    embeds = [embed1, embed2]
    reactions = ['⬅️', '➡️']
    message = await ctx.send(embed=embed1)
    page = Paginator(bot, message, only=ctx.author, use_more=False, embeds=embeds, reactions = reactions )
    await page.start()

@bot.command(pass_context=True)
async def админы_бота(ctx):

    embed = discord.Embed(
        colour = discord.Colour.red()

    )

    embed.set_author(name='Админы:', icon_url = bot.user.avatar_url) 
    embed.add_field(name='Создатель:', value='> KoqnC#6666', inline=False)
    embed.add_field(name='Гл. Администратор:', value='Pazitiv4ik#9902', inline=False)
    embed.add_field(name='Администратор:', value='> Нету!', inline=False)
    embed.add_field(name='Администратор:', value='> Нету', inline=False)
    embed.add_field(name='Помощники:', value='> Нету!', inline=False)
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def help(ctx):

    embed = discord.Embed(
        colour = discord.Colour.red()

    )

    embed.set_author(name='Неверная команда:', icon_url = bot.user.avatar_url) 
    embed.add_field(name='Команда:', value='-хелп')
    embed.set_footer(text=';D')
    await ctx.send(embed=embed)


@очистить.error
async def clear_error(ctx, error):
    if isinstance( error, commands.MissingRequiredArgument):
        await ctx.send(f'Привет {ctx.author.name}, в команде Очистке, мы нашли маленькую ошибку, именно то что вы не ввели аргумент Иcпользование: Очистить 100')

    if isinstance( error, commands.MissingPermissions):
        await ctx.send(f'Привет {ctx.author.name}, у вас недостаточно прав для очистки чата! (Required Permissions Administator)')


@бан.error
async def ban_error(ctx, error):

    if isinstance( error, commands.MissingRequiredArgument):
        await ctx.send(f'Привет {ctx.author.name}, Пожалуйста упомяните человека которого хотите забанить!')

    if isinstance( error, commands.MissingPermissions):
        await ctx.send(f'Привет {ctx.author.name}, у вас недостаточно прав для бана! (Required Permissions Administator) ')

@кик.error
async def kick_error(ctx, error):
    if isinstance( error, commands.MissingRequiredArgument):
        await ctx.send(f'Привет {ctx.author.name}, Пожалуйста упомяните человека которого хотите кикнуть!')

    if isinstance( error, commands.MissingPermissions):
        await ctx.send(f'Привет {ctx.author.name}, у вас недостаточно прав для кика! (Required Permissions Administator)')

@bot.command(aliases = ['рандомчисло'])
async def число(ctx, a=None, b=None):
    if a == None:
        msg = await ctx.send(embed=discord.Embed(description='Пример использования: `-число 5 100` - выведу рандомное число от 5 до 100.',  footer='Сразу говорю иногда рандом не работает!', color=discord.Color.purple()))
        await asyncio.sleep(5)
        await msg.delete()
    elif b == None:
        msg = await ctx.send(embed=discord.Embed(description='Вы не указали второе число!', color=discord.Color.orange()))
        await asyncio.sleep(2)
        await msg.delete()
    elif int(a) >= int(b):
        msg = await ctx.send(embed=discord.Embed(description='Первое число не должно быть равно или больше второго!', color=discord.Color.orange()))
        await asyncio.sleep(4)
        await msg.delete()
    else:
        try:
            await ctx.send(embed=discord.Embed(description=str(random.randint(int(a), int(b)))))
        except ValueError:
            msg = await ctx.send(embed=discord.Embed(description='В аргументах присутствуют сторонние символы!', color=discord.Color.orange()))
            await asyncio.sleep(3)
            await msg.delete()

@bot.command()
async def пинг(ctx):
    await ctx.channel.purge(limit = 1)

    await ctx.send(embed = discord.Embed(
        title = '**🏓Понг**',
        description = f'**{bot.ws.latency * 1000:.0f} мс**'
    ))

# Userinfo
@bot.command()
async def юзеринфо(ctx, member: discord.Member):
    await ctx.channel.purge(limit = 1)
    member = ctx.author if not member else member
    roles = [role for role in member.roles]

    embed = discord.Embed(colour = 0x4f4db3, timestamp = ctx.message.created_at )

    embed.set_author(name = f"Информация пользователя - {member}" )
    embed.set_thumbnail(url = member.avatar_url)
    embed.set_footer(text = f"Запросил: {ctx.author.name}", icon_url = ctx.author.avatar_url )

    embed.add_field(name = "Айди пользователя", value = member.id )
    embed.add_field(name = "Имя пользователя", value = member.display_name )

    embed.add_field(name = "Зарегистрирован: ", value = member.created_at.strftime("%a, %#d, %B, %Y, %I:%M %p") )
    embed.add_field(name = "Вошел на сервер:", value = member.joined_at.strftime("%a, %#d, %B, %Y, %I:%M %p") )

    embed.add_field(name = f"Роли({len(roles)})", value = "".join(role.mention for role in roles) )
    embed.add_field(name = "Высшая роль:", value = member.top_role.mention )

    await ctx.send( embed = embed )

@bot.command(pass_context=True)
async def say(ctx):
  await ctx.message.delete()
  say_at_me = input("Введите сообщение через консоль: ")
  await ctx.send(say_at_me)

@bot.command(pass_context=True)
async def chnick(ctx, nick):
    await member.edit(nick=nick)
    await ctx.send(f'Nickname was changed for {member.mention} ')



@bot.command()
async def news(ctx):  
  
    embed = discord.Embed(
        colour = discord.Colour.blue()

    )

    embed.set_author(name=f'Новости Бота!', icon_url = bot.user.avatar_url) 
    embed.add_field(name='News Date:', value='15.10.2020')
    embed.add_field(name='News ---> ', value='Взлом бота и краш его серверов был очень сложный.. Все удалили бота с серверов почти все. Обидненько но я буду работать мне это не мешает!')
    embed.set_footer( icon_url = bot.user.avatar_url, text = 'News Ended')
    await ctx.send(embed=embed)

@bot.command()
async def перезагрузить(ctx):
    await ctx.message.delete()
    message = await ctx.send("Перегейруска... Может займёт 5 минут или часов")
    restart_program()

@bot.command()
@commands.has_role("Права на розыгрыш")
async def gstart(ctx, mins : int, * , prize: str):
    embed = discord.Embed(title = "Раздача", description = f"{prize}", color = discord.Colour.black())

    end = datetime.datetime.utcnow() + datetime.timedelta(seconds = mins*60)

    embed.add_field(name = "Заканчивается в:", value = f"{end} ВРЕМЕНИ!")

    my_msg = await ctx.send(embed= embed)


    await my_msg.add_reaction("🎉")

    await asyncio.sleep(mins)

    new_msg = await ctx.channel.fetch_message(my_msg.id)


    users = await new_msg.reactions[0].users().flatten()
    users.pop(user.index(bot.user))

    winner = random.choice(users)

    await ctx.send("Поздрaвляю тебя! {winner.mention} ты выиграл {prize}")

@bot.command(pass_context = True)
async def начать_опрос(self, ctx, question, *options: str):
        author = ctx.message.author
        server = ctx.message.server

        if not author.server_permissions.manage_messages: return await self.bot.say(DISCORD_SERVER_ERROR_MSG)

        if len(options) <= 1:
            await self.bot.say("```Ошибка! В опросе должно быть несколько вариантов.```")
            return
        if len(options) > 2:
            await self.bot.say("```Ошибка! В опросе может быть не более двух вариантов.```")
            return

        if len(options) == 2 and options[0] == "yes" and options[1] == "no":
            reactions = ['👍', '👎']
        else:
            reactions = ['👍', '👎']

        description = []
        for x, option in enumerate(options):
            description += '\n {} {}'.format(reactions[x], option)

        embed = discord.Embed(title = question, color = 3553599, description = ''.join(description))

        react_message = await self.bot.say(embed = embed)

        for reaction in reactions[:len(options)]:
            await self.bot.add_reaction(react_message, reaction)

        embed.set_footer(text='ID опроса: {}'.format(react_message.id))

        await self.bot.edit_message(react_message, embed=embed)
@bot.command()
async def make_embed(ctx):
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    await ctx.send('Waiting for a title')
    title = await bot.wait_for('message', check=check)
  
    await ctx.send('Waiting for a description')
    desc = await bot.wait_for('message', check=check)

    embed = discord.Embed(title=title.content, description=desc.content, color=0x72d345)
    await ctx.send(embed=embd)

@bot.command()
@commands.has_permissions(administrator = True)
async def изменить_префикс(ctx,prefix):
    with open('prefixes.json', 'r') as f:
         prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

        embed = discord.Embed(color = 0xff9900, title = 'Префикс успешно изменён')
        embed.add_field(name = f'{prefix}', value = f'Слушай фигасе ты! Не плохо твой префикс стал своим!')
        await ctx.send(embed = embed)

@bot.command()
async def fox(ctx):
    response = requests.get('https://some-random-api.ml/canvas/youtube-comment') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xff9900, title = 'Random Fox') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed

bot.run(procces.env.BOT_TOKEN)