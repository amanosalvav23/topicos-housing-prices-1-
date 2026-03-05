import pandas as pd
import matplotlib.pyplot as plt
import os

# 1. Configurar rutas
csv_path = 'datalake/data/housing.csv' 
output_dir = 'anexos'

# Crear la carpeta anexos si no existe
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

if not os.path.exists(csv_path):
    print(f"❌ Error: No se encontró el archivo en {csv_path}")
else:
    # 2. Cargar los datos
    df = pd.read_csv(csv_path)

    # 3. Crear la visualización
    plt.figure(figsize=(10, 8))
    scatter = plt.scatter(df['longitude'], df['latitude'], alpha=0.4,
                          s=df['population']/100, label='Población',
                          c=df['median_house_value'], cmap=plt.get_cmap('jet'))

    # 4. Configuración estética
    plt.colorbar(scatter, label='Valor Medio de la Vivienda ($)')
    plt.xlabel('Longitud')
    plt.ylabel('Latitud')
    plt.title('Densidad de Precios en California')
    plt.legend()
    
    # 5. Guardar dentro de la carpeta 'anexos'
    output_path = os.path.join(output_dir, 'mapa_calor_california.png')
    plt.savefig(output_path, bbox_inches='tight', dpi=300)
    
    print(f"✅ ¡Mapa generado con éxito en: {output_path}!")