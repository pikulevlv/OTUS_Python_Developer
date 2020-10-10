# Домашнее задание №2. Классы.
# Цель: в этом ДЗ написать базовый класс и сделать главный модуль,
# при запуске которого выполняется демонстрация работы всех классов.

# 1. Написать базовый класс для средства передвижения, определить у него общие свойства.Например, вес, грузоподъемность.
# 2. Определить общие методы, например “издать звук”.
# 3. Сделать несколько наследников класса. Например: корабль, автомобиль, самолёт.
# 4. Перегрузить у них методы, чтобы соответствовать классу.
# 5. Также добавить свойства, относящиеся к классу: водоизмещение, количество колёс, предельная высота и т.д.
# 6. Базовые классы должны быть реализованы асбстрактными классами при помощи модуля abc.
# 7. Создать более конкретные классы. Например: “легковой автомобиль”, “парусная лодка” и тд.
# 8. Перегрузить общие свойства, а также добавить дополнительные свойства и методы.
# 9. Разнести все классы и исключения в отдельные модули.
# 10. Добавить методы, которые принимают параметры.
# 11. Добавить в инициализатор и другие методы классов выкидывание исключения при передаче неподходящих аргументов,
# или не выполнении других внутренних условий (например, если бак пустой,
# то при попытке “завести” ТС будет выкинуто исключение, что недостаточно топлива).
# 12. Можно создать вспомогательные объекты при помощи датаклассов. Например, объект “двигатель”,
# у которого есть несколько свойств: литраж, количество поршней, максимальное количество оборотов.
# 13. Сделать главный модуль, при запуске которого выполняется демонстрация работы всех классов
# (красивые принты с использованием print приветствуются).

from classes import Car, Jet, Ship, AmphibiaCar, Engine
from exceptions import NegativeValError

if __name__ == '__main__':
    car_engine = Engine(e_model='Mitsubishi У1', e_volume=2.0, e_piston=8,
                         e_fuel_consumption=8.0, e_brake_down=False, e_features={
            'Преимущества':'Довольно экономичный',
            'Недостатки':'Ненадежный, скачут обороты',
            })
    print("Create a car.")
    car = Car(producer='Hyundai', model='i40', mileage=22_000, release_year=2019, engine=car_engine, fuel=0)
    print(car)
    car.make_sound()
    print('Check mileage:', car.get_mileage, 'km.')
    print("Let's go 100 km!")
    car.move(100)
    print('Check fuel:', car.get_fuel(), 'l.')
    print("We have to fill the car. Bought 10 l of fuel.")
    car.fill_up(10)
    print("Let's go 100 km!")
    car.move(100)
    print(f"Good! Check fuel consumption: {car.engine.e_fuel_consumption} l per 100 km.")
    car.sport_mode()
    print(f"Check fuel consumption: {car.engine.e_fuel_consumption} l per 100 km.")
    car.engine.crash()
    print("Trying to go...")
    car.move(1)
    print("Write about the engine...")
    car.engine.get_engine_features()
    print('*'*60)
    print("We need to change the transport.")
    ship_engine = Engine(e_model='Model SE', e_volume=20.0, e_piston=16, e_fuel_consumption=80.,
                             e_brake_down=False, e_features={'Преимущества':'Тихий'})
    print("Create a ship.")
    ship = Ship('V5', 'Mercury', 1_000_000, 1995, ship_engine, 40)
    print(ship)
    ship.make_sound()
    print("Check technical parameters.")
    ship.get_features()
    print('Check fuel:', ship.get_fuel(), 'l.')
    print("We have to fill the ship. Try to fill negative number of fuel.")
    try:
        ship.fill_up(-10)
    except NegativeValError as e:
        print(e)
    print('Try to go negative number of km.')
    try:
        ship.move(-100)
    except NegativeValError as e:
        print(e)
    ship.alarm()
    print('*'*60)
    print("We need to change the transport.")
    jet_engine = Engine(e_model='Aero Model', e_volume=180., e_piston=32, e_fuel_consumption=100., e_brake_down=False,
                        e_features={'Преимущества': 'Не определены'})
    print("Create a jet.")
    jet = Jet('Sukhoi', 'SuperJet', 700_000, 2018, jet_engine, 400)
    print(jet)
    jet.make_sound()
    print('Check fuel:', jet.get_fuel(), 'l.')
    print('Fuel tank volume:', jet.FUEL_TANK)
    print("We have to fill the jet. Bought 300 l of fuel.")
    jet.fill_up(300)
    while jet.get_fuel() > 200:
        print("Pilot: need permission to fly.")
        jet.move(300)
    print('*'*60)
    print("We need to change the transport.")
    amphibia_engine = Engine(e_model='WaterTerra Model', e_volume=1.2, e_piston=4, e_fuel_consumption=10.,
                             e_brake_down=False, e_features={'Преимущества': 'Не определены'})
    print("Create an amphibia.")
    amphibia = AmphibiaCar('Amphicar ', '770', 150_000, 2001, amphibia_engine, 2)
    print(amphibia)
    amphibia.make_sound()
    print("Strange sound. Set features for the amphibia.")
    amphibia.set_basic_features()
    amphibia.make_sound()