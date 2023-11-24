from app.utils.db import db


class Datos(db.Model):
    DatosID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(255))
    Location = db.Column(db.String(255))
    Year = db.Column(db.Integer)
    Kilometers_Driven = db.Column(db.Integer)
    Fuel_Type = db.Column(db.String(255))
    Transmission = db.Column(db.String(255))
    Owner_Type = db.Column(db.String(255))
    Mileage = db.Column(db.String(255))
    Engine = db.Column(db.String(255))
    Power = db.Column(db.String(255))
    Seats = db.Column(db.Numeric(10, 7))
    New_Price = db.Column(db.String(255))
    Price = db.Column(db.Numeric(10, 7))

    def __init__(
        self,
        Name,
        Location,
        Year,
        Kilometers_Driven,
        Fuel_Type,
        Transmission,
        Owner_Type,
        Mileage,
        Engine,
        Power,
        Seats,
        New_Price,
        Price,
    ):
        self.Name = Name
        self.Location = Location
        self.Year = Year
        self.Kilometers_Driven = Kilometers_Driven
        self.Fuel_Type = Fuel_Type
        self.Transmission = Transmission
        self.Owner_Type = Owner_Type
        self.Mileage = Mileage
        self.Engine = Engine
        self.Power = Power
        self.Seats = Seats
        self.New_Price = New_Price
        self.Price = Price

    @property
    def obtenerDatos(self):
        return {
            "DatosID": self.DatosID,
            "Name": self.Name,
            "Location": self.Location,
            "Year": self.Year,
            "Kilometers_Driven": self.Kilometers_Driven,
            "Fuel_Type": self.Fuel_Type,
            "Transmission": self.Transmission,
            "Owner_Type": self.Owner_Type,
            "Mileage": self.Mileage,
            "Engine": self.Engine,
            "Power": self.Power,
            "Seats": self.Seats,
            "New_Price": self.New_Price,
            "Price": self.Price,
        }
