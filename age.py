driving = input('請問你有沒有開過車(有/沒有)?')
if driving != '有' and driving != '沒有':
	print('該問題只能輸入(有/沒有)，謝謝。')
	raise SystemExit

age = input('請問你的年齡?')
age = int(age)
if driving =='有': 
	if age >= 18:
		print('看來你已經通過駕照測驗了。')
	else:
		print('奇怪，你不應該有開過車才對。')
elif driving == '沒有':
	if age >= 18:
		print('你可以考駕照了，怎麼還不去考?')
	else:
		print('很好，你再過一陣子就可以考駕照了。')