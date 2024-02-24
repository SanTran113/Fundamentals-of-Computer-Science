class Vehicle():
    def __init__(self, wheels:float, fuel:float, doors:int, roof:bool):
        self.wheels = wheels
        self.fuel = fuel
        self.doors = doors
        self.roof = roof
    # where 0 is the midpoint of whether the roof is on or not
    def __str__(self) -> str:
        return self.wheels, self.fuel, self.doors, self.roof