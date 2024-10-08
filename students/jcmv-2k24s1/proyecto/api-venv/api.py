from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd
import uvicorn

# Cargar el modelo previamente guardado
with open("modelo_consumo_pickle.pkl", "rb") as f:
    modelo = pickle.load(f)

# Definir la estructura de la petición usando Pydantic
class ConsumoRequest(BaseModel):
    idproducto: str
    ciclo: str
    observacion_lectura: str
    tipo: str
    estado_tecnico: str
    barrio: str
    uso: str
    estrato: str
    zona: str
    anio: str
    mes: str
    cantidadfestivos: str
    consumo_promedio: str

app = FastAPI()

def transfor_model_columnas(datos):
    result = pd.DataFrame()

    # Definir las columnas esperadas por el modelo
    columnas_esperadas = [
        'idproducto',
        'ciclo',
        'zona',
        'anio',
        'mes',
        'cantidadfestivos',
        'consumo_promedio',
        'observacion_lectura_ALTO CONSUMO CONFIR POR CRITICA',
        'observacion_lectura_BAJO LLAVE',
        'observacion_lectura_DESACUMULACION DE CONSUMO',
        'observacion_lectura_DESOCUPADO',
        'observacion_lectura_DIRECTO',
        'observacion_lectura_FRENADO',
        'observacion_lectura_FUGA IMPERCEPTIBLE',
        'observacion_lectura_INACCESIBLE',
        'observacion_lectura_INUNDADO',
        'observacion_lectura_MEDIDOR CON CONCRETO Y/O REJA',
        'observacion_lectura_MEDIDOR NUEVO',
        'observacion_lectura_NORMAL',
        'observacion_lectura_SUSPENDIDO',
        'observacion_lectura_TAPADO',
        'observacion_lectura_USUARIO CONSUMOS MINIMOS',
        'observacion_lectura_VOLTEADO',
        'tipo_Cobro Lectura Critica',
        'tipo_Consumo Estimado',
        'tipo_Diferencia Lecturas',
        'tipo_Promedio Estrato',
        'tipo_Promedio Usuario',
        'estado_tecnico_CON SERVICIO',
        'estado_tecnico_CORTADO',
        'estado_tecnico_SUSCRIPTOR INACTIVO',
        'estado_tecnico_SUSPENDIDO FALTA  DE PAGO',
        'estado_tecnico_USUARIO CON CORTE ESPECIAL',
        'barrio_1 DE MAYO',
        'barrio_13 DE JUNIO',
        'barrio_14 DE OCTUBRE',
        'barrio_19 DE ENERO BAJO',
        'barrio_25 DE MAYO',
        'barrio_7 DE AGOSTO',
        'barrio_8 DE MARZO',
        'barrio_ALBERTO ZULETA',
        'barrio_ALCAZAR',
        'barrio_ALFONSO LOPEZ',
        'barrio_ALTOS DE AGUABONITA',
        'barrio_ALTOS DE LOS OCOBOS',
        'barrio_ANTONIO NARINO',
        'barrio_ARENALES',
        'barrio_ARRAYANES',
        'barrio_AV. CENTENARIO',
        'barrio_BAHIA BLANCA',
        'barrio_BELEN',
        'barrio_BELENCITO',
        'barrio_BELLO HORIZONTE',
        'barrio_BERLIN',
        'barrio_BLOQUES DE BOSQUES DE PINARES',
        'barrio_BOYACA',
        'barrio_BR LA ALAMEDA',
        'barrio_BR LOS LIBERTADORES',
        'barrio_BR NUEVA CECILIA',
        'barrio_BR RINCON SANTO',
        'barrio_BR SANTANDER',
        'barrio_BRISAS DEL BOSQUE',
        'barrio_BRISAS DEL CAMPO',
        'barrio_BUENOS AIRES',
        'barrio_BUENOS AIRES BAJO',
        'barrio_BUENOS AIRES PLANO',
        'barrio_BULEVAR DEL CENTENARIO',
        'barrio_C. R. IBERICA',
        'barrio_C.C. PORTAL DEL QUINDIO',
        'barrio_C.C. Y RES BALEARES',
        'barrio_C.CER. BRISAS DE LA SECRETA',
        'barrio_C.CER. CAMINOS DEL CAMPO',
        'barrio_C.CER. LA COLONIA',
        'barrio_C.R MIRADOR DEL QUINDIO',
        'barrio_C.R RIBADEO',
        'barrio_C.R. BOREAL',
        'barrio_C.R. BOSQUES DE PALERMO',
        'barrio_C.R. BOSQUES DE VIENA',
        'barrio_C.R. EL RETIRO',
        'barrio_C.R. LA PASTORITA',
        'barrio_C.R. LOS ANDES',
        'barrio_C.R. LOS GERANIOS',
        'barrio_C.R. QUINTAS DE LA CASTELLANA',
        'barrio_C.R. QUINTAS DE SAN JULIAN',
        'barrio_C.R. RINCON DE ANDALUCIA',
        'barrio_C.R. TORRES DE ALCAZAR',
        'barrio_CALIMA',
        'barrio_CASTILLA GRANDE',
        'barrio_CASTILLA NUEVA',
        'barrio_CENTRO',
        'barrio_CIUD DEL CAFE',
        'barrio_CIUD PUERTO ESPEJO',
        'barrio_CIUD SIMON BOLIVAR',
        'barrio_CIUD SORRENTO',
        'barrio_CIUDAD DORADA',
        'barrio_CIUDADELA CHILACOA',
        'barrio_CIUDADELA COMFENALCO',
        'barrio_CIUDADELA EL SOL',
        'barrio_COINCA',
        'barrio_COND ALTOS DE SOTAVENTO',
        'barrio_COND ASTURIAS',
        'barrio_COND BULEVAR DEL COLISEO',
        'barrio_COND EL CARMELO',
        'barrio_COND EL CORTIJO',
        'barrio_COND GALICIA',
        'barrio_COND LA ABADIA',
        'barrio_COND LA AURORA',
        'barrio_COND NISA BULEVAR',
        'barrio_COND PARQUE DE LA VILLA',
        'barrio_COND RESERVA DE LA SABANA',
        'barrio_COND SALAMANCA',
        'barrio_COND TORRES DEL RIO',
        'barrio_CONJ BOSQUES DE GIBRALTAR',
        'barrio_CONJ BOSQUES DE SAN MARTIN',
        'barrio_CONJ CA?O CRISTALES',
        'barrio_CONJ CRISTALES',
        'barrio_CONJ LA ALQUERIA',
        'barrio_CONJ LA HACIENDA',
        'barrio_CONJ PALMA REAL',
        'barrio_CONJ PALMAS DE SORRENTO',
        'barrio_CONJ PROVITEQ',
        'barrio_CONJ VILLA  JARDIN',
        'barrio_COOPERATIVO',
        'barrio_CORBONES',
        'barrio_EL CAMINO DE COCORA',
        'barrio_EL NOGAL',
        'barrio_EL PLACER',
        'barrio_EL PRADO',
        'barrio_ENTRE LOMAS',
        'barrio_FARALLONES',
        'barrio_FUNDADORES',
        'barrio_FUNDADORES BAJO',
        'barrio_GAITAN',
        'barrio_GIBRALTAR',
        'barrio_GRAN BRETANA',
        'barrio_GRANADA',
        'barrio_GUAYAQUIL',
        'barrio_JARDIN DE LA FACHADA',
        'barrio_JARDINES DEL EDEN',
        'barrio_LA ADIELA',
        'barrio_LA CABANA',
        'barrio_LA CAMPINA',
        'barrio_LA CASTELLANA',
        'barrio_LA CASTELLANA ',
        'barrio_LA CASTILLA',
        'barrio_LA CECILIA',
        'barrio_LA CLARITA',
        'barrio_LA DIVISA',
        'barrio_LA FACHADA',
        'barrio_LA FACHADA ',
        'barrio_LA FOGATA',
        'barrio_LA ISABELA',
        'barrio_LA LORENA',
        'barrio_LA MILAGROSA',
        'barrio_LA MIRANDA',
        'barrio_LA MONTANA',
        'barrio_LA PAVONA',
        'barrio_LAS ACACIAS',
        'barrio_LAS AMERICAS',
        'barrio_LAS MERCEDES',
        'barrio_LAS PALMAS',
        'barrio_LAURELES',
        'barrio_LOS ALAMOS',
        'barrio_LOS CAMBULOS',
        'barrio_LOS NARANJOS',
        'barrio_LOS PROFESIONALES',
        'barrio_LOS QUINDOS',
        'barrio_MANUELA BELTRAN',
        'barrio_MERCAR S.A.',
        'barrio_MIRAFLORES',
        'barrio_MODELO',
        'barrio_MONTEPRADO',
        'barrio_NIAGARA',
        'barrio_NORTE',
        'barrio_NUEVA LIBERTAD',
        'barrio_NUEVO ARMENIA',
        'barrio_NUEVO BERLIN',
        'barrio_NVA BRASILIA',
        'barrio_OBRERO MUNICIPAL',
        'barrio_P. R. COCORA',
        'barrio_P.R CAMINOS DEL BOSQUE',
        'barrio_P.R EL DORADO',
        'barrio_P.R. CALLEJAS DE SAN JOSE',
        'barrio_P.R. CISNEROS',
        'barrio_P.R. JARDIN DE LAS AMERICAS',
        'barrio_P.R. LAS RAMBLAS',
        'barrio_PARAISO',
        'barrio_PARQUE RESIDENCIAL DEL CAFE',
        'barrio_PARQUES DE BOLIVAR',
        'barrio_PATIO BONITO',
        'barrio_PATIO BONITO ALTO',
        'barrio_PINARES',
        'barrio_POPULAR',
        'barrio_PROVIDENCIA',
        'barrio_QUINDIO',
        'barrio_RESERVA DE COCORA',
        'barrio_RIO CLARO',
        'barrio_RIO VERDE ',
        'barrio_ROJAS PINILLA',
        'barrio_SALVADOR ALLENDE II',
        'barrio_SAN ANDRES',
        'barrio_SAN FERNANDO',
        'barrio_SAN JOSE',
        'barrio_SAN NICOLAS',
        'barrio_SANTA FE',
        'barrio_SANTA RITA',
        'barrio_SECTOR BAVARIA',
        'barrio_SECTOR DE TRES ESQUINAS',
        'barrio_SECTOR INDUSTRIAL',
        'barrio_SECTOR PARQUE SUCRE',
        'barrio_SECTOR PARQUE VALENCIA',
        'barrio_SINAI',
        'barrio_TERRAZA JARDIN',
        'barrio_TIGREROS',
        'barrio_TORRE ALMERIA',
        'barrio_TRES ESQUINAS',
        'barrio_URB ALTOS DE LA PAVONA',
        'barrio_URB BOSQUES DE PINARES',
        'barrio_URB BOSQUES DE PINARES ',
        'barrio_URB CAMINOS DEL CALAY',
        'barrio_URB CANAS GORDAS',
        'barrio_URB CASA BLANCA',
        'barrio_URB CASTELLON',
        'barrio_URB CENTENARIO',
        'barrio_URB COINCA',
        'barrio_URB EL JUBILEO',
        'barrio_URB EL PARQUE',
        'barrio_URB GENESIS',
        'barrio_URB GUADUALES DE LA VILLA',
        'barrio_URB HACIENDA PALMACERA',
        'barrio_URB JARDIN DE LAS MERCEDES',
        'barrio_URB LA ALDEA',
        'barrio_URB LA ARCADIA',
        'barrio_URB LA ESMERALDA',
        'barrio_URB LA GRECIA',
        'barrio_URB LA LINDA',
        'barrio_URB LA MARIELA',
        'barrio_URB LA PATRIA',
        'barrio_URB LA RIVERA',
        'barrio_URB LA VIRGINIA',
        'barrio_URB LAS BRISAS',
        'barrio_URB LAS COLINAS',
        'barrio_URB LIMONAR',
        'barrio_URB LINDARAJA',
        'barrio_URB LOMA VERDE',
        'barrio_URB LOS ARCADES',
        'barrio_URB LOS GIRASOLES',
        'barrio_URB MANANTIALES',
        'barrio_URB MARIA CRISTINA',
        'barrio_URB MERCEDES DEL NORTE',
        'barrio_URB NTRA. SRA. DE LA PAZ',
        'barrio_URB PORTAL DE PINARES',
        'barrio_URB PORTAL DEL EDEN',
        'barrio_URB QUINTAS DE LA MARINA',
        'barrio_URB QUINTAS DE VILLA LILIANA',
        'barrio_URB REMANSO DE MANANTIALES',
        'barrio_URB SAN FRANCISCO',
        'barrio_URB TEJARES DEL PARQUE',
        'barrio_URB TERRANOVA EL ALBA',
        'barrio_URB VERACRUZ',
        'barrio_URB VILLA ANDREA',
        'barrio_URB VILLA CAROLINA',
        'barrio_URB VILLA CLAUDIA',
        'barrio_URB VILLA DEL CARMEN',
        'barrio_URB VILLA DEL CENTENARIO',
        'barrio_URB VILLA HERMOSA',
        'barrio_URB VILLA ITALIA',
        'barrio_URB VILLA LILIANA',
        'barrio_URB VILLA XIMENA',
        'barrio_URB VISTA HERMOSA',
        'barrio_URB YULIMA',
        'barrio_URIBE',
        'barrio_VDA EL CAIMO',
        'barrio_VDA EL RHIN',
        'barrio_VDA MURILLO',
        'barrio_VDA PADILLA',
        'barrio_VDA PTO. ESPEJO',
        'barrio_VDA SAN JUAN',
        'barrio_VDA SAN PEDRO',
        'barrio_VDA SANTA ANA',
        'barrio_VDA TIGREROS',
        'barrio_VELEZ',
        'barrio_VIA AL EDEN',
        'barrio_VIA EL CAIMO',
        'barrio_VIA TEBAIDA',
        'barrio_VILLA ALEJANDRA',
        'barrio_VILLA ANDREA I ET',
        'barrio_VILLA ESPERANZA',
        'barrio_ZULDEMAYDA',
        'uso_COMERCIAL',
        'uso_INDUSTRIAL',
        'uso_OFICIAL',
        'uso_PROVISIONAL',
        'uso_RESIDENCIAL',
        'estrato_1 - BAJO BAJO',
        'estrato_1 - COMERCIAL',
        'estrato_1 - INDUSTRIAL',
        'estrato_1 - OFICIAL',
        'estrato_1 - PROVISIONAL',
        'estrato_2 - BAJO',
        'estrato_3 - MEDIO BAJO',
        'estrato_4 - MEDIO',
        'estrato_5 - MEDIO ALTO',
        'estrato_6 - ALTO'
            ]

    # Verificar y agregar columnas faltantes
    for col in columnas_esperadas:
        if col not in datos.columns:
            result[col] = False
        else:
            result[col] = datos[col]

    return result

# Función para transformar los datos antes de la predicción
def transfor_model(datos):

    # Realizar transformaciones en los datos
    result = transfor_model_columnas(datos)

    # Agregar columnas específicas
    result['idproducto'] = datos['idproducto']
    result['ciclo'] = datos['ciclo']
    result['observacion_lectura_'+datos['observacion_lectura']] = True
    result['tipo_'+datos['tipo']] = True
    result['estado_tecnico_'+datos['estado_tecnico']] = True
    result['barrio_'+datos['barrio']] = True
    result['uso_'+datos['uso']] = True
    result['estrato_'+datos['estrato']] = True
    result['zona'] = datos['zona']
    result['anio'] = datos['anio']
    result['mes'] = datos['mes']
    result['cantidadfestivos'] = datos['cantidadfestivos']
    result['consumo_promedio'] = datos['consumo_promedio']

    return result

# Ruta de inicio que devuelve un mensaje simple
@app.get('/')
def home():
    return "Is Up!"


# Ruta para predecir el consumo
@app.post("/predecir")
def predecir_consumo(request: ConsumoRequest):
    # Convertir la solicitud a un DataFrame de pandas
    datos = pd.DataFrame([request.dict()])

    # Transformar los datos
    result = transfor_model(datos)

    # Realizar la predicción
    prediccion = modelo.predict(result)
    return {"prediccion": prediccion[0]}

# Ejecutar la aplicación uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)