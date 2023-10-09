from creature import Monster, Player
from time import sleep


class Battle:
    def __init__(self, player, enemies):
        self.player = player
        self.enemies = enemies

    def start_battle(self):
        print(
            f"Бой начинается! Игрок {self.player.name}"
            " вступает в бой против монстров:")
        for enemy in self.enemies:
            print(f"{enemy.name} ({enemy.health} здоровья)")

        while self.player.is_alive() and any(
                enemy.is_alive() for enemy in self.enemies):
            for enemy in self.enemies:
                if enemy.is_alive():
                    sleep(3)
                    self.player.punch(enemy)
                    if enemy.is_alive():
                        sleep(3)
                        enemy.punch(self.player)
                    else:
                        print(f"{enemy.name} погиб!")
                        self.enemies.remove(enemy)

            if self.player.is_alive() and self.player.health > (
                    self.player.full_health * 0.3
            ):
                self.player.heal()

        if self.player.is_alive():
            print(f"Игрок {self.player.name} одержал победу!")
        else:
            print(f"Игрок {self.player.name} погиб в бою.")


if __name__ == "__main__":
    player = Player("Marti", 30, 25, 100, (1, 100))
    monsters = [Monster("Ork", 20, 25, 30, (1, 50)),
                Monster("Baldus", 30, 30, 100, (20, 100))]

    battle = Battle(player, monsters)
    battle.start_battle()
