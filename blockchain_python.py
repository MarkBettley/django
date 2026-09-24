from blockchain_clases import (
    Wallet,
    Block,
    Blockchain,
)


# Crear distintas wallets
wallet_marco = Wallet(
    "Marco",
    1000,
)

wallet_ana = Wallet(
    "Ana",
    800,
)

wallet_carlos = Wallet(
    "Carlos",
    600,
)

wallet_laura = Wallet(
    "Laura",
    500,
)


# Crear una instancia de Blockchain
blockchain = Blockchain()


# BLOQUE 1
transaccion_1 = (
    wallet_marco.crear_transaccion(
        wallet_ana,
        100,
    )
)

transaccion_2 = (
    wallet_ana.crear_transaccion(
        wallet_carlos,
        50,
    )
)

bloque_1 = Block(
    indice=1,
    transacciones=[
        transaccion_1,
        transaccion_2,
    ],
)

blockchain.agregar_bloque(
    bloque_1
)


# BLOQUE 2
transaccion_3 = (
    wallet_carlos.crear_transaccion(
        wallet_laura,
        75,
    )
)

transaccion_4 = (
    wallet_marco.crear_transaccion(
        wallet_carlos,
        120,
    )
)

bloque_2 = Block(
    indice=2,
    transacciones=[
        transaccion_3,
        transaccion_4,
    ],
)

blockchain.agregar_bloque(
    bloque_2
)


# BLOQUE 3
transaccion_5 = (
    wallet_laura.crear_transaccion(
        wallet_ana,
        40,
    )
)

transaccion_6 = (
    wallet_carlos.crear_transaccion(
        wallet_marco,
        60,
    )
)

bloque_3 = Block(
    indice=3,
    transacciones=[
        transaccion_5,
        transaccion_6,
    ],
)

blockchain.agregar_bloque(
    bloque_3
)


# BLOQUE 4
transaccion_7 = (
    wallet_ana.crear_transaccion(
        wallet_laura,
        90,
    )
)

transaccion_8 = (
    wallet_marco.crear_transaccion(
        wallet_laura,
        30,
    )
)

bloque_4 = Block(
    indice=4,
    transacciones=[
        transaccion_7,
        transaccion_8,
    ],
)

blockchain.agregar_bloque(
    bloque_4
)


# BLOQUE 5
transaccion_9 = (
    wallet_laura.crear_transaccion(
        wallet_carlos,
        110,
    )
)

transaccion_10 = (
    wallet_carlos.crear_transaccion(
        wallet_ana,
        25,
    )
)

bloque_5 = Block(
    indice=5,
    transacciones=[
        transaccion_9,
        transaccion_10,
    ],
)

blockchain.agregar_bloque(
    bloque_5
)


# Mostrar la blockchain
print("BLOCKCHAIN CON PYTHON")
print("=" * 60)

blockchain.mostrar()


# Verificar cantidad de bloques
print(
    "\nCantidad de bloques:",
    len(blockchain.bloques),
)


# Verificar integridad de la cadena
print(
    "Blockchain válida:",
    blockchain.es_valida(),
)


# Mostrar saldos finales
print("\nSALDOS FINALES")
print("=" * 60)

print(wallet_marco)
print(wallet_ana)
print(wallet_carlos)
print(wallet_laura)
