#Function 2 : Have Parameters/No Return
#parameter คือ ตัวแปรประเภทหนึ่ง ขอบเขตการใช้งานพารามิเตอร์
#ใช้งานได้เฉพาะในฟังก์ชั่นนั้นๆ เท่านั้น

def funcA ( x , y ):
    print ('Hi...')
    z=x+y
    print(f'{x} + {y} ={z}')
    #ไม่มีคำสั่ง return

def funcB (x):
    print(f"X is {x} 555 ... ")

funcA(10,20) #Argument อากิวเมน
funcA(5,5)
funcB( ' SAU IOT ')
