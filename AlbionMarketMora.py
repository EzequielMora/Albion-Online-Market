import requests
from bs4 import BeautifulSoup
from datetime import datetime, timezone
from itertools import groupby

# URL de la API
url = 'https://west.albion-online-data.com/api/v2/stats/view/T8_CAPEITEM_UNDEAD,T8_CAPEITEM_UNDEAD@1,T8_CAPEITEM_UNDEAD@2,T8_CAPEITEM_UNDEAD@3,T8_CAPEITEM_UNDEAD@4,T8_CAPEITEM_FW_LYMHURST,T8_CAPEITEM_FW_LYMHURST@1,T8_CAPEITEM_FW_LYMHURST@2,T8_CAPEITEM_FW_LYMHURST@3,T8_CAPEITEM_FW_LYMHURST@4,T8_CAPEITEM_AVALON,T8_CAPEITEM_AVALON@1,T8_CAPEITEM_AVALON@2,T8_CAPEITEM_AVALON@3,T8_CAPEITEM_AVALON@4,T8_CAPEITEM_MORGANA,T8_CAPEITEM_MORGANA@1,T8_CAPEITEM_MORGANA@2,T8_CAPEITEM_MORGANA@3,T8_CAPEITEM_MORGANA@4,T8_CAPEITEM_FW_BRECILIEN,T8_CAPEITEM_FW_BRECILIEN@1,T8_CAPEITEM_FW_BRECILIEN@2,T8_CAPEITEM_FW_BRECILIEN@3,T8_CAPEITEM_FW_BRECILIEN@4,T8_CAPEITEM_FW_CAERLEON,T8_CAPEITEM_FW_CAERLEON@1,T8_CAPEITEM_FW_CAERLEON@2,T8_CAPEITEM_FW_CAERLEON@3,T8_CAPEITEM_FW_CAERLEON@4,T8_CAPEITEM_KEEPER,T8_CAPEITEM_KEEPER@1,T8_CAPEITEM_KEEPER@2,T8_CAPEITEM_KEEPER@3,T8_CAPEITEM_KEEPER@4,T8_HEAD_LEATHER_UNDEAD,T8_HEAD_LEATHER_UNDEAD@1,T8_HEAD_LEATHER_UNDEAD@2,T8_HEAD_LEATHER_UNDEAD@3,T8_HEAD_LEATHER_UNDEAD@4,T8_OFF_LAMP_UNDEAD,T8_OFF_LAMP_UNDEAD@1,T8_OFF_LAMP_UNDEAD@2,T8_OFF_LAMP_UNDEAD@3,T8_OFF_LAMP_UNDEAD@4,T8_ARMOR_CLOTH_FEY,T8_ARMOR_CLOTH_FEY@1,T8_ARMOR_CLOTH_FEY@2,T8_ARMOR_CLOTH_FEY@3,T8_ARMOR_CLOTH_FEY@4,T8_ARMOR_PLATE_ROYAL,T8_ARMOR_PLATE_ROYAL@1,T8_ARMOR_PLATE_ROYAL@2,T8_ARMOR_PLATE_ROYAL@3,T8_ARMOR_PLATE_ROYAL@4,T8_SHOES_LEATHER_ROYAL,T8_SHOES_LEATHER_ROYAL@1,T8_SHOES_LEATHER_ROYAL@2,T8_SHOES_LEATHER_ROYAL@3,T8_SHOES_LEATHER_ROYAL@4,T8_SHOES_PLATE_AVALON,T8_SHOES_PLATE_AVALON@1,T8_SHOES_PLATE_AVALON@2,T8_SHOES_PLATE_AVALON@3,T8_SHOES_PLATE_AVALON@4,T8_HEAD_CLOTH_ROYAL,T8_HEAD_CLOTH_ROYAL@1,T8_HEAD_CLOTH_ROYAL@2,T8_HEAD_CLOTH_ROYAL@3,T8_HEAD_CLOTH_ROYAL@4,T8_HEAD_CLOTH_AVALON,T8_HEAD_CLOTH_AVALON@1,T8_HEAD_CLOTH_AVALON@2,T8_HEAD_CLOTH_AVALON@3,T8_HEAD_CLOTH_AVALON@4,T8_ARMOR_LEATHER_ROYAL,T8_ARMOR_LEATHER_ROYAL@1,T8_ARMOR_LEATHER_ROYAL@2,T8_ARMOR_LEATHER_ROYAL@3,T8_ARMOR_LEATHER_ROYAL@4,T8_ARMOR_LEATHER_FEY,T8_ARMOR_LEATHER_FEY@1,T8_ARMOR_LEATHER_FEY@2,T8_ARMOR_LEATHER_FEY@3,T8_ARMOR_LEATHER_FEY@4,T8_SHOES_PLATE_ROYAL,T8_SHOES_PLATE_ROYAL@1,T8_SHOES_PLATE_ROYAL@2,T8_SHOES_PLATE_ROYAL@3,T8_SHOES_PLATE_ROYAL@4,T8_HEAD_PLATE_ROYAL,T8_HEAD_PLATE_ROYAL@1,T8_HEAD_PLATE_ROYAL@2,T8_HEAD_PLATE_ROYAL@3,T8_HEAD_PLATE_ROYAL@4,T8_SHOES_CLOTH_FEY,T8_SHOES_CLOTH_FEY@1,T8_SHOES_CLOTH_FEY@2,T8_SHOES_CLOTH_FEY@3,T8_SHOES_CLOTH_FEY@4,T8_SHOES_CLOTH_AVALON,T8_SHOES_CLOTH_AVALON@1,T8_SHOES_CLOTH_AVALON@2,T8_SHOES_CLOTH_AVALON@3,T8_SHOES_CLOTH_AVALON@4,T8_BAG_INSIGHT,T8_BAG_INSIGHT@1,T8_BAG_INSIGHT@2,T8_BAG_INSIGHT@3,T8_BAG_INSIGHT@4,T8_OFF_SPIKEDSHIELD_MORGANA,T8_OFF_SPIKEDSHIELD_MORGANA@1,T8_OFF_SPIKEDSHIELD_MORGANA@2,T8_OFF_SPIKEDSHIELD_MORGANA@3,T8_OFF_SPIKEDSHIELD_MORGANA@4,T8_2H_QUARTERSTAFF,T8_2H_QUARTERSTAFF@1,T8_2H_QUARTERSTAFF@2,T8_2H_QUARTERSTAFF@3,T8_2H_QUARTERSTAFF@4,T8_SHOES_CLOTH_MORGANA,T8_SHOES_CLOTH_MORGANA@1,T8_SHOES_CLOTH_MORGANA@2,T8_SHOES_CLOTH_MORGANA@3,T8_SHOES_CLOTH_MORGANA@4,T8_SHOES_CLOTH_ROYAL,T8_SHOES_CLOTH_ROYAL@1,T8_SHOES_CLOTH_ROYAL@2,T8_SHOES_CLOTH_ROYAL@3,T8_SHOES_CLOTH_ROYAL@4,T8_SHOES_LEATHER_AVALON,T8_SHOES_LEATHER_AVALON@1,T8_SHOES_LEATHER_AVALON@2,T8_SHOES_LEATHER_AVALON@3,T8_SHOES_LEATHER_AVALON@4?locations=BlackMarket,Lymhurst&qualities=0'  
response = requests.get(url)
print(f"Código de estado de la respuesta: {response.status_code}")
if response.status_code != 200:
    print("Error al conectar con la API.")
    exit()

# Analizar el contenido de la página
soup = BeautifulSoup(response.content, 'html.parser')
rows = soup.find_all('tr')

if not rows:
    print("No se encontraron filas en el HTML.")
    exit()

# Obtener la hora actual en UTC
hora_actual = datetime.now(timezone.utc)

# Estructuras para almacenar datos
tiempos_actualizacion = {"BlackMarket": [], "Lymhurst": []}
precios = {"BlackMarket": {}, "Lymhurst": {}}
beneficios = []

# Procesar las filas del HTML
for row in rows[1:]:
    cols = row.find_all('td')
    if len(cols) < 11:  # Verifica que haya suficientes columnas
        print(f"Fila con columnas insuficientes: {cols}")
        continue

    try:
        item_id = cols[0].text.strip()
        city = cols[1].text.strip()
        quality = cols[2].text.strip()

        buy_price_max_date = cols[10].text.strip() if len(cols) > 10 else None
        sell_price_min_date = cols[4].text.strip() if len(cols) > 4 else None
        buy_price_max = int(cols[9].text.strip()) if cols[9].text.strip() else None
        sell_price_min = int(cols[3].text.strip()) if cols[3].text.strip() else None

        # Procesar las fechas y calcular tiempo transcurrido
        if city == "Black Market" and buy_price_max_date:
            fecha_actualizacion = datetime.fromisoformat(buy_price_max_date).replace(tzinfo=timezone.utc)
            tiempo_transcurrido = hora_actual - fecha_actualizacion
            minutos = int(tiempo_transcurrido.total_seconds() / 60)
            tiempos_actualizacion["BlackMarket"].append((item_id, quality, minutos))
            precios["BlackMarket"][(item_id, quality)] = buy_price_max

        if city == "Lymhurst" and sell_price_min_date:
            fecha_actualizacion = datetime.fromisoformat(sell_price_min_date).replace(tzinfo=timezone.utc)
            tiempo_transcurrido = hora_actual - fecha_actualizacion
            minutos = int(tiempo_transcurrido.total_seconds() / 60)
            tiempos_actualizacion["Lymhurst"].append((item_id, quality, minutos))
            precios["Lymhurst"][(item_id, quality)] = sell_price_min

    except Exception as e:
        print(f"Error procesando fila: {cols}, Error: {e}")

# Comparar datos y calcular beneficios
procesados = set()

for item_id, quality_black, mins_black in tiempos_actualizacion["BlackMarket"]:
    for item_id_lym, quality_lym, mins_lym in tiempos_actualizacion["Lymhurst"]:
        try:
            if item_id == item_id_lym and int(quality_lym) > int(quality_black):
                clave_procesada = (item_id, quality_black, quality_lym)

                if clave_procesada in procesados:
                    continue
                procesados.add(clave_procesada)

                price_black = precios["BlackMarket"].get((item_id, quality_black))
                price_lym = precios["Lymhurst"].get((item_id_lym, quality_lym))



                beneficio = (price_black - price_lym) * 0.96
                if beneficio > 0:
                    beneficios.append((item_id, quality_black, quality_lym, mins_lym, mins_black, price_black, price_lym, beneficio))
        except Exception as e:
            print(f"Error comparando: {item_id} {quality_black} con {item_id_lym} {quality_lym}, Error: {e}")

# Ordenar por item_id y beneficio (descendente)
beneficios_ordenados = sorted(beneficios, key=lambda x: (x[0], -x[7]))

# Filtrar el mejor beneficio por item_id
mejores_beneficios = []
for item_id, grupo in groupby(beneficios_ordenados, key=lambda x: x[0]):
    mejores_beneficios.append(max(grupo, key=lambda x: x[7]))

# Ordenar los mejores beneficios de menor a mayor
mejores_beneficios_ordenados = sorted(mejores_beneficios, key=lambda x: x[7])

# Calcular porcentaje de diferencia
porcentaje_diferencia = ((price_black - price_lym) / price_black) * 100

# Calcular porcentaje de diferencia solo para Lymhurst
porcentaje_diferencia_lym = ((price_black - price_lym) / price_lym) * 100

# Iteración sobre los productos
for item_id, quality_black, quality_lym, mins_lym, mins_black, price_black, price_lym, beneficio in mejores_beneficios_ordenados:
    # Calcular porcentaje de diferencia solo para Lymhurst en cada iteración
    porcentaje_diferencia_lym = ((price_black - price_lym) / price_lym) * 100
    
    minutos_black_color = f'\033[91m{mins_black} mins\033[0m' if mins_black > 30 else f'\033[92m{mins_black} mins\033[0m'
    minutos_lym_color = f'\033[91m{mins_lym} mins\033[0m' if mins_lym > 30 else f'\033[92m{mins_lym} mins\033[0m'

    print(f'''{item_id} (BM Cali {quality_black} vs Lym Cali {quality_lym})
    PB({price_black}) - PL({price_lym}) = Profit: \033[92m${beneficio:.0f}\033[0m \033[93m{porcentaje_diferencia_lym:.2f}%\033[0m 
    B({minutos_black_color})  L({minutos_lym_color})''')
