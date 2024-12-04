import disnake
from disnake.ext import commands
from disnake import AllowedMentions
from disnake.ext.commands import Bot
from disnake import TextInputStyle



bot = commands.Bot()


@bot.event
async def on_ready():
    print("Бот готов!")


@bot.slash_command()
async def mulipage_modal(inter):
    await inter.response.send_message(
        "Нажми на кнопку",
        components = [
            disnake.ui.Button(label="Верефицироваться <3", style=disnake.ButtonStyle.success, custom_id="open")
                ])


@bot.listen("on_button_click")
async def help_listener(inter: disnake.MessageInteraction):
    if inter.component.custom_id == "open":
        await inter.response.send_modal(modal=page_one())
    else:
        return

class page_one(disnake.ui.Modal):
    def __init__(self):
        components = [
            disnake.ui.TextInput(
                label="Имя:",
                placeholder="Антон/vixlencqqe",
                custom_id="name",
                style=TextInputStyle.short,
                max_length=50,
            ),
            disnake.ui.TextInput(
                label="Возраст",
                placeholder="17 лет",
                custom_id="age",
                style=TextInputStyle.short,
                max_length=50,
            ),
            disnake.ui.TextInput(
                label="Цель?",
                placeholder="Я пришел сюда пообщать",
                custom_id="target",
                style=TextInputStyle.short,
                max_length=50,
            ),
        
        ]
        super().__init__(title="Application", components=components)


    async def callback(self, inter: disnake.ModalInteraction):
        user_id = str(inter.author.id)
        for key, value in inter.text_values.items():
           embed.add_field(
                    name=key.capitalize(),
                    value=value[:1024],
                    inline=False
                )
        await inter.response.send_message(embed=embed)


bot.run("TOKEN")

connection.close()