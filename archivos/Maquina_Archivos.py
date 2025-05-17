import datetime

Products = {
    1: {"name": "Galleta", "price": 1200},
    2: {"name": "Botella con Agua", "price": 2500},
    3: {"name": "Paquete de Papas Fritas", "price": 3600},
    4: {"name": "Pan", "price": 900}
}

Denominaciones = [100, 200, 500, 1000, 2000, 5000, 10000]

def main():
    mostrar_bienvenida()
    while True:
        total_money = input_money()
        if total_money is None:
            print("Programa finalizando.\nQue tenga un lindo día :)")
            break
        product_code = select_product()
        if product_code is None:
            continue

        product = Products[product_code]
        if validate_payment(total_money, product["price"]):
            print(f"\nUsted ha comprado '{product['name']}' por ${product['price']}")
            print("¡Producto entregado!")
            change = total_money - product["price"]
            return_change(change)
            guardar_historial(product['name'], product['price'], total_money, change)
        else:
            print("Compra cancelada por fondos insuficientes.")

def mostrar_bienvenida():
    print("\n" + "_" * 33)
    print("  Bienvenido a la Máquina Expendedora")
    print("  podrás adquirir tus productos favoritos.")
    print("  Aceptamos las siguientes denominaciones de dinero :")
    print(" ", Denominaciones)
    print("  Para salir, puedes ingresar -1 en cualquier momento.")
    print("_" * 33 + "\n")

def show_menu():
    print("\n" + "__" * 25)
    print("Productos Disponibles")
    print("Código \t| Precio \t| Nombre")
    print("-" * 35)
    for code, details in Products.items():
        print(f"{code} \t\t| ${details['price']} \t| {details['name']}")
    print("__" * 20)

def input_money():
    total = 0
    print("__" * 30)
    print("\nPor favor, ingrese su dinero.")
    print("Cantidades válidas que la máquina recibe:", Denominaciones)
    print("Ingrese -1 para salir, 0 para seleccionar producto.")

    while True:
        user_input = int(input("Monto: "))
        if user_input == -1:
            return None
        elif user_input == 0:
            break
        elif user_input in Denominaciones:
            total += user_input
            print(f"Saldo actual: ${total}")
        else:
            print("Cantidad no válida.")
    return total

def select_product():
    show_menu()
    while True:
        code = int(input("Ingrese el código del producto (0 para cancelar): "))
        if code == 0:
            print("Compra cancelada. Que tenga un bonito día/noche.")
            return None
        if code in Products:
            product = Products[code]
            print(f"Producto seleccionado: '{product['name']}' - Precio: ${product['price']}")
            return code
        else:
            print("Código inválido.")

def validate_payment(total, price):
    if total >= price:
        print("Pago aceptado. Procesando compra...")
        return True
    else:
        print(f"Saldo insuficiente. Tiene ${total}, necesita ${price}.")
        return False

def return_change(change):
    if change > 0:
        print(f"\nSu cambio es: ${change}")
        denominations = sorted(Denominaciones, reverse=True)
        for denom in denominations:
            count = change // denom
            if count > 0:
                print(f"{count} x ${denom}")
                change %= denom
    else:
        print("No hay cambio. Gracias por su compra.")

def guardar_historial(nombre_producto, precio, dinero_ingresado, cambio):
    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linea = f"{fecha} | Producto: {nombre_producto} | Precio: ${precio} | Ingresado: ${dinero_ingresado} | Cambio: ${cambio}\n"
    with open("compras.txt", "a", encoding="utf-8") as archivo:
        archivo.write(linea)

if __name__ == '__main__':
    main()

