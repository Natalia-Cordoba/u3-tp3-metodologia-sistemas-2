TASAS = {
    "VIP": {"web": 0.002, "app": 0.003, "sucursal": 0.005},
    "ESTANDAR": {"web": 0.005, "app": 0.006, "sucursal": 0.01},
}


def obtener_tasa(tipo_cliente, canal):
    if tipo_cliente not in TASAS:
        raise ValueError("Tipo de cliente inválido")
    if canal not in TASAS[tipo_cliente]:
        raise ValueError("Canal inválido")
    return TASAS[tipo_cliente][canal]


def comision_transferencia(tipo_cliente, canal, monto, es_feriado):
    comision = monto * obtener_tasa(tipo_cliente, canal)
    if es_feriado:
        comision *= 1.5
    if monto > 100000:
        comision *= 0.9
    return comision


def comision_transferencia_programada(tipo_cliente, canal, monto, es_feriado):
    return comision_transferencia(tipo_cliente, canal, monto, es_feriado) * 0.8
