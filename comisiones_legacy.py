def comision_transferencia(tipo_cliente, canal, monto, es_feriado):
    if tipo_cliente == "VIP":
        if canal == "web":
            tasa = 0.002
        elif canal == "app":
            tasa = 0.003
        elif canal == "sucursal":
            tasa = 0.005
        else:
            raise ValueError("Canal inválido")
    elif tipo_cliente == "ESTANDAR":
        if canal == "web":
            tasa = 0.005
        elif canal == "app":
            tasa = 0.006
        elif canal == "sucursal":
            tasa = 0.01
        else:
            raise ValueError("Canal inválido")
    else:
        raise ValueError("Tipo de cliente inválido")

    comision = monto * tasa
    if es_feriado:
        comision = comision * 1.5
    if monto > 100000:
        comision = comision * 0.9
    return comision


def comision_transferencia_programada(tipo_cliente, canal, monto, es_feriado):
    # Duplicación idéntica del bloque anterior
    if tipo_cliente == "VIP":
        if canal == "web":
            tasa = 0.002
        elif canal == "app":
            tasa = 0.003
        elif canal == "sucursal":
            tasa = 0.005
        else:
            raise ValueError("Canal inválido")
    elif tipo_cliente == "ESTANDAR":
        if canal == "web":
            tasa = 0.005
        elif canal == "app":
            tasa = 0.006
        elif canal == "sucursal":
            tasa = 0.01
        else:
            raise ValueError("Canal inválido")
    else:
        raise ValueError("Tipo de cliente inválido")

    comision = monto * tasa
    if es_feriado:
        comision = comision * 1.5
    if monto > 100000:
        comision = comision * 0.9
    return comision * 0.8
