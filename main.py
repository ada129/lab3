#18.1
"""def print_shurg_smile():
    print("¯\_(ツ)_/¯")
def print_ktulhu_smile():
    print("{:€")
def print_happy_smile():
    print("(͡°ʖ ͡°)")
print_happy_smile()
print_shurg_smile()
print_ktulhu_smile()
#18.2
def ask_password():
    k=True
    for i in  range(3):
        if input()=="password":
           print("Пароль принят")
           k=False
    if k:
        print("Доступ отказан")
ask_password()
#18.3
def golden_radio(i):
    st=1
    tec=1
    for i in range(1,i):
        tec+=st
        st=tec-st
    print(tec/st)
golden_radio()
?#18.5
def equation(a,b):
    x1=float(a[0])
    y1=float(a[2])
    x2=float(b[0])
    y2=float(b[2])
equation("1;2.1","2;4")
#18.6
def line(s,t):
    x=float(t[0])
    y=float(t[2])
    if float(s[0])*x+float(s[3])==y and s[2]=="+":
        print("True")
    elif float(s[0])*x-float(s[3])==y and s[2]=="-":
        print("True")
    else:
        print("False")
line("1x+6","1;7")
#19.1
s=["январь","февраль","март","апрель","май","июнь","июль","август","сентябрь","октябрь","ноябрь","декабрь"]
s1=["January","february","March","april","May","June","July","august","september","october","November","december"]
def month_name(n,lan):
    if lan=="ru":
        print(s[n-1])
    else:
        print(s1[n - 1])
month_name(2,"ru")
#19.3"""
def roots_of_quadratic_equation(a,b,c):
    c1=b*b-4*a*c
    if c1<0:
        return
    elif c1==0:
        return (-b/(2*a))
    else:
        return ((-b+c1**(1/2))/(2*a),(-b-c1**(1/2))/(2*a))
"""
print(roots_of_quadratic_equation(1,2,1))
#20.1
text=""
zap={"е","ё","а","о","я",",",".","ю","Ё","Е","А","О","Я","Ю","У","у","Э","э","и","И","ы","Ы"}
def translate(s):
    global text
    for i in range(len(s)):
        if s[i] not in zap:
            text=text+s[i]
translate("Удивительный факт, но текст на языке НЕРАЗБОРЧИВО оказывается довольнопросто читать. Достаточно небольшой тренировки - и вы сможете это делать")
print(text)
#20.2
name1=""
per=""
def setup_profile(name,vacationDates):
    global name1
    name1=name
    global per
    per=vacationDates
def print_application_for_leave():
    print("Заявление на отпуск в период "+ per+ " " + name1)
def print_holiday_money_claim(amount):
    print("Прошу выплатить ",amount ," тысяч пианистров отпускных дней")
def print_attorney_letter(toWhom):
    print("На время отпуска в период "+ per +" моим заместителям будет " +toWhom + " " + name1 )
setup_profile("иван","1-29")
print_application_for_leave()
print_attorney_letter("глеб")
print_holiday_money_claim(10)
#20.3
set=set()
def print_only_new(message):
    if message not in set:
        print(message)
        set.add(message)
print_only_new("шутка 10")
print_only_new("шутка 10")
print_only_new("шутка 20")
#20.4
base=["Иван","алина"]
def hello(name):
        print("Здравствуйте "+name+ " вашу карточку ищут...")
def search_card(name):
    for i in range(len(base)):
        if base[i]==name:
            print("Ваша карта с номером ",i+1)
            return
        print("Ваша карта не найдена")
hello("Иван")
hello("алина")
search_card("Иван")
search_card("витя")
#20.5
last=124124
def lucky(ticket):
    global last
    if (last%10+(last%100)%10+((last%1000)//100)==(last//100000+(last//10000)%10+(last//1000)%10)):
        if ticket%10+(ticket%100)%10+((ticket%1000)//100)==(ticket//100000+(ticket//10000)%10+(ticket//1000)%10):
            print("Счатливый")
            return
    print("Несчастливый")
lucky(100001)
#20.6
set=set()
def do_bet(x,y):
    if x not in set and y!=0:
        set.add(x)
        print("Ваша ставка в размере",y," на лошадь ",x," принята")
    else:
        print("Что-то пошло не так, попробуйте еще раз")
do_bet(1,200)
do_bet(2,0)
do_bet(1,100)
#21.1
def from_string_to_list(string, container):
    set={"1","2","3","4","5","6","7","8","9"}
    for i in range(len(string)):
        if string[i] in set:
            container.append(string[i])
    return container
a=[1,2,3]
a=from_string_to_list("1 2 67",a)
print(*a)
def transpose(matrix):
    for i in range(len(matrix)):
        for j in range(i,len(matrix[0])):
            c=matrix[i][j]
            matrix[i][j]=matrix[j][i]
            matrix[j][i]=c
    return matrix
matrix = [[2, 4], [1, 5]]
print(transpose(matrix))
#21.3
def swap(first, second):
    c=first[:]
    first=second[:]
    second=c
    return first,second
first=[1,2,4]
second=[3,5,6]
first,second=swap(first,second)"""
#22.4
def solve(*coefficients):
    if len(coefficients)==0 or len(coefficients)>3:
        return None
    else:
        if len(coefficients)==1:
            return 0
        if len(coefficients)==2:
            return -coefficients[1]/coefficients[0]
        else:
           return roots_of_quadratic_equation(*coefficients)
print(solve(1,-3,2))

