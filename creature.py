from random import randint


class Creature:
    """Класс сущности."""

    def __init__(self,
                 name: str,
                 attack: int,
                 defend: int,
                 health: int,
                 damage: tuple,
                 ):
        self.name = name
        self.attack = self.validate_att_def(attack, "attack")
        self.defend = self.validate_att_def(defend, "defend")
        self.health = self.validate_health(health)
        self.damage = self.validate_damage(damage)
        self.full_health = health

    def validate_damage(self, value) -> tuple:
        """Валидация урона."""
        if len(value) == 2 and isinstance(value, tuple):
            if value[0] >= 1 and value[1] >= 1:
                return sorted(value)

        raise ValueError(
            "Неверный параметр Damage - "
            "должно быть два числа в кортеже больше 0!"
        )

    def validate_att_def(self, value, param) -> int:
        """Валидация атаки и защиты."""
        if 1 <= value <= 30:
            return value
        raise ValueError(
            f"Параметр {param} должен быть в диапазоне от 1 до 30")

    def validate_health(self, value) -> int:
        """Валидация здоровья."""
        if value <= 0:
            raise ValueError(
                "Health должно быть не меньше 1."
            )
        return value

    def health_info(self, another=None):
        """Инфо по текущему здоровью."""
        if another is not None:
            print(f"Здоровье {another.name} - {another.health}")
        print(f"Здоровье {self.name} - {self.health}")

    def is_alive(self):
        """Проверка жив или нет."""
        return self.health != 0

    def punch(self, defending):
        """Удар."""
        if not self.is_alive():
            print(f"Игрок {self.name} мертв! Он не может атаковать!")
            return
        if not defending.is_alive():
            print(f"Давайте постараемся не трогать мертвых."
                  f"{defending.name} один из таких.")
        print(f"{self.name} атакует {defending.name}!")
        modifier_attack = self.attack - defending.defend + 1
        modifier_attack = max(modifier_attack, 1)
        dice_roll = [randint(1, 6) for _ in range(modifier_attack)]
        if 5 in dice_roll or 6 in dice_roll:
            damage = randint(self.damage[0], self.damage[1])
            defending.health -= damage
            print(f"Удар оказался Успешен! "
                  f"{defending.name} получил урон - {damage}")
            if defending.health <= 0:
                defending.health = 0
                print(f"Игрок {self.name} убил {defending.name}!")
        else:
            print(f"{self.name} промахнулся!")
        self.health_info(defending)


class Player(Creature):
    """Класс Игрока."""
    def __init__(self,
                 name: str,
                 attack: int,
                 defend: int,
                 health: int,
                 damage: tuple
                 ):
        super().__init__(name, attack, defend, health, damage)
        self.heal_count = 4

    def heal(self):
        """Лечение."""
        if not self.is_alive():
            return print(f"Игрок {self.name} мертв! Он не может исцеляться.")
        if self.heal_count == 0:
            return print(f"Игроку {self.name} больше нельзя исцеляться. "
                         f"Хилки кончились =(")
        healing = (0.3 * self.full_health)
        print(f"Здоровье {self.name} увеличено на {int(healing)}")
        self.health += int(healing)
        if self.health > self.full_health:
            self.health = self.full_health
        self.heal_count -= 1
        self.health_info()


class Monster(Creature):
    """Класс монстра."""
    def __init__(self,
                 name: str,
                 attack: int,
                 defend: int,
                 health: int,
                 damage: tuple
                 ):
        super().__init__(name, attack, defend, health, damage)
