from app.utils.db import db


class Datos(db.Model):
    Customer_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)  
    Age = db.Column(db.Integer)  
    Gender = db.Column(db.String(255)) 
    Item_Purchased = db.Column(db.String(255)) 
    Category = db.Column(db.String(255))
    Purchase_Amount = db.Column(db.Integer)  
    Location = db.Column(db.String(255)) 
    Size = db.Column(db.String(255)) 
    Color = db.Column(db.String(255)) 
    Season = db.Column(db.String(255)) 
    Review_Rating = db.Column(db.Numeric(10, 7))
    Subscription_Status = db.Column(db.String(255)) 
    Payment_Method = db.Column(db.String(255)) 
    Shipping_Type = db.Column(db.String(255)) 
    Discount_Applied = db.Column(db.String(255)) 
    Promo_Code_Used = db.Column(db.String(255)) 
    Previous_Purchases = db.Column(db.Integer)  
    Preferred_Payment_Method = db.Column(db.String(255)) 
    Frequency_of_Purchases = db.Column(db.String(255)) 
    Estado = db.Column(db.String(255))

    def __init__(self, age, gender, item_purchased, category, purchase_amount, location, size, color, season, review_rating,
                 subscription_status, payment_method, shipping_type, discount_applied, promo_code_used,
                 previous_purchases, preferred_payment_method, frequency_of_purchases, estado):
        self.Age = age
        self.Gender = gender
        self.Item_Purchased = item_purchased
        self.Category = category
        self.Purchase_Amount = purchase_amount
        self.Location = location
        self.Size = size
        self.Color = color
        self.Season = season
        self.Review_Rating = review_rating
        self.Subscription_Status = subscription_status
        self.Payment_Method = payment_method
        self.Shipping_Type = shipping_type
        self.Discount_Applied = discount_applied
        self.Promo_Code_Used = promo_code_used
        self.Previous_Purchases = previous_purchases
        self.Preferred_Payment_Method = preferred_payment_method
        self.Frequency_of_Purchases = frequency_of_purchases
        self.Estado = estado

    @property
    def obtenerDatos(self):
        return {
            "Customer_ID": self.Customer_ID,
            "Age": self.Age,
            "Gender": self.Gender,
            "Item_Purchased": self.Item_Purchased,
            "Category": self.Category,
            "Purchase_Amount": self.Purchase_Amount,
            "Location": self.Location,
            "Size": self.Size,
            "Color": self.Color,
            "Season": self.Season,
            "Review_Rating": float(self.Review_Rating) if self.Review_Rating is not None else None,
            "Subscription_Status": self.Subscription_Status,
            "Payment_Method": self.Payment_Method,
            "Shipping_Type": self.Shipping_Type,
            "Discount_Applied": self.Discount_Applied,
            "Promo_Code_Used": self.Promo_Code_Used,
            "Previous_Purchases": self.Previous_Purchases,
            "Preferred_Payment_Method": self.Preferred_Payment_Method,
            "Frequency_of_Purchases": self.Frequency_of_Purchases,
            "Estado": self.Estado
        }
