class Weapon:
    
    def __init__(self, name, damage, range):
        self.name = name
        self.damage = damage
        self.range = range

    def hit(self, actor, target):
        if not target.is_alive():
            print("Враг уже повержен")
        else:
            x1, y1 = actor.get_coords()
            x2, y2 = target.get_coords()
            if ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 > self.range:
                print(f"Враг слишком далеко для оружия {self.name}")
            else:
                target.get_damage(self.damage)
                print(
                    f"Врагу был нанесен урон оружием {self.name} в размере {self.damage}")

    def __str__(self):
        return self.name


class BaseCharacter:
    def __init__(self, pos_x, pos_y, hp):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.hp = hp

    def move(self, delta_x, delta_y):
        self.pos_x += delta_x
        self.pos_y += delta_y

    def is_alive(self):
        if self.hp > 0:
            return True
        return False

    def get_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.hp = 0
        return self.hp

    def get_coords(self):
        return self.pos_x, self.pos_y


class BaseEnemy(BaseCharacter):
    def __init__(self, pos_x, pos_y, hp, weapon):
        super().__init__(pos_x, pos_y, hp)
        self.weapon = weapon

    def hit(self, target):
        if isinstance(target, MainHero):
            self.weapon.hit(self, target)
        else:
            print("Могу ударить только главного героя")

    def __str__(self):
        return f"Враг на позиции ({self.pos_x, self.pos_y}) с оружием {self.weapon}"


class MainHero(BaseCharacter):

    def __init__(self, pos_x, pos_y, hp, name):
        super().__init__(pos_x, pos_y, hp)
        self.max_hp = 200
        self.name = name
        self.weapon = None
        self.weapons = []

    def hit(self, target):
        if isinstance(target, BaseEnemy) and self.weapons:
            self.weapon.hit(self, target)
        elif not isinstance(target, BaseEnemy) and self.weapons:
            print("Могу ударить только врага")
        else:
            print("Я безоружен")

    def add_weapon(self, weapon):
        self.weapons.append(weapon)
        print(f"Подобрал {weapon}")
        if not self.weapon:
            self.weapon = weapon

    def next_weapon(self):
        if self.weapon:
            self.weapon = self.weapons[-1]
            print(f"Сменил оружие на {self.weapon}")
        elif self.weapon and self.weapons[0] == self.weapons[-1]:
            print("У меня только одно оружие")
        else:
            print("Я безоружен")

    def heal(self, amount):
        if self.hp < self.max_hp:
            self.hp += amount
            print(f"Полечился, теперь здоровья {self.hp}")


weapon1 = Weapon("Короткий меч", 5, 1)
weapon2 = Weapon("Длинный меч", 7, 2)
weapon3 = Weapon("Лук", 3, 10)
weapon4 = Weapon("Лазерная орбитаьная пушка", 1000, 1000)
princess = BaseCharacter(100, 100, 100)
archer = BaseEnemy(50, 50, 100, weapon3)
armored_swordsman = BaseEnemy(10, 10, 500, weapon2)
archer.hit(armored_swordsman)
armored_swordsman.move(10, 10)
print(armored_swordsman.get_coords())
main_hero = MainHero(0, 0, 200, "Король Артур")
main_hero.hit(armored_swordsman)
main_hero.next_weapon()
main_hero.add_weapon(weapon1)
main_hero.hit(armored_swordsman)
main_hero.add_weapon(weapon4)
main_hero.hit(armored_swordsman)
main_hero.next_weapon()
main_hero.hit(princess)
main_hero.hit(armored_swordsman)
main_hero.hit(armored_swordsman)
