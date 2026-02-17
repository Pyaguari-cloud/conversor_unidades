"""
Módulo central de lógica de conversión.
"""

from decimal import Decimal, InvalidOperation


# ========== TEMPERATURA ==========
def calc_temp(valor: float, unidad_origen: str, unidad_destino: str) -> float:
    """
    Conversión de temperatura entre: C, F, K.
    """
    v = float(valor)

    # a Celsius
    if unidad_origen == "C":
        c = v
    elif unidad_origen == "F":
        c = (v - 32) * 5.0 / 9.0
    elif unidad_origen == "K":
        c = v - 273.15
    else:
        raise ValueError(f"Unidad de temperatura origen no soportada: {unidad_origen}")

    # de Celsius a destino
    if unidad_destino == "C":
        return c
    elif unidad_destino == "F":
        return c * 9.0 / 5.0 + 32
    elif unidad_destino == "K":
        return c + 273.15
    else:
        raise ValueError(f"Unidad de temperatura destino no soportada: {unidad_destino}")


# ========== LONGITUD ==========
def calc_longitud(valor: float, unidad_origen: str, unidad_destino: str) -> float:
    """
    Longitud: m, km, cm, mm, in, ft, yd, mi
    """
    v = float(valor)

    factores_m = {
        "m": 1.0,
        "km": 1000.0,
        "cm": 0.01,
        "mm": 0.001,
        "in": 0.0254,
        "ft": 0.3048,
        "yd": 0.9144,
        "mi": 1609.344,
    }

    try:
        en_m = v * factores_m[unidad_origen]
    except KeyError:
        raise ValueError(f"Unidad de longitud origen no soportada: {unidad_origen}")

    try:
        return en_m / factores_m[unidad_destino]
    except KeyError:
        raise ValueError(f"Unidad de longitud destino no soportada: {unidad_destino}")


# ========== MASA ==========
def calc_masa(valor: float, unidad_origen: str, unidad_destino: str) -> float:
    """
    Masa: g, kg, mg, lb, oz
    """
    v = float(valor)

    factores_kg = {
        "kg": 1.0,
        "g": 0.001,
        "mg": 0.000001,
        "lb": 0.45359237,
        "oz": 0.028349523125,
    }

    try:
        en_kg = v * factores_kg[unidad_origen]
    except KeyError:
        raise ValueError(f"Unidad de masa origen no soportada: {unidad_origen}")

    try:
        return en_kg / factores_kg[unidad_destino]
    except KeyError:
        raise ValueError(f"Unidad de masa destino no soportada: {unidad_destino}")


# ========== TIEMPO ==========
def calc_tiempo(valor: float, unidad_origen: str, unidad_destino: str) -> float:
    """
    Tiempo: s, min, h, dia
    """
    v = float(valor)

    factores_s = {
        "s": 1.0,
        "min": 60.0,
        "h": 3600.0,
        "dia": 86400.0,
    }

    try:
        en_s = v * factores_s[unidad_origen]
    except KeyError:
        raise ValueError(f"Unidad de tiempo origen no soportada: {unidad_origen}")

    try:
        return en_s / factores_s[unidad_destino]
    except KeyError:
        raise ValueError(f"Unidad de tiempo destino no soportada: {unidad_destino}")


# ========== ÁREA ==========
def calc_area(valor: float, unidad_origen: str, unidad_destino: str) -> float:
    """
    Área: m2, cm2, mm2, km2, ha
    """
    v = float(valor)

    factores_m2 = {
        "m2": 1.0,
        "cm2": 0.0001,
        "mm2": 0.000001,
        "km2": 1_000_000.0,
        "ha": 10_000.0,
    }

    try:
        en_m2 = v * factores_m2[unidad_origen]
    except KeyError:
        raise ValueError(f"Unidad de área origen no soportada: {unidad_origen}")

    try:
        return en_m2 / factores_m2[unidad_destino]
    except KeyError:
        raise ValueError(f"Unidad de área destino no soportada: {unidad_destino}")


# ========== VOLUMEN ==========
def calc_volumen(valor: float, unidad_origen: str, unidad_destino: str) -> float:
    """
    Volumen: m3, L, mL, cm3
    """
    v = float(valor)

    factores_m3 = {
        "m3": 1.0,
        "L": 0.001,
        "mL": 0.000001,
        "cm3": 0.000001,
    }

    try:
        en_m3 = v * factores_m3[unidad_origen]
    except KeyError:
        raise ValueError(f"Unidad de volumen origen no soportada: {unidad_origen}")

    try:
        return en_m3 / factores_m3[unidad_destino]
    except KeyError:
        raise ValueError(f"Unidad de volumen destino no soportada: {unidad_destino}")


# ========== VELOCIDAD ==========
def calc_velocidad(valor: float, unidad_origen: str, unidad_destino: str) -> float:
    """
    Velocidad: m_s, km_h, mi_h
    """
    v = float(valor)

    # a m/s
    if unidad_origen == "m_s":
        ms = v
    elif unidad_origen == "km_h":
        ms = v * 1000.0 / 3600.0
    elif unidad_origen == "mi_h":
        ms = v * 1609.344 / 3600.0
    else:
        raise ValueError(f"Unidad de velocidad origen no soportada: {unidad_origen}")

    # a destino
    if unidad_destino == "m_s":
        return ms
    elif unidad_destino == "km_h":
        return ms * 3.6
    elif unidad_destino == "mi_h":
        return ms * 3600.0 / 1609.344
    else:
        raise ValueError(f"Unidad de velocidad destino no soportada: {unidad_destino}")


# ========== ALMACENAMIENTO / INFORMÁTICA ==========
def calc_bytes(valor: float, unidad_origen: str, unidad_destino: str) -> float:
    """
    Almacenamiento (base 1024): B, KB, MB, GB, TB
    """
    v = float(valor)

    factores = {
        "B": 1,
        "KB": 1024,
        "MB": 1024 ** 2,
        "GB": 1024 ** 3,
        "TB": 1024 ** 4,
    }

    try:
        en_bytes = v * factores[unidad_origen]
    except KeyError:
        raise ValueError(f"Unidad de almacenamiento origen no soportada: {unidad_origen}")

    try:
        return en_bytes / factores[unidad_destino]
    except KeyError:
        raise ValueError(f"Unidad de almacenamiento destino no soportada: {unidad_destino}")


# ========== MONEDA / CONTABILIDAD (tipo cambio fijo) ==========
def calc_moneda(valor: float, unidad_origen: str, unidad_destino: str) -> float:
    """
    Conversión de moneda con tasas fijas de ejemplo.
    """
    v = Decimal(str(valor))

    tasas_vs_usd = {
        "USD": Decimal("1"),
        "EUR": Decimal("1.08"),
        "ARS": Decimal("0.0012"),
        "MXN": Decimal("0.058"),
    }

    if unidad_origen not in tasas_vs_usd:
        raise ValueError(f"Moneda origen no soportada: {unidad_origen}")
    if unidad_destino not in tasas_vs_usd:
        raise ValueError(f"Moneda destino no soportada: {unidad_destino}")

    a_usd = v / tasas_vs_usd[unidad_origen]
    resultado = a_usd * tasas_vs_usd[unidad_destino]
    return float(resultado)


# ========== IVA / IMPUESTOS ==========
def calc_iva(valor: float, unidad_origen: str, unidad_destino: str) -> float:
    """
    unidad: 'neto', 'bruto', 'iva'
    tasa fija 21%.
    """
    tasa = Decimal("0.21")

    try:
        base = Decimal(str(valor))
    except InvalidOperation:
        raise ValueError("Valor inválido para IVA")

    if unidad_origen == "neto":
        neto = base
        iva = neto * tasa
        bruto = neto + iva
    elif unidad_origen == "bruto":
        bruto = base
        neto = bruto / (Decimal("1") + tasa)
        iva = bruto - neto
    elif unidad_origen == "iva":
        iva = base
        neto = iva / tasa
        bruto = neto + iva
    else:
        raise ValueError(f"Tipo origen IVA no soportado: {unidad_origen}")

    if unidad_destino == "neto":
        return float(neto)
    elif unidad_destino == "bruto":
        return float(bruto)
    elif unidad_destino == "iva":
        return float(iva)
    else:
        raise ValueError(f"Tipo destino IVA no soportado: {unidad_destino}")


# ========== PORCENTAJE GENÉRICO ==========
def calc_porcentaje(valor: float, unidad_origen: str, unidad_destino: str) -> float:
    """
    'base', 'total', 'porc' con tasa fija 10% (demo).
    """
    tasa = Decimal("0.10")
    base = Decimal(str(valor))

    if unidad_origen == "base":
        base_val = base
        porc_val = base_val * tasa
        total_val = base_val + porc_val
    elif unidad_origen == "total":
        total_val = base
        base_val = total_val / (Decimal("1") + tasa)
        porc_val = total_val - base_val
    elif unidad_origen == "porc":
        porc_val = base
        base_val = porc_val / tasa
        total_val = base_val + porc_val
    else:
        raise ValueError(f"Tipo origen porcentaje no soportado: {unidad_origen}")

    if unidad_destino == "base":
        return float(base_val)
    elif unidad_destino == "total":
        return float(total_val)
    elif unidad_destino == "porc":
        return float(porc_val)
    else:
        raise ValueError(f"Tipo destino porcentaje no soportado: {unidad_destino}")


# ========== REGISTRO CENTRAL ==========
CONVERSION_FUNCTIONS = {
    "calc_temp": calc_temp,
    "calc_longitud": calc_longitud,
    "calc_masa": calc_masa,
    "calc_tiempo": calc_tiempo,
    "calc_area": calc_area,
    "calc_volumen": calc_volumen,
    "calc_velocidad": calc_velocidad,
    "calc_bytes": calc_bytes,
    "calc_moneda": calc_moneda,
    "calc_iva": calc_iva,
    "calc_porcentaje": calc_porcentaje,
}


# ========== FUNCIÓN GENÉRICA ==========
def convertir_valor(
    codigo_calculo: str,
    valor: float,
    unidad_origen: str,
    unidad_destino: str,
) -> float:
    func = CONVERSION_FUNCTIONS.get(codigo_calculo)
    if func is None:
        raise ValueError(
            f"No hay función registrada para el código de cálculo: {codigo_calculo}"
        )
    return func(valor, unidad_origen, unidad_destino)