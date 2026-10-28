class ValidadorTransferencia:
    def validar_transferencia(self, monto, saldo_disponible, cuenta_activa):
        if not cuenta_activa:
            raise ValueError("La cuenta origen se encuentra inactiva.")
        if monto <= 0:
            raise ValueError("El monto a transferir debe ser mayor a cero.")
        if monto > saldo_disponible:
            raise ValueError("Saldo insuficiente para realizar la transferencia.")
        return "TRANSFERENCIA_APROBADA"
