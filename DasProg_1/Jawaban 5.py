# Meminta input volume dan menit
volume = int(input("Masukkan volume infus (ml) : "))
menit = int(input("Masukkan berapa menit infusnya habis : "))

# Rumus
Rate = volume/(menit/60)

# Output
print(f"VTBI : {volume} ml")
print(f"Rate : {Rate} ml/hr")