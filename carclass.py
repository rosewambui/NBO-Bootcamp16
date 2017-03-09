class Car(object):


    def __init__(self, name='General', model='GM',car_type='honda') :
        self.name = name
        self.model = model
        self.car_type = car_type
        self.speed=0

        if name== 'Porshe' or name== 'Koenigsegg':
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4

        if car_type == 'trailer':
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4
    
    def doors(self, num_of_doors):
        pass

    
    def drive(self, moving_man):
        return moving_man

    def drive(self, speed):
        if self.car_type == 'trailer':
            self.speed = speed * 11
        else:
            self.speed = 10 ** speed

        return self

    def wheels(self, num_of_wheels):
        return num_of_wheels
        
    def is_saloon(self):
        if self.car_type ==  'trailer':
          return False
        else:
            return True