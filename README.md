# 🔄 Conversor Universal de Unidades

Sistema web profesional de conversión de unidades organizado por especialidades, desarrollado con Django 5.2 y arquitectura modular.

## 🎯 Características Principales

- ✅ **11 tipos de conversiones** distribuidas en 3 especialidades
- ✅ **Arquitectura modular** con patrón Strategy para conversiones
- ✅ **Interfaz moderna** con diseño oscuro profesional
- ✅ **Base de datos relacional** optimizada con Django ORM
- ✅ **Sistema extensible** para agregar nuevas conversiones

## 🏗️ Especialidades

### 🔬 Ciencias
- Temperatura (Celsius, Fahrenheit, Kelvin)
- Longitud (Metro, Kilómetro, Milla, Pulgada, etc.)
- Masa (Kilogramo, Gramo, Libra, Onza)
- Tiempo (Segundo, Minuto, Hora, Día)
- Área (Metro², Hectárea, Kilómetro²)
- Volumen (Metro³, Litro, Mililitro)
- Velocidad (m/s, km/h, mi/h)

### 💻 Informática
- Almacenamiento (Byte, KB, MB, GB, TB)

### 💰 Contabilidad
- Moneda (USD, EUR, ARS, MXN)
- IVA (Neto, Bruto, IVA)
- Porcentaje (Base, Total, Porción)

## 🚀 Instalación

```bash
# Clonar repositorio
git clone <tu-repo>
cd conversor-universal

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Ejecutar servidor
python manage.py runserver