from app.modelo.datos_modelo import Datos as datos_modelo

from app.utils.db import db

from app import jsonify

def obtener_Datos():
    try:
        lista_Datos = [dato.obtenerDatos for dato in datos_modelo.query.all()]

        return jsonify(status=True, msg=lista_Datos)
    except Exception as e:
        return jsonify(status= False, msg=str(e))


def agregar_estado_activo():
    try:
        lista_Datos = [dato for dato in datos_modelo.query.all()]
        for dato in lista_Datos:
            dato.Estado = "activo"
        db.session.commit()
        return jsonify(status=True, msg="Se han actualizado los estados.")
    except Exception as e:
        return jsonify(status= False, msg=str(e))


def obtener_dato_by_ID(datos_ID):
    try:
        # Traer el registro según el id dado
        dato = datos_modelo.query.filter_by(DatosID=datos_ID).first()
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
        old_datos = datos_modelo.query.filter_by(DatosID=dato_ID).first()

        old_datos.Name = datos.Name
        old_datos.Location = datos.Location
        old_datos.Year = datos.Year
        old_datos.Kilometers_Driven = datos.Kilometers_Driven
        old_datos.Fuel_Type = datos.Fuel_Type
        old_datos.Transmission = datos.Transmission
        old_datos.Owner_Type = datos.Owner_Type
        old_datos.Mileage = datos.Mileage
        old_datos.Engine = datos.Engine
        old_datos.Power = datos.Power
        old_datos.Seats = datos.Seats
        old_datos.New_Price = datos.New_Price
        old_datos.Price = datos.Price

        db.session.commit()
        return jsonify(status=True, msg='Se ha actualizado el Dato.')
    except Exception as e:
        return jsonify(status=False, msg=str(e))

def eliminar_dato(datos):
    try:
        old_datos = datos_modelo.query.filter_by(DatosID=datos.DatosID).first()

        old_datos.Estado = 'desactivado'
        db.session.commit()
        return jsonify(status=True, msg='Se ha eliminado el Dato.')
    except Exception as e:
        return jsonify(status=False, msg=str(e))
