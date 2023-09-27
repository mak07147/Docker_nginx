#1. Сделать простое web-приложение с главной страницей и тремя точками входа. Реализовать можно на любом ЯП, с применением любых фреймворков (например flask, gin, Spring Boot.
#	-  Главная страница выводит текущую дату и время
#	-  Первая точка входа выводит приветствие (название `/greetings`)
#	-  Вторая выводит имя сервера (название `/servername`)
#2. Подготовить `Dockerfile` для приложения, собрать образ и отправить в registry.
#3. Подготовить docker-compose файл, который запускает 3 контейнера: 
#	- 2 контейнера приложение из п.1
#	- nginx в качестве балансировщика между ними
#4. Изменить проект так, чтобы nginx в контейнере запускался не от рута
#5. Настроить на nginx TLS с самоподписанным сертификатом
#6. Настроить перенаправление http запросов на https
#7. Настроить nginx так, чтобы любой запрос к несуществующему ресурсу перенаправлялся на точку входа `/greetings`. 
#8. Настроить nginx так, чтобы запросы на `/servername` перенаправлялись на `/hostname` с соответствующим изменением пути в адресной строке браузера.  
#9. Настроить nginx так, чтобы запросы на `/hello`  отображали тоже-самое, что при запросе на `/greetings`, при этом url в адресной строке браузера не должен меняться. (для обработки запроса на `/hello` должен использоваться отдельный блок `/location`).
#10. Настроить nginx так, чтобы запросы к  приложению по путям `/random-dog`, `/randomdog`  и `/dograndom` показывал содержимое страницы https://random.dog/  (текст + картинка/видео/анимация), при этом, содержимое адресной строки не должно меняться. 
#11. Настроить nginx так, чтобы запросе `/greetings?user=userName` на странице выводилось `Hello, userName!`.
#12. Тоже самое, что 11, только параметр `user` передаётся через заголовок http запроса `X-User-Name` на точку входа `/hi`.
#13. Настроить nginx так, чтобы при запросе на `/envtext` пользователю  возвращалось текстовое сообщение. Содержимое этого сообщения должно передаваться в конфиг.файл nginx через переменную среды, задаваемую в `docker-compose.yml.`