import tkinter
root = tkinter.Tk()
root.geometry('300x270+400+100')
root.title(r"lin's calculator")
contentVar = tkinter.StringVar(root,'')

def fac(a):
	if a>1:
		return a*fac(a-1)
	else:
		return a
def getNum(x):
	global h,j,a,b
	h,j=i-1,i+2
	if h==0:#用于取3x23运算符号前面数字
		a=float(x[h:i])
	else:
		while h>=0:
			if x[h] not in ['+','-','x','/','^','!']:#用于取运算符号前面数字
				h-=1
				if h==0:
					a=float(x[h:i])#用于取(-3)x23运算符号前面的数字
					break
			else:
				if x[h]=='-' and x[h-1] in ['+','-','x','/']:#用于...+(-22)x5中取运算符号前面负数的情况
					a=float(x[h:i])
					break
				else:
					a=float(x[h+1:i])	#用于...+22x5取运算符号前面数字的情况
					break

	if x[i]=='!':
		return
	while j<=len(x)-1:
		if x[j] not in ['+','-','x','/','^','!']:#用于32x(-22)取运算符号后面负数的情况
			j+=1
		else:
			break
	b=float(x[i+1:j])
def judge_bracket(x):
	i=len(x)-1
	while i>=0:
		if x[i]=='(':
			j=i
			while j<=len(x)-1:
				if x[j]!=')':
					j+=1
				else:
					x=str(calculate(x[i+1:j])).join(x.split(x[i:j+1]))
					break
		else:
			i-=1
	return x
def loop1(x,operator):
	global i
	getNum(x)
	if h==0:
		if operator=='!':
			x=x.split(x[h:i+1])
		else:
			x=x.split(x[h:j])
	else:
		if x[h]=='-' and x[h-1] in ['+','-','x','/']:
			if operator=='!':
				x=x.split(x[h:i+1])
			else:
				x=x.split(x[h:j])
		else:
			if operator=='!':
				x=x.split(x[h+1:i+1])
			else:
				x=x.split(x[h+1:j])
	if operator=='^':
		x=str(a**b).join(x)
	elif operator=='/':
		x=str(a/b).join(x)
	elif operator=='x':
		x=str(a*b).join(x)
	elif operator=='!':
		x=str(fac(a)).join(x)
	elif operator=='-':
		x=str(a-b).join(x)
	i=h+2
	return x
def loop(x,operator):
	global i
	i=0
	while i<=len(x)-1:
		if x[i]==operator:
			if operator=='-':
				if i==0:
					i+=1
				elif x[i-1] not in ['+','-','x','/','^','!']:					
					x=loop1(x,'-')
				else:
					i+=1
			else:
				if operator=='!':
					x=loop1(x,'!')
				elif operator=='^':
					x=loop1(x,'^')
				elif operator=='/':
					x=loop1(x,'/')
				elif operator=='x':
					x=loop1(x,'x')
		else:
			i+=1
	return x
def calculate(x):
	x,y=loop(loop(loop(loop(loop(x,'!'),'^'),'/'),'x'),'-').split('+'),0
	for temp in x:
		y+=float(temp)
	return y
#==============================================
while True:
	print('')
	print('===Scientific Calculator 1.0==='.center(70))
	print('===Supported Operator[sum:+,sub:-,mul:x,div:/,exp:^,fac:!,bracket:()]==='.center(70))
	x=(input('Enter The Formule:\n'))[:-1]
	print(calculate(judge_bracket(x)))
	notice=input('Press Enter to Continue/\'q\'to quit:')
	if notice=='q':
		break