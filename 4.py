a=(input('please input your score     '))
if a.isdigit():
    a=int(a)
    if a<=100 and a>0:
        if a>=90:
            print ('优秀')
        elif a>=80 and a<90:
            print ('良好')
        elif a>=70 and a<80:
            print ('中')
        elif a>=60 and a<70:
            print ('合格')
        else:
            print ('不合格')
    else:
        print ('请输入0到100范围的数字')
else:
    print ('请输入数字，谢谢')
