from consultas import consulta

class microservice(consulta):

    def ejecucion(nit):
        json_file = consulta.consultar(nit)
        return json_file