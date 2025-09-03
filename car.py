class Car:
    wheels=4
    def __init__(self, brand,color, topspeed, acceleration_rate):
        self.brand=brand
        self.color=color
        self.topspeed=topspeed
        self.acceleration=acceleration_rate
    def check_speed(self, time_travelled):
        speed=time_travelled*self.acceleration
        if speed>=self.topspeed:
            return self.topspeed
        else:
            return speed
    def check_distance(self,average_speed, time_travelled):
        if average_speed>self.topspeed:
            return "Impossible"
        else:
            distance=average_speed*time_travelled
            return distance
    
Mercedes= Car("Mercedes","Blue", 140, 0.03)
print(Mercedes.brand)
print(Mercedes.color)
print(f"{Mercedes.topspeed}km/hr")
print(f"{Mercedes.acceleration}km/hr^2")
print(Mercedes.check_distance(76, 20))
print(Mercedes.check_speed(2000))
print(Mercedes.check_speed(5))
print(Mercedes.check_speed(6))