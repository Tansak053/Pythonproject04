#หาพื้นที่สี่เหลี่ยม เเละสามเหลี่ยม โดนรับกว้าง ยาว/ฐาน สูง ทางเเป้นพิมพ์ เเละเเสดงทางหน้าจอ
#feature การทำงานอะไรได้บ้าง
# 1.รับค่ากว้างยาว 2.รับค่า ฐาน สูง 3. คำนวณพื้นที่ สี่เหลี่ยม 4. คำนวณพื้นที่ สามเหลี่ยม
# 3. คำนวณพื้นที่ สี่เหลี่ยม เเละ เเสดงพื้นที่สี่เหลี่ยม 4.คำนวณพื้นที่ สามเหลี่ยม เเละ เเสดงพื้นที่สามเหลี่ยม
def inputWitdhLong( ):
    wi = float(input('ป้อนกว้าง : '))
    lo = float(input ('ป้อนยาว : '))
    return wi,lo

def inputBaseHigh( ):
    ba = float(input('ป้อนฐาน : '))
    hi = float(input ('ป้อนสูง : '))
    return ba,hi

def calANDShowAreaSquare( wi , lo ) :
    area = wi * lo 
    print(f'สี่เหลี่ยมกว้าง{wi} ยาว {lo} มีพื้นที่{area}')

def calANDShowAreaTrianble( ba , hi ) :
    area = ba * hi/2
    print(f'สามเหลี่ยมฐาน {ba} สูง {hi} มีพื้นที่ {area}')

wi, lo = inputWitdhLong( ) 

calANDShowAreaSquare( wi , lo )
print('----------------------')
ba,hi = inputBaseHigh ( )
calANDShowAreaTrianble(ba,hi)