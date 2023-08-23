import pandas as pd
class Flight():
    def __init__(self):
        self.__dict = {"FlightId":["AI161E90","BR161F91","Al161F99","VS171E20","AS171G30","AI131F49"],
        "From":["BLR","BOM","BBI","JLR","HYD","HYD"],"To":["BOM","BBI","BLR","BBI","JLR","BOM"],
        "Price":[5600,6750,8210,5500,4400,3499]}
        self.__df = pd.DataFrame(self.__dict)
    def fetch_dataFrame(self):
        return self.__df
F = Flight()
Flight_data = F.fetch_dataFrame()
print("""
    Choose the Option below to Look at Flight Details:
    Press 1 : To Look Through Flight Id
    Press 2 : To Look Through Source City
    Press 3 : To Look Through Destination City
      """)
Choice = int(input("Enter your choice "))
if(Choice == 1):
    FlightId_ = input("Enter The Flight You want Details on : ")
    print(Flight_data.loc[Flight_data["FlightId"]==FlightId_].to_string())
elif(Choice == 2):
    Source_ = input("Enter The City You want to Fly From : ")
    print(Flight_data.loc[Flight_data["From"]==Source_].to_string())
else:
    To_ = input("Enter Your destination City : ")
    print(Flight_data.loc[Flight_data["To"]==To_].to_string())

    

