class CuentaBancaria:
    """Representa una cuenta bancaria."""

    def __init__(self, titular, saldo=0):
        """Inicializa una cuenta bancaria con un titular y un saldo (por defecto 0)."""
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        """Deposita dinero en la cuenta."""
        self.saldo += monto
        print(f"Se han depositado ${monto}. Saldo actual: ${self.saldo}.")

    def retirar(self, monto):
        """Retira dinero de la cuenta si hay saldo suficiente."""
        if monto <= self.saldo:
            self.saldo -= monto
            print(f"Se han retirado ${monto}. Saldo actual: ${self.saldo}.")
        else:
            print(f"Fondos insuficientes. Saldo actual: ${self.saldo}.")


# Ejemplo de uso del sistema de gestión de cuentas bancarias
cuenta1 = CuentaBancaria("Luis Gómez", 500)  # Creamos una cuenta para Luis Gómez con un saldo inicial de 500
cuenta1.depositar(200)  # Depositamos 200 en la cuenta
cuenta1.retirar(100)  # Retiramos 100 de la cuenta
cuenta1.retirar(700)  # Intentamos retirar 700, pero hay fondos insuficientes