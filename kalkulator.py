a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua: "))
op = input("Operator (+, -, *, /): ")

if op == "+":
    print("Hasil:", a + b)
elif op == "-":
    print("Hasil:", a - b)
elif op == "*":
    print("Hasil:", a * b)
elif op == "/":
    print("Hasil:", a / b)
else:
    print("Operator tidak valid")
