
class Result2:
    def __init__(self):
        self.hasLabel = True
        self.isBottle = False
        self.hasFigure = False
        self.hasLabel = False
        self.wht_tsp = False
        self.others = False
        self.green = False
        self.blue = False
        self.final_result = 0
        self.path = "/Users/bonha/realtimefirebase_easypath/image/0.png"
    
    def print_final_color(self):
        if(self.wht_tsp):
            print("White/Transparent")
        elif(self.green):
            print("Green")
        elif(self.blue):
            print("Blue")
        else:
            print("Other")

    def print_final_result(self):
        print("\n\n===================================================\n")
        print("Result ==>\tBottle? " +str(self.isBottle))
        if(self.hasFigure):
            print("\t\tFigure? " +str(self.hasFigure))
        print("\t\tLabel? " +str(self.hasLabel))
        print("\t\tColor? ",end='')
        self.print_final_color()
    
    def calculate_result(self):
        if(not self.isBottle):
            self.final_result =0
        elif(not self.hasLabel):
            if(self.hasFigure):
                self.final_result = 0
            elif(not self.hasFigure):
                if(self.blue):
                    self.final_result = 5
                if(self.green):
                    self.final_result = 6
                if(self.wht_tsp):
                    self.final_result = 7
                if(self.others):
                    self.final_result = 8

        elif(self.hasLabel):
            if(self.blue):
                self.final_result = 1
            if(self.green):
                self.final_result = 2
            if(self.wht_tsp):
                self.final_result = 3
            if(self.others):
                self.final_result = 4


res3 = Result2()
