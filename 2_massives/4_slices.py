"""Получение среза."""

invocie = """
0.....6.................................40........52...55........
1909  Pimoroni PiBrella                 $17.50    3    $52.50
1489  6mm Tactile Switch x20            $4.95     2    $9.90
1510  Panavise Jr. - PV-201             $28.00    1    $28.00
"""

"""We can name slice objects:"""

print('Named slices demo:\n')
SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 50)
QUANTITY = slice(50, 55)
ITEM_TOTAL = slice(55, None)
invoice_items = invocie.split('\n')[2:]
for item in invoice_items:
    print(item[DESCRIPTION], item[UNIT_PRICE])
