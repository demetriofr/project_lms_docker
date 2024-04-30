## Платформа для онлайн-обучения

В мире развивается тренд на онлайн-обучение. Поэтому для веб-разработчика важно не только обучиться, но и знать, 
как реализовать платформу для онлайн-обучения. 

**Цель проекта:** Разработка LMS-системы, в которой каждый желающий может размещать свои полезные материалы или курсы.

Данный проект это SPA веб-приложение и результатом создания его будет бэкенд-сервер, который возвращает клиенту 
JSON-структуры.


### ДЗ: 24.1 Вьюсеты и дженерики

#### Задание 1
- [x] Создайте новый Django-проект, подключите DRF в настройках проекта.

#### Задание 2
Создайте следующие модели:

- [x] Пользователь:
все поля от обычного пользователя, но авторизацию заменить на email; 
- телефон; 
- город; 
- аватарка.
- [x] Модель пользователя разместите в приложении users

- [x] Курс:
- название, 
- превью (картинка), 
- описание.

- [x] Урок:
- название, 
- описание, 
- превью (картинка), 
- ссылка на видео.

**Урок и курс** - это связанные между собой сущности. Уроки складываются в курс, в одном курсе может быть много уроков. 
- [x] Реализуйте связь между ними.

- [x] Модель курса и урока разместите в отдельном приложении. 
Название для приложения выбирайте такое, чтобы оно описывало то, с какими сущностями приложение работает. Например, 
lms или materials - отличные варианты.


#### Задание 3
- [x] Опишите CRUD для моделей курса и урока. 
Для реализации CRUD
- - [x] для курса используйте Viewsets, 
- - [x] а для урока - Generic-классы.

- [x] Для работы контроллеров опишите простейшие сериализаторы.

- [x] При реализации CRUD для уроков реализуйте все необходимые операции (получение списка, получение одной сущности, 
создание, изменение и удаление).

- [x] Работу каждого эндпоинта необходимо проверять с помощью Postman.

Также на данном этапе работы мы не заботимся о безопасности и не закрываем от редактирования объекты и модели даже 
самой простой авторизацией.


#### Дополнительное задание
- [x] Реализуйте эндпоинт для редактирования профиля любого пользователя на основе более привлекательного подхода для 
личного использования: Viewset или Generic.



### ДЗ: 24.2 Сериализаторы

#### Задание 1
- [x] Для модели курса добавьте в сериализатор поле вывода количества уроков. Поле реализуйте с помощью 
SerializerMethodField()


#### Задание 2
- [x] Добавьте новую модель в приложение users:

Платежи
- пользователь,
- дата оплаты, 
- оплаченный курс или урок, 
- сумма оплаты, 
- способ оплаты: наличные или перевод на счет.

- [x] Поля пользователь, оплаченный курс и отдельно оплаченный урок должны быть ссылками на соответствующие модели.

- [x] Запишите в таблицу, соответствующую этой модели данные через инструмент фикстур или кастомную команду.

Если вы забыли как работать с фикстурами или кастомной командой - можете вернуться к уроку 20.1 Работа с ORM в Django 
чтобы вспомнить материал.


#### Задание 3
- [x] Для сериализатора для модели курса реализуйте поле вывода уроков. 
- - [x] Вывод реализуйте с помощью сериализатора для связанной модели.

Один сериализатор должен выдавать и количество уроков курса и информацию по всем урокам курса одновременно.

#### Задание 4
- [x] Настроить фильтрацию для эндпоинта вывода списка платежей с возможностями:

- менять порядок сортировки по дате оплаты,
- фильтровать по курсу или уроку,
- фильтровать по способу оплаты.


#### Дополнительное задание
- [x] Для профиля пользователя сделайте вывод истории платежей, расширив сериализатор для вывода списка платежей.



### ДЗ: 25.1 Права доступа в DRF

#### Задание 1
- [x] Реализуйте CRUD для пользователей, в том числе 
- - [x] регистрацию пользователей, 
- - [x] настройте в проекте использование JWT-авторизации и 
- - [x] закройте каждый эндпоинт авторизацией.

- [x] Эндпоинты для авторизации и регистрации должны остаться доступны для неавторизованных пользователей.


#### Задание 2
- [x] Заведите группу модераторов и 
- опишите для нее права работы с любыми уроками и курсами, 
- но без возможности их удалять и создавать новые. 

- [x] Заложите функционал такой проверки в контроллеры.


#### Задание 3
- [x] Опишите права доступа для объектов таким образом, чтобы пользователи, которые не входят в группу модераторов, 
- могли видеть, 
- редактировать и 
- удалять только свои курсы и уроки.

- [x] Заводить группы лучше через админку и не реализовывать для этого дополнительных эндпоинтов.


#### Дополнительное задание
- [x] Для профиля пользователя введите ограничения, чтобы авторизованный пользователь 
- мог просматривать любой профиль, 
- но редактировать только свой. 
- [x] При этом для просмотра чужого профиля должна быть доступна только общая информация, в которую не входят: 
- пароль, 
- фамилия, 
- история платежей.



### ДЗ: 25.2 Валидаторы, пагинация и тесты

#### Задание 1
- [x] Для сохранения уроков и курсов реализуйте 
- - [x] дополнительную проверку на отсутствие в материалах ссылок на сторонние - ресурсы, 
- - [x] кроме youtube.com.
- То есть ссылки на видео можно прикреплять в материалы, а ссылки на сторонние образовательные платформы или личные 
сайты — нельзя.

- [x] Создайте отдельный файл validators.py,
- [x] реализуйте валидатор, проверяющий ссылку, 
- которую пользователь хочет записать в поле урока с помощью класса или функции.

- [x] Интегрируйте валидатор в сериализатор.

- [x] Если вы используете 
- функцию-валидатор — указанием валидаторов для поля сериализатора validators=[ваш_валидатор].
- класс-валидатор — указанием валидаторов в class Meta: validators = [ваш_валидатор(field='поле_которое_валидируем')].


#### Задание 2
- [x] Добавьте модель подписки на обновления курса для пользователя.

- [x] Модель подписки должна содержать следующие поля: 
- «пользователь» (FK на модель пользователя), 
- «курс» (FK на модель курса). 
- Можете дополнительно расширить модель при необходимости.

- [x] Вам необходимо реализовать эндпоинт для установки подписки пользователя и на удаление подписки у пользователя.

- [x] При этом при выборке данных по курсу пользователю необходимо присылать признак подписки текущего пользователя на курс. 
- То есть давать информацию, подписан пользователь на обновления курса или нет.


#### Задание 3
- [x] Реализуйте пагинацию для вывода всех уроков и курсов.

- - [x] Пагинацию реализуйте в отдельном файле paginators.py. 
- Можно реализовать один или несколько классов пагинатора. 
- - [x] Укажите параметры 
- - page_size, 
- - page_size_query_param, 
- - max_page_size
- для класса PageNumberPagination
- Количество элементов на странице выберите самостоятельно. 
- [x] Интегрируйте пагинатор в контроллеры, используя параметр pagination_class.


#### Задание 4
- [x] Напишите тесты, которые будут проверять корректность работы
- CRUD уроков и 
- функционал работы подписки на обновления курса.

- [x] В тестах используйте метод setUp для заполнения базы данных тестовыми данными. 
- [x] Обработайте возможные варианты взаимодействия с контроллерами пользователей с разными правами доступа. 
- [x] Для аутентификации пользователей используйте self.client.force_authenticate()

- [x] Сохраните результат проверки покрытия тестами.
