def squares():
  """Tạo list chứa bình phương các số từ 1 đến 20 và in ra, ngoại trừ 5 số đầu tiên."""
  # Tạo list chứa bình phương các số từ 1 đến 20
  squares = [x**2 for x in range(1, 21)]

  # Bỏ qua 5 số đầu tiên
  squares = squares[5:]

  # In ra list
  for square in squares:
    print(square)

# Gọi hàm
squares()
