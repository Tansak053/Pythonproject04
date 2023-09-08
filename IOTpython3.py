#Function A : No Parameter/Have return
def funcA( ):
    print('AAA')
    print('BBB')
    return ' WOW WOW WOW'

def funcB( ):
    return 999, True ,10+20

#funcA( )เขียนได้เเต่เขาไม่ทำกัน
print( funcA ( ) )
x = funcA( )

a , b, c = funcB( )   #****
print(f'{a} {b} {c}')