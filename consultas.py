from conexion_bd import connection
import json

class consulta(connection):

    def consultar(nit):
        curs = connection.connected()

        data = []

        curs.execute(f'''SELECT 
        cliente.nit, 
        cliente.nombreCliente, 
        cliente.contrato, 
        cliente.direccion, 
        cliente.planta, 
        cliente.correo, 
        factura.idFactura, 
        factura.fechaInicial, 
        factura.fechaFinal, 
        factura.diasFacturados, 
        factura.CUFE, 
        factura.fechaDian, 
        factura.pdf, 
        factura.numeroFactura, 
        factura.fechaPago, 
        generacion.idgeneracion, 
        generacion.generacionactual, 
        generacion.generacionacumulado, 
        generacion.valorunidad, 
        generacion.valortotal, 
        generacion.diferenciatarifa, 
        generacion.ahorroactual, 
        generacion.ahorroacumulado, 
        generacion.ahorrocodosactual, 
        generacion.ahorrocodosacumulado, 
        generacion.anio, 
        generacion.mes 
    FROM 
        cliente
    JOIN 
        factura ON cliente.nit = factura.nitcliente 
    JOIN 
        generacion ON cliente.nit = generacion.nitcliente
    WHERE
        cliente.nit = {nit};''')

        for row in curs.fetchall():
            data_json = {
                "nit": row[0],
                "nombreCliente": row[1],
                "contrato": row[2],
                "direccion": row[3],
                "planta": row[4],
                "correo": row[5],
                "factura": {
                    "idFactura": row[6],
                    "fechaInicial": str(row[7]),
                    "fechaFinal": str(row[8]),
                    "diasFacturados": row[9],
                    "CUFE": row[10],
                    "fechaDian": str(row[11]),
                    "pdf": row[12],
                    "numeroFactura": row[13],
                    "fechaPago": str(row[14])
                },
                "generacion": {
                    "idgeneracion": row[15],
                    "generacionactual": row[16],
                    "generacionacumulado": row[17],
                    "valorunidad": row[18],
                    "valortotal": row[19],
                    "diferenciatarifa": row[20],
                    "ahorroactual": row[21],
                    "ahorroacumulado": row[22],
                    "ahorrocodosactual": row[23],
                    "ahorrocodosacumulado": row[24],
                    "anio": row[25],
                    "mes": row[26]
                }
            }
            data.append(data_json)

        return json.dumps(data)

    