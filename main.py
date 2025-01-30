import telebot 
from config import token

from logic import Pokemon, Wizard, Fighter
import random

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        chance = random.randint(1, 3)
        if chance == 1:
            pokemon = Pokemon(message.from_user.username)
        elif chance == 2:
            pokemon = Wizard(message.from_user.username)
        else:
            pokemon = Fighter(message.from_user.username)
        
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

@bot.message_handler(commands=['info'])
def info(message):
    if message.from_user.username in Pokemon.pokemons:
        pokemon = Pokemon.pokemons[message.from_user.username]
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        return

@bot.message_handler(commands=['feed'])
def feed(message):
    if message.from_user.username in Pokemon.pokemons:
        Pokemon.pokemons[message.from_user.username].health += random.randint(5, 20)
        Pokemon.pokemons[message.from_user.username].hunger -= random.randint(10, 70)
        bot.reply_to(message, "Ты покормил своего покемона. Здоровье увеличилось!")

@bot.message_handler(commands=['drink'])
def drink(message):
    if message.from_user.username in Pokemon.pokemons:
        Pokemon.pokemons[message.from_user.username].thirst -= random.randint(10, 50)
        bot.reply_to(message, "Ты напоил своего покемона!")


@bot.message_handler(commands=['attack'])
def attack_pok(message):
    if message.reply_to_message:
        if message.reply_to_message.from_user.username in Pokemon.pokemons.keys() and message.from_user.username in Pokemon.pokemons.keys():
            enemy = Pokemon.pokemons[message.reply_to_message.from_user.username]
            pok = Pokemon.pokemons[message.from_user.username]
            res = pok.attack(enemy)
            bot.send_message(message.chat.id, res)
        else:
            bot.send_message(message.chat.id, "Сражаться можно только с покемонами")
    else:
            bot.send_message(message.chat.id, "Чтобы атаковать, нужно ответить на сообщения того, кого хочешь атаковать")


@bot.message_handler(commands=['fight'])
def fight(message):
    if message.from_user.username not in Pokemon.pokemons:
        bot.reply_to(message, "У тебя все еще нету покемона! Используй команду /go")
        return
    
    user_pokemon = Pokemon.pokemons[message.from_user.username]

    enemy_pokemon = Pokemon("Enemy")
    bot.send_message(message.chat.id, f"Твой соперник: {enemy_pokemon.name}!")
    bot.send_photo(message.chat.id, enemy_pokemon.show_img())

    bot.send_message(message.chat.id, f"Сражаются {user_pokemon.name} против {enemy_pokemon.name}")

    player_damage = user_pokemon.strength + user_pokemon.level * 5
    enemy_damage = enemy_pokemon.strength + enemy_pokemon.level * 5

    if player_damage > enemy_damage:
        bot.send_message(message.chat.id, f"Победил {user_pokemon.name}! Твой уровень повышен!")
        user_pokemon.level += 1
        user_pokemon.hunger += random.randint(10, 25)
        user_pokemon.thirst += random.randint(10, 25)
    elif enemy_damage > player_damage:
        bot.send_message(message.chat.id, f"Победил {enemy_pokemon.name}! Не расстраивайся.")
        user_pokemon.hunger += random.randint(10, 25)
        user_pokemon.thirst += random.randint(10, 25)
        user_pokemon.strength -= random.randint(1, 5)
    else:
        bot.send_message(message.chat.id, "Ничья. Вы оба топчики")
        user_pokemon.hunger += random.randint(10, 25)
        user_pokemon.thirst += random.randint(10, 25)


bot.infinity_polling(none_stop=True)

