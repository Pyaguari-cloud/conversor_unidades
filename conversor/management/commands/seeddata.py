from django.core.management.base import BaseCommand
from conversor.models import Especialidad, Magnitud, Unidad

class Command(BaseCommand):
    help = 'Carga datos de ejemplo'

    def handle(self, *args, **options):
        # Limpiar datos existentes
        self.stdout.write('Limpiando datos existentes...')
        Unidad.objects.all().delete()
        Magnitud.objects.all().delete()
        Especialidad.objects.all().delete()

        # ============ CIENCIAS ============
        self.stdout.write('Creando especialidad: Ciencias')
        ciencias = Especialidad.objects.create(
            nombre="Ciencias",
            slug="ciencias",
            descripcion="Conversiones científicas y físicas"
        )

        # Temperatura
        temp = Magnitud.objects.create(
            especialidad=ciencias,
            nombre="Temperatura",
            codigo_calculo="calc_temp"
        )
        Unidad.objects.bulk_create([
            Unidad(magnitud=temp, nombre="Celsius", simbolo="C"),
            Unidad(magnitud=temp, nombre="Fahrenheit", simbolo="F"),
            Unidad(magnitud=temp, nombre="Kelvin", simbolo="K"),
        ])

        # Longitud
        longitud = Magnitud.objects.create(
            especialidad=ciencias,
            nombre="Longitud",
            codigo_calculo="calc_longitud"
        )
        Unidad.objects.bulk_create([
            Unidad(magnitud=longitud, nombre="Metro", simbolo="m"),
            Unidad(magnitud=longitud, nombre="Kilómetro", simbolo="km"),
            Unidad(magnitud=longitud, nombre="Centímetro", simbolo="cm"),
            Unidad(magnitud=longitud, nombre="Milímetro", simbolo="mm"),
            Unidad(magnitud=longitud, nombre="Milla", simbolo="mi"),
            Unidad(magnitud=longitud, nombre="Yarda", simbolo="yd"),
            Unidad(magnitud=longitud, nombre="Pie", simbolo="ft"),
            Unidad(magnitud=longitud, nombre="Pulgada", simbolo="in"),
        ])

        # Masa
        masa = Magnitud.objects.create(
            especialidad=ciencias,
            nombre="Masa",
            codigo_calculo="calc_masa"
        )
        Unidad.objects.bulk_create([
            Unidad(magnitud=masa, nombre="Kilogramo", simbolo="kg"),
            Unidad(magnitud=masa, nombre="Gramo", simbolo="g"),
            Unidad(magnitud=masa, nombre="Miligramo", simbolo="mg"),
            Unidad(magnitud=masa, nombre="Tonelada", simbolo="t"),
            Unidad(magnitud=masa, nombre="Libra", simbolo="lb"),
            Unidad(magnitud=masa, nombre="Onza", simbolo="oz"),
        ])

        # Tiempo
        tiempo = Magnitud.objects.create(
            especialidad=ciencias,
            nombre="Tiempo",
            codigo_calculo="calc_tiempo"
        )
        Unidad.objects.bulk_create([
            Unidad(magnitud=tiempo, nombre="Segundo", simbolo="s"),
            Unidad(magnitud=tiempo, nombre="Minuto", simbolo="min"),
            Unidad(magnitud=tiempo, nombre="Hora", simbolo="h"),
            Unidad(magnitud=tiempo, nombre="Día", simbolo="d"),
            Unidad(magnitud=tiempo, nombre="Semana", simbolo="sem"),
            Unidad(magnitud=tiempo, nombre="Mes", simbolo="mes"),
            Unidad(magnitud=tiempo, nombre="Año", simbolo="año"),
        ])

        # Área
        area = Magnitud.objects.create(
            especialidad=ciencias,
            nombre="Área",
            codigo_calculo="calc_area"
        )
        Unidad.objects.bulk_create([
            Unidad(magnitud=area, nombre="Metro cuadrado", simbolo="m²"),
            Unidad(magnitud=area, nombre="Kilómetro cuadrado", simbolo="km²"),
            Unidad(magnitud=area, nombre="Hectárea", simbolo="ha"),
            Unidad(magnitud=area, nombre="Acre", simbolo="ac"),
        ])

        # Volumen
        volumen = Magnitud.objects.create(
            especialidad=ciencias,
            nombre="Volumen",
            codigo_calculo="calc_volumen"
        )
        Unidad.objects.bulk_create([
            Unidad(magnitud=volumen, nombre="Metro cúbico", simbolo="m³"),
            Unidad(magnitud=volumen, nombre="Litro", simbolo="L"),
            Unidad(magnitud=volumen, nombre="Mililitro", simbolo="mL"),
            Unidad(magnitud=volumen, nombre="Galón", simbolo="gal"),
        ])

        # Velocidad
        velocidad = Magnitud.objects.create(
            especialidad=ciencias,
            nombre="Velocidad",
            codigo_calculo="calc_velocidad"
        )
        Unidad.objects.bulk_create([
            Unidad(magnitud=velocidad, nombre="Metro por segundo", simbolo="m/s"),
            Unidad(magnitud=velocidad, nombre="Kilómetro por hora", simbolo="km/h"),
            Unidad(magnitud=velocidad, nombre="Milla por hora", simbolo="mi/h"),
            Unidad(magnitud=velocidad, nombre="Nudo", simbolo="kn"),
        ])

        # ============ INFORMÁTICA ============
        self.stdout.write('Creando especialidad: Informática')
        informatica = Especialidad.objects.create(
            nombre="Informática",
            slug="informatica",
            descripcion="Conversiones de almacenamiento digital"
        )

        bytes_mag = Magnitud.objects.create(
            especialidad=informatica,
            nombre="Almacenamiento",
            codigo_calculo="calc_bytes"
        )
        Unidad.objects.bulk_create([
            Unidad(magnitud=bytes_mag, nombre="Byte", simbolo="B"),
            Unidad(magnitud=bytes_mag, nombre="Kilobyte", simbolo="KB"),
            Unidad(magnitud=bytes_mag, nombre="Megabyte", simbolo="MB"),
            Unidad(magnitud=bytes_mag, nombre="Gigabyte", simbolo="GB"),
            Unidad(magnitud=bytes_mag, nombre="Terabyte", simbolo="TB"),
        ])

        # ============ CONTABILIDAD ============
        self.stdout.write('Creando especialidad: Contabilidad')
        contabilidad = Especialidad.objects.create(
            nombre="Contabilidad",
            slug="contabilidad",
            descripcion="Conversiones financieras y fiscales"
        )

        # Moneda
        moneda = Magnitud.objects.create(
            especialidad=contabilidad,
            nombre="Moneda",
            codigo_calculo="calc_moneda"
        )
        Unidad.objects.bulk_create([
            Unidad(magnitud=moneda, nombre="Dólar estadounidense", simbolo="USD"),
            Unidad(magnitud=moneda, nombre="Euro", simbolo="EUR"),
            Unidad(magnitud=moneda, nombre="Peso argentino", simbolo="ARS"),
            Unidad(magnitud=moneda, nombre="Peso mexicano", simbolo="MXN"),
        ])

        # IVA
        iva = Magnitud.objects.create(
            especialidad=contabilidad,
            nombre="IVA",
            codigo_calculo="calc_iva"
        )
        Unidad.objects.bulk_create([
            Unidad(magnitud=iva, nombre="Neto", simbolo="neto"),
            Unidad(magnitud=iva, nombre="Bruto", simbolo="bruto"),
            Unidad(magnitud=iva, nombre="IVA", simbolo="iva"),
        ])

        # Porcentaje
        porcentaje = Magnitud.objects.create(
            especialidad=contabilidad,
            nombre="Porcentaje",
            codigo_calculo="calc_porcentaje"
        )
        Unidad.objects.bulk_create([
            Unidad(magnitud=porcentaje, nombre="Base", simbolo="base"),
            Unidad(magnitud=porcentaje, nombre="Total", simbolo="total"),
            Unidad(magnitud=porcentaje, nombre="Porción", simbolo="porc"),
        ])

        self.stdout.write(self.style.SUCCESS('✅ Datos cargados exitosamente'))
        self.stdout.write(f'  📊 {Especialidad.objects.count()} especialidades')
        self.stdout.write(f'  📏 {Magnitud.objects.count()} magnitudes')
        self.stdout.write(f'  🔢 {Unidad.objects.count()} unidades')