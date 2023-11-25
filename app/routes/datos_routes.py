from flask import Blueprint, jsonify, request
from app.controlador import datos_controlador
from app.modelo.datos_modelo import Datos as datos_modelo
from flask_cors import cross_origin

datos_blueprint = Blueprint('datos', __name__)

#Rutas
@datos_blueprint.route('/datos', methods=["GET"])
@datos_blueprint.route('/datos/buscar/<data_ID>', methods=["GET"])
@datos_blueprint.route('/datos/actualizar', methods=["PUT"])
@datos_blueprint.route('/datos/agregar', methods=["POST"])
@datos_blueprint.route('/datos/eliminar', methods=["DELETE"])
@cross_origin()
def managerDatos(data_ID = None):
    try:
        if data_ID == None:
            if request.method == 'GET':
                return datos_controlador.agregar_estado_activo()
            if request.method == 'DELETE':
                datoID = request.json['DatosID'] 
                return datos_controlador.eliminar_dato(datoID) 

            datos = datos_modelo(
                request.json["Age"],
                request.json["Gender"],
                request.json["Item_Purchased"],
                request.json["Category"],
                request.json["Purchase_Amount"],
                request.json["Location"],
                request.json["Size"],
                request.json["Color"],
                request.json["Season"],
                request.json["Review_Rating"],
                request.json["Subscription_Status"],
                request.json["Payment_Method"],
                request.json["Shipping_Type"],
                request.json["Discount_Applied"],
                request.json["Promo_Code_Used"],
                request.json["Previous_Purchases"],
                request.json["Preferred_Payment_Method"],
                request.json["Frequency_of_Purchases"],
                request.json["Estado"]
            )

            if request.method == 'POST':
                return datos_controlador.agregar_Datos(datos)

            if request.method == 'PUT':
                datoID = request.json['DatosID']
                return datos_controlador.actualizar_datos(datoID, datos)

        if data_ID is not None:
            return datos_controlador.obtener_dato_by_ID(data_ID) #  <-
        
    except Exception as e:
        return jsonify(status=False, msg=str(e))
