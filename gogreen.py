import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

tips_mengurangi_polusi = [
    "Gunakan transportasi umum untuk mengurangi emisi gas rumah kaca.",
    "Matikan lampu dan perangkat elektronik yang tidak digunakan untuk menghemat energi.",
    "Gunakan kantong belanja kain atau tas serut yang dapat digunakan berulang kali daripada plastik sekali pakai.",
    "Daur ulang kertas, plastik, logam, dan bahan lainnya secara terpisah untuk mengurangi limbah.",
    "Gunakan produk yang ramah lingkungan atau yang dapat didaur ulang untuk mengurangi dampak lingkungan.",
    "Membuat taman mini disekitar rumah agar udara disekitar rumah lebih segar."
]

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def halo(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')
    
@bot.command()
async def tips(ctx):
    random_tip = random.choice(tips_mengurangi_polusi)
    await ctx.send(f"Salah satu tips mengurangi polusi : {random_tip}")

@bot.command()
async def meme(ctx):
    daftar_gambar = os.listdir('image')
    gambar = random.choice(daftar_gambar)
    with open(f'image/{gambar}', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
    # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)
    
bot.run('Masukan token bot kamu disini')
