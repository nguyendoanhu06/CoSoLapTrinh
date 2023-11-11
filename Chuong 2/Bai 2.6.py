Hoten=input('Ho ten: ')
SoNgayCong=int(input('So ngay cong: '))
DonGia=int(input('Don gia ngay cong: '))
HeSo= float(input('He so phu cap: '))
TamUng=int(input('Tam ung: '))
Luong= DonGia*SoNgayCong*HeSo
ThucLinh=Luong-TamUng
print('Nhan vien ',Hoten,', Co tien Luong=',round(Luong,1),', Tam ung=',TamUng,' va Thuc linh=',round(ThucLinh,1), sep='')

