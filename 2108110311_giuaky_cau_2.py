def is_valid_code(code):
  """Kiểm tra mã hàng hợp lệ hay không."""
  return len(code) == 4 and code[0].isalpha() and code[1:].isdigit()

def is_valid_quantity(quantity):
  """Kiểm tra số lượng hợp lệ hay không."""
  return 1 <= quantity <= 100

def is_valid_price(price):
  """Kiểm tra giá bán hợp lệ hay không."""
  return 1 <= price <= 100

def main():
  """Chương trình quản lý hàng hóa."""
  # Nhập số lượng hàng hóa
  n = int(input("Nhập số lượng hàng hóa: "))

  # Tạo dictionary lưu trữ thông tin hàng hóa
  products = {}

  # Nhập thông tin cho từng hàng hóa
  for i in range(n):
    # Nhập mã hàng
    while True:
      code = input("Nhập mã hàng (b123): ").lower()
      if is_valid_code(code):
        break
      print("Mã hàng không hợp lệ. Vui lòng nhập lại.")

    # Nhập tên hàng
    name = input("Nhập tên hàng: ")

    # Nhập số lượng
    while True:
      try:
        quantity = int(input("Nhập số lượng: "))
        if is_valid_quantity(quantity):
          break
        print("Số lượng không hợp lệ. Vui lòng nhập lại.")
      except ValueError:
        print("Số lượng phải là số nguyên. Vui lòng nhập lại.")

    # Nhập giá bán
    while True:
      try:
        price = float(input("Nhập giá bán: "))
        if is_valid_price(price):
          break
        print("Giá bán không hợp lệ. Vui lòng nhập lại.")
      except ValueError:
        print("Giá bán phải là số nguyên. Vui lòng nhập lại.")

    # Thêm thông tin hàng hóa vào dictionary
    products[code] = {
      "name": name,
      "quantity": quantity,
      "price": price
    }

  # In danh sách hàng hóa vừa nhập ra màn hình
  print("-" * 40)
  print("Danh sách hàng hóa")
  print("-" * 40)
  for code, product in products.items():
    print(f"Mã hàng: {code}")
    print(f"Tên hàng: {product['name']}")
    print(f"Số lượng: {product['quantity']}")
    print(f"Giá bán: {product['price']}")
    print("-" * 20)

  # Hiển thị thông tin các mặt hàng có số lượng lớn hơn 5
  print("-" * 40)
  print("Mặt hàng có số lượng lớn hơn 5")
  print("-" * 40)
  for code, product in products.items():
    if product["quantity"] > 5:
      print(f"Mã hàng: {code}")
      print(f"Tên hàng: {product['name']}")
      print(f"Số lượng: {product['quantity']}")
      print(f"Giá bán: {product['price']}")
      print("-" * 20)

  # Hiển thị thông tin các mặt hàng có giá bán nhỏ hơn 10
  print("-" * 40)
  print("Mặt hàng có giá bán nhỏ hơn 10")
  print("-" * 40)
  for code, product in products.items():
    if product["price"] < 10:
      print(f"Mã hàng: {code}")
      print(f"Tên hàng: {product['name']}")
      print(f"Số lượng: {product['quantity']}")
      print(f"Giá bán: {product['price']}")
      print("-" * 20)

if __name__ == "__main__":
  main()
