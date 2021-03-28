"""Task 2
Напишіть клас робота пилососа
в ініт приймається заряд батареї, заповненість сміттєбака і кількість води
реалізуйте функцію move() - нескінченний цикл який на кожній ітерації "замерзає" на 1 сек
окрім цього на кожній ітерації викликаються функції "wash" і "vacuum cleaner"
(в цих функціях повинні стояти прніти "wash" і "vacuum cleaner" відповідно),
також на кожній ітерації прінтиться "move"
+ на кожній ітерації цикла заряд батареї і кількість води зменшується на певну кількість
(задайте в статік аргументах класу як конфіг пилососа, або в окремому конфіг файлі),
а кількість сміття збільшується
Напишіть власні ексепшини які кидаються коли заряд батареї менше ніж 20%, заряд батареї 0%, кількість води - 0,
 кількість сміття більша ніж певне число
опрацюйте ваші ексепшини (наприклад якщо заряд батареї менше 20% то цикл робить ще певну кількість ітерацій
і зупиняється,
якщо вода закінчилась то пилосос тепер не миє підлогу а тільки пилососить,
0 відсотків заряду - пилосос кричить щоб його занесли на зарядку бо сам доїхати не може)
можете придумати ще свої ексепшини і як їх опрацьовувати """

import time


class LowBattery(Exception):
    pass


class BatteryNoCharge(Exception):
    pass


class FullGarbage(Exception):
    pass


class RobotNoWater(Exception):
    pass


class RobotCleaner:
    max_work_energy = 10
    max_full_rubbish = 70
    max_amount_of_water = 99

    def __init__(self, charge_battery, capacity_rubbish, water_quantity):
        self.charge_battery = charge_battery
        self.capacity_rubbish = capacity_rubbish
        self.water_quantity = water_quantity

    def wash(self):
        if self.water_quantity > 0:
            self.water_quantity = self.water_quantity - self.max_amount_of_water
            print(f"I am washing your floor right now. The amount of water in the tank - {self.water_quantity} ml.")
        else:
            raise RobotNoWater

    def vacuum_cleaner(self):
        if self.charge_battery > 15:
            self.charge_battery = self.charge_battery - self.max_work_energy
            print(f"I am cleaning your house now. The amount of charge - {self.charge_battery}%!")
        elif 1 < self.charge_battery <= 15:
            self.charge_battery -= 1
            raise LowBattery
        else:
            raise BatteryNoCharge
        if self.capacity_rubbish < 220:
            self.capacity_rubbish = self.capacity_rubbish + self.max_full_rubbish
            print(f"I am cleaning your house of rubbish. The amount of rubbish in my tank - {self.capacity_rubbish} ml!"
                  )
        else:
            raise FullGarbage

    def move(self):
        step = 0
        while True:
            print(f"_____________________________________{step}_______________________________________")
            try:
                self.vacuum_cleaner()
            except FullGarbage:
                print("Stop working! My tank is empty")
                self.capacity_rubbish = 0
            except LowBattery:
                print(f"I almost ran out. The amount of charge - {self.charge_battery}%")
            except BatteryNoCharge:
                print('I have no charge. I need to recharge to keep working!')
                exit()
            try:
                self.wash()
            except RobotNoWater:
                print(f" I don't have water. So, I can vacuum clean!")
            step += 1
            time.sleep(1)


Asus2000 = RobotCleaner(100, 0, 750)
Asus2000.move()
