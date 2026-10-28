import unittest

from validador_transferencia import ValidadorTransferencia


class TestValidadorTransferencia(unittest.TestCase):

    def setUp(self):
        self.validador = ValidadorTransferencia()

    # 1. Camino feliz
    def test_transferencia_exitosa(self):
        # Arrange
        monto, saldo, activa = 500.0, 1000.0, True

        # Act
        resultado = self.validador.validar_transferencia(monto, saldo, activa)

        # Assert
        self.assertEqual(resultado, "TRANSFERENCIA_APROBADA")

    # 2. Caso de borde: monto exactamente igual al saldo disponible
    def test_transferencia_monto_igual_al_saldo(self):
        # Arrange
        monto, saldo, activa = 1000.0, 1000.0, True

        # Act
        resultado = self.validador.validar_transferencia(monto, saldo, activa)

        # Assert
        self.assertEqual(resultado, "TRANSFERENCIA_APROBADA")

    # 3. Inyección de error: saldo insuficiente
    def test_transferencia_saldo_insuficiente(self):
        # Arrange
        monto, saldo, activa = 1500.0, 1000.0, True

        # Act
        with self.assertRaises(ValueError) as contexto:
            self.validador.validar_transferencia(monto, saldo, activa)

        # Assert
        self.assertEqual(
            str(contexto.exception),
            "Saldo insuficiente para realizar la transferencia.",
        )

    # 4. Inyección de error: monto fuera de rango (límite cero)
    def test_transferencia_monto_cero(self):
        # Arrange
        monto, saldo, activa = 0.0, 1000.0, True

        # Act
        with self.assertRaises(ValueError) as contexto:
            self.validador.validar_transferencia(monto, saldo, activa)

        # Assert
        self.assertEqual(
            str(contexto.exception), "El monto a transferir debe ser mayor a cero."
        )

    # 5. Inyección de error: monto negativo (caso extremo fuera de rango)
    def test_transferencia_monto_negativo(self):
        # Arrange
        monto, saldo, activa = -50.0, 1000.0, True

        # Act
        with self.assertRaises(ValueError) as contexto:
            self.validador.validar_transferencia(monto, saldo, activa)

        # Assert
        self.assertEqual(
            str(contexto.exception), "El monto a transferir debe ser mayor a cero."
        )

    # 6. Inyección de error: cuenta inactiva
    def test_transferencia_cuenta_inactiva(self):
        # Arrange
        monto, saldo, activa = 100.0, 1000.0, False

        # Act
        with self.assertRaises(ValueError) as contexto:
            self.validador.validar_transferencia(monto, saldo, activa)

        # Assert
        self.assertEqual(
            str(contexto.exception), "La cuenta origen se encuentra inactiva."
        )


if __name__ == "__main__":
    unittest.main()
