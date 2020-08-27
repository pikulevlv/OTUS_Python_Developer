import re
import random
from abc import ABCMeta, abstractmethod
from exceptions import NegativeValError

class BaseVehicle(metaclass=ABCMeta):
    @abstractmethod
    def get_mileage(self) -> int:
        raise NotImplementedError
    @abstractmethod
    def move(self, distance: int) -> int:
        raise NotImplementedError
    @abstractmethod
    def get_features(self) -> None:
        raise NotImplementedError
    @abstractmethod
    def make_sound(self) -> None:
        raise NotImplementedError
    # @abstractmethod
    # def make_sound2(self) -> None:
    #     raise NotImplementedError


class MechanicVehicle(BaseVehicle):
    TONNAGE = 200
    ENVIRONMENT = 'terrestrial'
    WEIGHT = 1000
    SOUND = 'trr'
    FUEL_TANK = 45

    def __init__(self, producer, model, mileage,
                 release_year, fuel_consumption, fuel=0):
        self.__producer = producer
        self.__model = model
        self.__mileage = mileage
        self.__release_year = release_year
        self.fuel_consumption = fuel_consumption
        self.__fuel = fuel
        
        numeric_val_list = [self.TONNAGE, self.WEIGHT, self.FUEL_TANK, self.__mileage,
                            self.__release_year, self.fuel_consumption, self.__fuel]
        if sum(map(lambda x: isinstance(x, (int, float)), numeric_val_list)) != len(numeric_val_list):
            print("Please, call get_features() and check data type of numeric variables.")

    def __str__(self):
        return f"{self.__class__.__name__} {self.__producer} {self.__model} {self.__release_year}"
    def __repr__(self):
        return f"{self.__class__.__name__} {self.__producer} {self.__model} {self.__release_year}"

    def get_mileage(self):
        return self.__mileage

    def get_fuel(self):
        return self.__fuel

    def move(self, distance):
        if distance < 0:
            raise NegativeValError(distance)
        # расчет кол-ва топлива
        need_fuel = distance * self.fuel_consumption
        # проверка достаточности топлива
        if self.__fuel >= need_fuel:
            # расходование топлива
            self.__fuel -= need_fuel
            self.__mileage += distance
            print(f"{self.__producer} {self.__model} went {distance} km "
            f"and spent {need_fuel} units of fuel. {self.__fuel} units of fuel left in the tank.")
        else:
            print(f"You need {need_fuel} units of fuel, but you have {self.__fuel}. " +
                  f"Please, fill up your {self.__producer} {self.__model} " +
                  f"(at least {(need_fuel-self.__fuel):.3f} units).")
            return

    def fill_up(self, fuel_units):
        if fuel_units < 0:
            raise NegativeValError(fuel_units)
        total_fuel = self.__fuel + fuel_units
        if total_fuel > self.FUEL_TANK:
            lost_fuel = total_fuel - self.FUEL_TANK
            self.__fuel = self.FUEL_TANK
            print(f"{self.__producer} {self.__model} was filled up with {__fuel_units} units of fuel."
            f" Unfortunately, {lost_fuel} units of fuel were lost. Fuel rank: {self.__fuel}.")
        else:
            self.__fuel += fuel_units
            print(f"{self.__producer} {self.__model} was filled up with {fuel_units} units of fuel." +
                  f" Fuel rank: {self.__fuel}.")

    def get_features(self):
        pattern = '^[A-Z]+'
        basic_attr_list = [re.search(pattern, i).string for i in dir(self) if (re.search(pattern, i) != None)]
        add_attr_list = [i for i in self.__dict__.keys() if i not in basic_attr_list]
        print(self.__class__.__name__)
        print(f"{self} has basic features:")
        for a in basic_attr_list:
            print('\t'+a)
        print(f"{self} has additional features:")
        for a in add_attr_list:
            print('\t'+a)

    def make_sound(self):
        print(f"{self.__producer} {self.__model} made sound '{self.SOUND}'.")


class Ship(MechanicVehicle):
    SAILS = 2

    def alarm(self):
        print('DANGER! Din-don-din-don!!!')


class Car(MechanicVehicle):
    WHEELS = 4
    MAX_SPEED = 200
    SPORT_MODE = False
    def sport_mode(self, sport_mode_coef = 1.2):
        self.SPORT_MODE = not self.SPORT_MODE

        if self.SPORT_MODE == True:
            self.fuel_consumption *= sport_mode_coef
            print(f'Turn on sport mode! Fuel consumption: {self.fuel_consumption} fuel units per km.')
        elif self.SPORT_MODE == False:
            self.fuel_consumption /= sport_mode_coef
            print(f'Turn off sport mode! Fuel consumption: {self.fuel_consumption} fuel units per km.')

class Jet(MechanicVehicle):
    WHEELS = 3
    WINGS = 2

    def permission_to_fly(self):
        # print('Pilot: requesting permission to take off.')
        permission = random.choices([True, False], weights=[60, 40])[0]
        if permission:
            print('Dispatcher: Permission to take off.')
            return permission
        else:
            print('Dispatcher: You can not take off. Wait.')
            return permission

    def permission_decorator(func):
        def new_func(self, *args, **kwargs):
            prm = self.permission_to_fly()
            if prm:
                return func(self, *args, **kwargs)
            else:
                return
        return new_func

    @permission_decorator
    def move(self, distance):
        super().move(distance)

class AmphibiaCar(Car, Ship):

    def set_basic_features(self):
        print(f"You're going to enter values for {self.__class__.__name__}' basic features.")
        print("""Suggested values:
                    ENVIRONMENT:terrestrial/marine
                    FUEL_TANK:30
                    MAX_SPEED:90
                    SAILS:0
                    SOUND:bul beep bul
                    SPORT_MODE:PASS
                    TONNAGE:100
                    WEIGHT:670
                    WHEELS:4""")
        print("Enter 'Y' to do that. If you want to set some values manually, enter any other.")
        enter_or_not = input("Enter:")
        if enter_or_not.upper() == 'Y':
            self.ENVIRONMENT = 'terrestrial/marine'
            self.FUEL_TANK = 30
            self.MAX_SPEED = 90
            self.SAILS = 0
            self.SOUND = 'bul beep bul'
            self.TONNAGE = 100
            self.WEIGHT = 670
            self.WHEELS = 4
            print('The values are set.')
        else:
            print('The changes are not accepted.')

    def get_features(self):
        pattern = '^[A-Z]+'
        basic_attr_list = [re.search(pattern, i).string for i in dir(self) if (re.search(pattern, i) != None)]
        add_attr_list   = [i for i in self.__dict__.keys() if i not in basic_attr_list]
        print(f"{self} has basic features:")
        for a in basic_attr_list:
            print(f"\t{a}: {getattr(self, a)}")
        print(f"{self} has additional features:")
        for a in add_attr_list:
            print(f"\t{a}: {getattr(self, a)}")


if __name__ == '__main__':
    some_vhcl = MechanicVehicle('KIA', 'Rio', 22_000, 2019, 8/100, 0)
    print(some_vhcl)
    some_vhcl.move(15)
    some_vhcl.fill_up(1.2)
    some_vhcl.move(15)
    some_vhcl.make_sound()
    # some_vhcl.set_sound('beep')
    some_vhcl.make_sound()
    some_vhcl.get_features()
    print('*'*30)
    ship = Ship('V5', 'Mercury', 1_000_000, 1995, 80, 40)
    ship.TONNAGE = 1_000_000
    ship.ENVIRONMENT = 'marine'
    ship.WEIGHT = 2_000_000
    ship.SOUND = 'tooo'
    ship.FUEL_TANK = 1000
    ship.alarm()
    print(ship)
    ship.make_sound()
    ship.get_features()
    print('*' * 30)
    car = Car('Kia', 'Sportage', 5, 2020, 8.5, 5)
    car.TONNAGE = 400
    car.WEIGHT = 1300
    car.SOUND = 'beep'
    car.FUEL_TANK = 55
    print(car)
    car.make_sound()
    car.get_features()
    car.sport_mode()
    car.sport_mode()
    car.sport_mode()
    car.sport_mode()
    print('*' * 30)
    jet = Jet('Sukhoi', 'SuperJet', 700_000, 2018, 100, 50000)
    jet.TONNAGE = 2000
    jet.ENVIRONMENT = 'air'
    jet.WEIGHT = 5000
    jet.SOUND = 'fooo'
    jet.FUEL_TANK = 1000
    jet.SAILS = 1000
    jet.MAX_SPEED = 1000
    jet.make_sound()
    jet.get_features()
    jet.move(100)
    jet.move(100)
    jet.move(100)
    jet.move(100)
    print(jet)
    print('*' * 30)
    amphibia = AmphibiaCar('Amphicar ', '770', 150_000, '2001', 10, 2)
    print(amphibia)
    # amphibia.TONNAGE = 100
    # amphibia.ENVIRONMENT = 'terrestrial/marine'
    # amphibia.WEIGHT = 670
    # amphibia.SOUND = 'bul beep bul'
    # amphibia.FUEL_TANK = 30
    amphibia.alarm()
    amphibia.set_basic_features()
    # amphibia.fill_up(-5)
    amphibia.fill_up(fuel_units=5)
    amphibia.get_features()









