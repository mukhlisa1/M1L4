from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.health = randint(50, 100)
        self.strength = randint(30, 200)
        self.level = randint(1, 10)
        self.hunger = randint(1, 90)
        self.thirst = randint(1, 90)
        self.img = self.get_img()
        self.name = self.get_name()
        self.ability = self.get_ability()

        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['front_default'])
        else:
            return "Pikachu"
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"
        
    def get_ability(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return [ability['ability']['name'] for ability in data['abilities']]
        else:
            return "Pikachu"
        
    def attack(self, enemy):

        temp = ''
        
        if isinstance(self, Wizard):
            if randint(1,5) == 1:
                temp += f'{self.name} применил щит\n'
            else:
                self.health -= enemy.strength
        else:
            self.health -= enemy.strength

        if isinstance(enemy, Wizard):
            if randint(1,5) == 1:
                temp += f'{enemy.name} применил щит\n'
            else:
                enemy.health -= self.strength
        else:
            self.health -= enemy.strength

        if self.health <= 0 and enemy.health <= 0:
            return f"Ничья!"
        elif self.health <= 0:
            return f"{self.pokemon_trainer} победил!"
        elif enemy.health <= 0:
            return f"{enemy.pokemon_trainer} победил!"
        else:
            return f'''
    Сражение состоялось:
    {self.name} HP: {self.health}
    {enemy.name} HP: {enemy.health}
    '''


    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покемона: {self.name},\n Способности: {self.ability},\n Сила: {self.strength},\n Здоровье: {self.health},\n Уровень: {self.level},\n Голод: {self.hunger},\n Жажда: {self.thirst}"
    
    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img

class Wizard(Pokemon):
    pass


class Fighter(Pokemon):

    def attack(self, enemy):
        super_power = randint(5, 15)
        self.strength += super_power
        result = super().attack(enemy)
        self.strength -= super_power
        return result + f"\nБоец применил супер-атаку силой:{super_power} "

