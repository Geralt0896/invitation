import smtplib
server = smtplib.SMTP_SSL('smtp.yandex.ru', 456)
server.login('cozlova.v3ronicka@yandex.ru', 'Veronika+96')
server.sendmail('cozlova.v3ronicka@yandex.ru_from', 'ischmametovruslan@yandex.ru_to', 'message')
server.quit()
sample = """From: ischmametovruslan@yandex.ru
To: cozlova.v3ronicka@yandex.ru
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";
Привет, %friend_name%! %my_name% приглашает вас на сайт %website%!

%website% — это новая версия онлайн-курса по программированию.
Изучаем Python и не только. Решаем задачу. Получаем отзывы от преподавателей.

Как будет проходить ваше обучение на %website%?

→ Попрактикуешься на своих кейсах.
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей.
Задачи не «сгорят» и не уйдут в раунд. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решения наших задач — можно ссылаться на твоём GitHub. Работодатели такое оценят.

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить о релизе сразу на имейл."""
sample = sample.replace("%website%", "https://dvmn.org/profession-ref-program/tatarin08.96/prjNs/"). replace("%my_name%", "Руслан"). replace("%friend_name%", "Вероника")
sample = sample.encode("UTF-8")
print(sample)
