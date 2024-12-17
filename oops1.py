class employee:
    # special method / magic method - constructor 
    def __init__(self):
        print("Data attributes started executing")
        self.id = 123
        self.salary =50000
        self.designation = "SDE"
        print("Data/attributes initiated")

    def travel(self,destination):
        print("Function/method called")
        print(f"Employee is travelling to {destination}")


        
# creating object , data/attributes are called itself 
sam = employee()

# functions are called manually
sam.travel("kerala")




