def send_email (message , recipient , sender = "university.help@gmail.com"):
    if sender == 'university.help@gmail.com':
        print( f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender != recipient:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")
    elif recipient  not in ("@" , ".com",".ru",".net" ) and sender not in ("@" , ".com",".ru",".net" ):
        print (f'Невозможно отправить письмо с адреса {recipient} на адрес {sender}')



    else:
        print ("Нельзя отправить письмо самому себе!")







send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email ('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'university.help.' , sender= 'box')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.info@gmail.com', sender='urban.info@gmail.com')
