GNiemYet= int(input('Nhap Gia niem yet: '))
ChietKhau= int(input('Nhap Chiet Khau: '))
VAT = (GNiemYet - ChietKhau)*0.01
Gban= GNiemYet - ChietKhau + VAT
print('Gia ban:', Gban)