# LIM Serial - Comunicación Serie & Visualización de Datos

**README en:** [English](../README.md) | [Português](README_pt-br.md) | [Español](README_es.md) | [Deutsch](README_de.md) | [Français](README_fr.md)

---

## Resumen

LIM Serial es una aplicación fácil de usar para comunicación serie y visualización de datos en tiempo real. Conéctate a Arduino u otros dispositivos serie, recopila datos y crea gráficos dinámicos con características de visualización profesionales. Disponible en 5 idiomas con guardado automático de preferencias.

![LIM Serial Screenshot](shot.png)

![LIM Serial Screenshot](shot_stacked.png)

## Características

### 🌍 **Múltiples Idiomas**
- Disponible en inglés, portugués, español, alemán y francés
- Cambiar idioma desde el menú (requiere reinicio)
- Todas las configuraciones preservadas al cambiar idiomas

### 📡 **Conexión Serie Fácil**
- Conectar a dispositivos serie reales (Arduino, sensores, etc.)
- Modo de simulación integrado para pruebas sin hardware
- Detección automática de puertos con actualización de un clic
- Compatibilidad completa con velocidades de baudios del IDE de Arduino (300-2000000 bps)

### 📊 **Visualización de Datos Profesional**
- **Gráficos de Series Temporales**: Grafica hasta 5 columnas de datos simultáneamente
- **Gráficos de Área Apilada**: Compara datos como valores absolutos o porcentajes
- **Apariencia Personalizable**: Elige colores, marcadores y tipos de línea para cada serie de datos
- **Actualizaciones en Tiempo Real**: Tasas de actualización configurables (1-30 FPS)
- **Exportación**: Guarda gráficos como imágenes PNG de alta calidad
- **Controles Interactivos**: Pausa/reanuda recopilación de datos, zoom y desplazamiento

### 💾 **Gestión Inteligente de Datos**
- **Guardar/Cargar Manual**: Exporta e importa tus datos en cualquier momento
- **Respaldo Automático**: Guardado automático opcional con nombres de archivo con marca de tiempo
- **Seguridad de Datos**: Limpia datos con confirmaciones
- **Todas las Configuraciones Guardadas**: Preferencias automáticamente preservadas entre sesiones

## Primeros Pasos

### Requisitos
- Python 3.7 o más reciente
- Conexión a internet para instalación de dependencias

### Instalación
```bash
# Instalar paquetes requeridos
pip install matplotlib pyserial PyYAML

# Descargar y ejecutar lim_bal
cd limbal00
python lim_bal.py
```

### Primeros Pasos
1. **Idioma**: Elige tu idioma del menú Idioma
2. **Conexión**: Ve a la pestaña Configuración, selecciona tu puerto serie y velocidad de baudios
3. **Datos**: Cambia a la pestaña Datos para ver datos entrantes
4. **Visualización**: Usa la pestaña Gráfico para crear gráficos de tus datos

## Cómo Usar

### Pestaña Configuración
- **Modo**: Elige "Hardware" para dispositivos reales, "Simulado" para pruebas
- **Puerto**: Selecciona tu puerto serie (haz clic en Actualizar para actualizar la lista)
- **Velocidad de Baudios**: Establece la velocidad de comunicación (coincide con la configuración de tu dispositivo)
- **Conectar**: Haz clic para comenzar a recibir datos

### Pestaña Datos
- **Ver Datos**: Ve datos entrantes en formato de tabla en tiempo real
- **Guardar Datos**: Exporta datos actuales a un archivo de texto
- **Cargar Datos**: Importa archivos de datos guardados previamente
- **Limpiar Datos**: Reinicia el conjunto de datos actual (con confirmación)
- **Guardado Automático**: Activa/desactiva respaldo automático con nombres de archivo con marca de tiempo

### Pestaña Gráfico
- **Elegir Columnas**: Selecciona eje X y hasta 5 columnas de eje Y de tus datos
- **Tipos de Gráfico**:
  - **Series Temporales**: Gráficos de línea/dispersión individuales para cada serie de datos
  - **Área Apilada**: Gráficos en capas mostrando datos acumulativos o porcentajes
- **Personalizar**: Expande "Mostrar Opciones Avanzadas" para cambiar colores, marcadores, tasa de actualización
- **Exportar**: Guarda tus gráficos como imágenes PNG
- **Control**: Pausa/reanuda actualizaciones en tiempo real en cualquier momento

### Menú Idioma
- **Cambiar Idioma**: Selecciona entre 5 idiomas disponibles
- **Reinicio Requerido**: La aplicación te pedirá reiniciar para el cambio de idioma
- **Configuraciones Preservadas**: Todas tus preferencias se mantienen al cambiar idiomas

## Formato de Datos

Tu dispositivo serie debe enviar datos en formato de texto simple:

```
# Línea de encabezado opcional
timestamp voltage current temperature

# Filas de datos (separadas por espacio o tabulación)
1.0 3.3 0.125 25.4
2.0 3.2 0.130 25.6
3.0 3.4 0.122 25.2
```

**Formatos soportados:**
- Columnas separadas por espacio o tabulación
- Números en cualquier columna
- Fila de encabezado opcional (será detectada automáticamente)
- Transmisión en tiempo real o carga de datos por lotes

## Solución de Problemas

**Problemas de Conexión:**
- Asegúrate de que tu dispositivo esté conectado y encendido
- Verifica que ningún otro programa esté usando el puerto serie
- Prueba diferentes velocidades de baudios si los datos aparecen corruptos
- Usa el modo Simulado para probar la interfaz sin hardware

**Problemas de Datos:**
- Asegúrate de que los datos estén separados por espacio o tabulación
- Verifica que los números estén en formato estándar (usa . para decimales)
- Verifica que tu dispositivo esté enviando datos continuamente
- Prueba guardar y recargar datos para verificar el formato

**Rendimiento:**
- Reduce la tasa de actualización si los gráficos son lentos
- Reduce el tamaño de la ventana de datos para mejor rendimiento
- Cierra otros programas si el sistema se vuelve lento

## Desarrollo

Esta aplicación está construida con Python y usa tkinter para la interfaz y matplotlib para gráficos.

**Para desarrolladores:**
- La base de código usa una arquitectura modular con componentes separados para GUI, gestión de datos y visualización
- Las traducciones se almacenan en archivos YAML en el directorio `languages/`
- La configuración usa un sistema de preferencias jerárquico guardado en `config/prefs.yml`
- El sistema de actualización de gráficos está desacoplado de la llegada de datos para rendimiento óptimo

## Licencia

Desarrollado por CBPF-LIM (Centro Brasileño de Investigación en Física - Laboratorio de Luz y Materia).

---

**LIM Serial** - Comunicación serie y visualización de datos profesionales simplificadas.