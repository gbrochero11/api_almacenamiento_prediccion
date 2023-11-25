from app.modelo.datos_modelo import Datos as datos_modelo

from app.utils.db import db

from app import jsonify

def obtener_Datos():
    try:
        lista_Datos = [dato.obtenerDatos for dato in datos_modelo.query.all()]

        return jsonify(status=True, msg=lista_Datos)
    except Exception as e:
        return jsonify(status= False, msg=str(e))


def obtener_dato_by_ID(datos_ID):
    try:
        # Traer el registro según el id dado
        dato = datos_modelo.query.filter_by(Customer_ID=datos_ID).first()
        # si está vacio enviar mensaje
        if dato is None:
            return jsonify(status=False, msg="No se encontraron Datos.")
        
        return jsonify(status=True, msg=dato.obtenerDatos)
    except Exception as e:
        return jsonify(status=False, msg=str(e))

def agregar_Datos(datos):
    try:
        db.session.add(datos)
        db.session.commit()
        return jsonify(status=True, msg="Datos agregados correctamente.")
    except Exception as e:
        return jsonify(status=False, msg=str(e))

def actualizar_datos(dato_ID, datos):
    try:
        old_datos = datos_modelo.query.filter_by(Customer_ID=dato_ID).first()
        old_datos.Age = datos.Age 
        old_datos.Gender = datos.Gender 
        old_datos.Item_Purchased = datos.Item_Purchased 
        old_datos.Category = datos.Category 
        old_datos.Purchase_Amount = datos.Purchase_Amount 
        old_datos.Location = datos.Location 
        old_datos.Size = datos.Size 
        old_datos.Color = datos.Color 
        old_datos.Season = datos.Season 
        old_datos.Review_Rating = datos.Review_Rating 
        old_datos.Subscription_Status = datos.Subscription_Status 
        old_datos.Payment_Method = datos.Payment_Method 
        old_datos.Shipping_Type = datos.Shipping_Type 
        old_datos.Discount_Applied = datos.Discount_Applied 
        old_datos.Promo_Code_Used = datos.Promo_Code_Used 
        old_datos.Previous_Purchases = datos.Previous_Purchases 
        old_datos.Preferred_Payment_Method = datos.Preferred_Payment_Method 
        old_datos.Frequency_of_Purchases = datos.Frequency_of_Purchases 
        old_datos.Estado = datos.Estado 
        db.session.commit()
        return jsonify(status=True, msg='Se ha actualizado el Dato.')
    except Exception as e:
        return jsonify(status=False, msg=str(e))

def eliminar_dato(dato_ID,datos):
    try:
        old_datos = datos_modelo.query.filter_by(Customer_ID=dato_ID).first()

        old_datos.Estado = 'desactivado'
        db.session.commit()
        return jsonify(status=True, msg='Se ha eliminado el Dato.')
    except Exception as e:
        return jsonify(status=False, msg=str(e))
