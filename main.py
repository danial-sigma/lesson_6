import os
import discord,random,requests
from discord.ext import commands

from key import token
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
garbages=[
    'Пластик:В год выробатывается около 400 миллионов тонн пластика,По некоторым данным из интернета, примерно 80% отработанного пластика невозможно правильно переработать,И лишь переработке подвергается от 14% пластиковых отходов                                                                                                                                                  ',
    'Дерево:Деревья играют ключевую роль в экосистеме, обеспечивая кислород, очищая воздух и служа домом для множества животных. Они также помогают предотвращать эрозию почвы и регулируют климат, поглощая углекислый газ. Однако вырубка лесов и загрязнение окружающей среды угрожают этим важным ресурсам, что приводит к потере биоразнообразия и ухудшению качества жизни на планете.',    'Вода:Загрязнение воды — это серьезная проблема, вызванная различными факторами. Промышленные отходы, сельскохозяйственные химикаты и пластиковые изделия, попадая в водоемы, ухудшают качество воды и наносят вред экосистемам. Кроме того, несанкционированные сбросы сточных вод и бытовые отходы также способствуют загрязнению, что негативно сказывается на здоровье людей и животных.',
    'Воздух:Воздух — это смесь газов, необходимая для дыхания всех живых существ. Он играет ключевую роль в поддержании жизни, но загрязнение, вызванное промышленностью и транспортом, ухудшает его качество. Это приводит к проблемам со здоровьем и изменению климата, что подчеркивает важность охраны окружающей среды для сохранения чистоты воздуха.']    

@bot.command()
async def mem(ctx):
    mema=random.choice(os.listdir("images"))
    with open(f'images/{mema}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)
@bot.command()
async def question_random(ctx):
    selected_message = random.choice(garbages)
    await ctx.send(selected_message)
@bot.command()
async def question_all(ctx):
    await ctx.send(garbages)
@bot.command()
async def question_image_water(ctx):
    water=random.choice(os.listdir('images'))
    with open(f'images/{water}','rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

bot.run(token())