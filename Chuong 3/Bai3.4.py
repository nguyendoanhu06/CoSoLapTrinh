Toan=int(input())
Ly=int(input())
Hoa=int(input())
DTB=((Toan*2)+(Ly*3)+Hoa)/6
if DTB<3:
    print('Kém')
elif 3<=DTB<5:
    print('Yếu')
elif 5<=DTB<6:
    print('Trung Bình')
elif 6<=DTB<7:
    print('Trung bình Khá')
elif 7<=DTB<8:
    print('Khá')
elif 8<=DTB<9:
    print('Giỏi')
elif 9<=DTB<10:
    print('Xuất sắc')
    