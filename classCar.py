class car:
    def __init__(self,model,company,color,speed):
        self.model=model
        self.company= company
        self.color=color
        self.speed=speed

    def display(self):
        if (self.company=="Audi"):
            print("Cost of Audi Car is = 1.5 million")

        if (self.company=="Mercendens Benz"):
            print("Cost of Benz Car is = 1.2 million")

        if (self.company=="Volkswagen"):
            print("Cost of Volkswagen Car is = 80 Lakhs")

        if (self.company=="KIA"):
            print("Cost of KIA Car is = 90 Lakhs")

        if (self.company=="BMW"):
            print("Cost of BMW Car is = 2 million")


c1 = car("SUV", "KIA", "White", 110)

c1.display()
        
    
