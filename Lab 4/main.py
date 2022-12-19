from dataclasses import dataclass


@dataclass
class Person:
    age: int
    fullname: str

    def __str__(self):
        return f"Full name: {self.fullname}\nAge: {self.age}"

@dataclass
class Driver(Person):
    experience: int

    def __str__(self):
        return super().__str__() + f"\nExperience: {self.experience}"


@dataclass
class Engine:
    power: int
    company: str

    def __str__(self):
        return f"Power: {self.power}\nCompany: {self.company}"


@dataclass
class Car:
    brand: str
    carClass: str
    weight: float
    engine: Engine
    driver: Driver

    def start(self):
        print("Поехали")

    def stop(self):
        print("Останавливаемся")

    def turnRight(self):
        print("Поворот направо")

    def turnLeft(self):
        print("Поворот налево")

    def __str__(self):
        return f"Brand: {self.brand}\nClass: {self.carClass}\nWeight: {self.weight}\nEngine: {self.engine}\n" \
               f"Driver: {self.driver}"


@dataclass
class Lorry(Car):
    carrying: int

    def __str__(self):
        return f"{super().__str__()}\nCarrying: {self.carrying}"


@dataclass
class SportCar(Car):
    speedLimit: int

    def __str__(self):
        return f"{super().__str__()}\nSpeed Limit: {self.speedLimit}"


person = Person(age=20, fullname="John Doe")
driver = Driver(experience=2, age=20, fullname="John Doe")
engine = Engine(power=250, company='Mercedes')
car = Car(brand="Mercedes", carClass="S", driver=driver, engine=engine, weight=1200.0)
print(car)

lorry = Lorry(brand="Volvo", carClass="E", weight=3000.0, engine=engine, driver=driver, carrying=2000)
print(f"\n{lorry}")

sport_car = SportCar(brand="Ferrari", carClass="S", weight=1500.0, engine=engine, driver=driver, speedLimit=250)
print(f"\n{sport_car}")