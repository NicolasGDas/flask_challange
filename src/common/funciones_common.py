import io 
import json
"""
Funcion que transforma a json y despues a binario la data que sea enviada por parametro
"""
def format_data_for_download(data):
    #trasnformo la data a json y la paso a bytes para ser enviada para descargar
    return io.BytesIO(json.dumps(data).encode('utf-8'))
