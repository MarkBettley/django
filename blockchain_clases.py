import hashlib
import json
from datetime import datetime


class Wallet:
    def __init__(self, propietario, saldo=0):
        self.propietario = propietario
        self.saldo = saldo

    def crear_transaccion(
        self,
        destinatario,
        cantidad,
    ):
        if cantidad <= 0:
            raise ValueError(
                "La cantidad debe ser mayor a cero."
            )

        if cantidad > self.saldo:
            raise ValueError(
                "Saldo insuficiente."
            )

        self.saldo -= cantidad
        destinatario.saldo += cantidad

        return Transaction(
            emisor=self.propietario,
            receptor=destinatario.propietario,
            cantidad=cantidad,
        )

    def __str__(self):
        return (
            f"Wallet({self.propietario}, "
            f"saldo={self.saldo})"
        )


class Transaction:
    def __init__(
        self,
        emisor,
        receptor,
        cantidad,
    ):
        self.emisor = emisor
        self.receptor = receptor
        self.cantidad = cantidad
        self.fecha = datetime.now().isoformat()

    def to_dict(self):
        return {
            "emisor": self.emisor,
            "receptor": self.receptor,
            "cantidad": self.cantidad,
            "fecha": self.fecha,
        }


class Block:
    def __init__(
        self,
        indice,
        transacciones,
        hash_anterior="0",
    ):
        self.indice = indice
        self.timestamp = datetime.now().isoformat()
        self.transacciones = transacciones
        self.hash_anterior = hash_anterior
        self.hash = self.calcular_hash()

    def calcular_hash(self):
        datos_bloque = {
            "indice": self.indice,
            "timestamp": self.timestamp,
            "transacciones": [
                transaccion.to_dict()
                for transaccion
                in self.transacciones
            ],
            "hash_anterior": self.hash_anterior,
        }

        bloque_json = json.dumps(
            datos_bloque,
            sort_keys=True,
        )

        return hashlib.sha256(
            bloque_json.encode()
        ).hexdigest()


class Blockchain:
    def __init__(self):
        self.bloques = []

    def agregar_bloque(self, bloque):
        if self.bloques:
            bloque.hash_anterior = (
                self.bloques[-1].hash
            )

            bloque.hash = (
                bloque.calcular_hash()
            )

        self.bloques.append(bloque)

    def es_valida(self):
        for indice in range(
            1,
            len(self.bloques),
        ):
            bloque_actual = (
                self.bloques[indice]
            )

            bloque_anterior = (
                self.bloques[indice - 1]
            )

            if (
                bloque_actual.hash_anterior
                != bloque_anterior.hash
            ):
                return False

            if (
                bloque_actual.hash
                != bloque_actual.calcular_hash()
            ):
                return False

        return True

    def mostrar(self):
        for bloque in self.bloques:
            print(
                f"\nBLOQUE {bloque.indice}"
            )
            print(
                f"Hash: {bloque.hash}"
            )
            print(
                "Hash anterior: "
                f"{bloque.hash_anterior}"
            )

            print("Transacciones:")

            for transaccion in (
                bloque.transacciones
            ):
                print(
                    f"  {transaccion.emisor}"
                    f" -> "
                    f"{transaccion.receptor}"
                    f": "
                    f"${transaccion.cantidad}"
                )
