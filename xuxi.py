from random import randint

print("-"*20)
player = input("nhập Búa, Kéo, Lá:")
print("-"*20)
computer = randint(0,2)

if computer == 0:
	computer = "Kéo"
if computer == 1:
	computer = "Búa"
if computer == 2:
	computer = "Lá"

print("-"*20)
print("bạn chọn:", player)
print("máy chọn:", computer)
print("-"*20)	

if player == computer:
	print("Hòa")

if player == "Kéo":
	if computer == "Búa":
		print("Thua")
	if computer == "Lá":
		print("Thắng")	

if player == "Búa":
	if computer == "Lá":
		print("Thua")
	if computer == "Kéo":
		print("Thắng")	

if player == "Lá":
	if computer == "Kéo":
		print("Thua")
	if computer == "Búa":
		print("Thắng")					
