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


    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покемона: {self.name}, Способности: {self.ability}, Сила: {self.strength}, Здоровье: {self.health}, Уровень: {self.level}, Голод: {self.hunger}, Жажда: {self.thirst}"
    
    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img

