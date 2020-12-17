# Tìm hiểu về module math trong Python rồi trả lời các câu hỏi sau:
#    1. Module đó có mục đích gì?
#    2. Kể tên một số thứ trong nó hay dùng hoặc bạn thấy ấn tượng?
#    3. Code minh họa cho các thứ đã nói ở câu trên?
"""
1. Module Math trong python dùng để biểu diễn các công thức toán học
2. hàm thường dùng như math.pow() dùng để thể hiện giá trị lũy thừa
"""
# noinspection PyUnresolvedReferences
import math
x = 2
y = 3
a = pow(2, 3) # hàm pow thể hiện 2*2*2 là 2 lũy thừa 3
print(a)
'''
Code đoạn chương trình cho phép:
 1. Nhập vào bán kình r của đường tròn
 2. Tính diện tích đường tròn đó
 3. In kết quả ra màn hình "Dien tich hình tron la: <giá trị"
'''
import math
var = math.pi
r = float(input('mời nhập bán kính: ')) # bán kính đường tròn
perimeter_circle = (var*r)
area_circle = var * pow(r,2)
print('Chu vi đường tròn: ''%.2f' % perimeter_circle)
print('bán kính đường tròn: ''%.2f' % area_circle)
'''
Đặt 7 tên biến (variable) hợp lệ, chuẩn PEP8
'''
var_1 = 'chuỗi đầu tiên'
var_2 = 123132
var_3 = True
var_4 = '231qcv'
ho_ten = 'Co_Nhan_Thien'
a = 1
b =2*2
'''
Đặt 7 tên biến (variable) không hợp lệ
'''
#nhẫn=thiên
#if=1
#try=sada
#345=avb
#^&**=13
#  abc=122
'''
Code đoạn chương trình để giải quyết các yêu cầu sau
1. Nhập 3 số thực x, y, z  bất kì.
2. Tính giá trị biểu thức F:
               F = (x+y+z)/(x^2+y^2+1) - |x-z*cos(y)|
3. Đưa giá trị tính được của F  ra màn hình dưới dạng:
              Gia tri cua F  = <gia tri>
'''
x = float(input('mời nhập x: '))
y = float(input('mời nhập y: '))
z = float(input('mời nhập z: '))
cos_y = math.cos(y)
F = (x+y+z) / (x**2+y**2+1) - abs(x-z*cos_y)
print('Giá trị của F =', F)







