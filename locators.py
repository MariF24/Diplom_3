from selenium.webdriver.common.by import By

class StellaburgerLocators:

    # Кнопка Конструктор
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")

    # Кнопка Войти в аккаунт
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")

    # Кнопка Лента заказов
    FEED_BUTTON = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")

    #Надпись В работе
    IN_PROGRESS_TEXT = (By.XPATH, "//p[contains(text(),'В работе')]")

    # Ссылка Восстановить пароль
    PASSWORD_RECOVERY_LINK = (By.XPATH, "//a[contains(@href,'/forgot-password')]")

    # Кнопка Восстановить
    PASSWORD_RECOVERY_BUTTON = (By.XPATH, "//button[contains(text(),'Восстановить')]")

    # Кнопка Сохранить
    SAVE_BUTTON = (By.XPATH, "//button[contains(text(),'Сохранить')]")

    #Поле со значком показать/скрыть пароль
    FIELD_ICON_SHOW_HIDE_PASSWORD = (By.XPATH, "//div[contains(@class,'input__icon input__icon-action')]")

    # Надпись Восстановление пароля
    PASSWORD_RECOVERY_TITLE = (By.XPATH, "//h2[contains(text(),'Восстановление пароля')]")

    # Поле ввода пароля в форме восстановления пароля
    PASSWORD_RECOVERY_FIELD = (By.XPATH, "//input[contains(@class,'text input__textfield') and @name = 'Введите новый пароль']")

    #Логотип сервиса
    LOGO_FIELD = (By.XPATH, "//div[contains(@class,'AppHeader_header__logo')]")

    # Поле ввода емейла в форме регистрации и входа
    EMAIL_FIELD = (By.XPATH, "//label[(text()='Email')]/../input")

    # Поле ввода пароля в форме регистрации и входа
    PASSWORD_FIELD = (By.XPATH, "//input[contains(@type,'password')]")

    # Кнопка Личный кабинет
    ACCOUNT_BUTTON = (By.XPATH, "//a[contains(@href,'/account')]")

    # Кнопка Войти
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")

    # Кнопка Выход
    LOGOUT_BUTTON = (By.XPATH, "//button[(text()='Выход')]")

    # Кнопка Оформить заказ
    CHECKOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")

    # Переход к разделу Соусы
    SECTION_SAUCES = (By.XPATH, "//div[contains(@class,'pt-4 pr-10')]/span[(text()='Соусы')]")

    # Переход к разделу Начинки
    SECTION_FILLINGS = (By.XPATH, "//div[contains(@class,'pt-4 pr-10')]/span[(text()='Начинки')]")

    # Кнопка Отмена
    CANCEL_BUTTON = (By.XPATH, "//button[contains(text(),'Отмена')]")

    # Ссылка История заказов
    LINK_ORDERS_HISTORY = (By.XPATH, "//a[contains(text(),'История заказов')]")

    # Ссылка Войти
    LOGIN_LINK = (By.XPATH, "//a[contains(@href,'/login')]")

    #Выбор ингредиента Булка
    CLICK_INGREDIENT_BUN = (By.XPATH, "//p[contains(text(), 'Флюоресцентная булка')]")

    #Выбор ингредиента Соус
    CLICK_INGREDIENT_SAUCE = (By.XPATH, "//p[contains(text(), 'Соус фирменный')]")

    #Выбор ингредиента Начинка
    CLICK_INGREDIENT_FILLING = (By.XPATH, "//p[contains(text(), 'Говяжий метеорит')]")

    #Пустое поле для перетягивания ингредиента
    DRAG_FIELD = (By.XPATH, "//img[contains(@alt,'Перетяните булочку сюда (верх)')]")

    #Поле для перетягивания ингредиента с булкой
    DRAG_FIELD_WITH_BUN = (By.XPATH, "//img[contains(@alt,'(низ)')]")

    #Перетянутый ингредиент Булка
    DRAG_INGREDIENT_BUN = (By.XPATH, "//img[contains(@alt,'Флюоресцентная булка R2-D3 (верх)')]")

    #Перетянутый ингредиент Соус
    DRAG_INGREDIENT_SAUCE = (By.XPATH, "//img[contains(@class,'constructor-element') and @alt = 'Соус фирменный Space Sauce']")

    #Перетянутый ингредиент Начинка
    DRAG_INGREDIENT_FILLING = (By.XPATH, "//img[contains(@class,'constructor-element') and @alt = 'Говяжий метеорит (отбивная)']")

    #Попап с информацией об ингредиенте
    POPUP_INGREDIENT = (By.XPATH, "//h2[contains(@class,'Modal_modal__title') and (text() ='Детали ингредиента')]")

    # Кнопка Закрыть информацию об ингредиенте
    CLOSE_POPUP_INGREDIENT = (By.XPATH, "//section[1]//button[contains(@class,'Modal_modal__close__TnseK')]")

    # Закрыть Попап с информацией об идентификаторе заказа после оформления,в Ленте заказов и Истории заказов
    CLOSE_POPUP_ID_ORDER = (By.XPATH, "//section[2]//button[contains(@class,'Modal_modal__close__TnseK')]")

    #Кнопка Закрыть попап с информацией об идентификаторе заказа
    CLOSE_BUTTON_POPUP_ID_ORDER = (By.XPATH, "//button[contains(@class,'Modal_modal__close__TnseK')]")

    #Количество ингредиента
    COUNT_INGREDIENT = (By.XPATH, "//section[1]/div[2]/ul[1]/a[1]/div[1]/p")

    #Попап с информацией об идентификаторе заказа
    POPUP_ID_ORDER = (By.XPATH, "//p[contains(text(),'идентификатор заказа')]")

    # Идентификатор заказа в Ленте заказов и Истории заказов
    IDENTIFIER_ORDER_IN_FEED_AND_HISTORY = (By.XPATH, "//li[1]/a/div[1]/p[1]")

    # Попап созданного заказа в Ленте заказов и Истории заказов
    POPUP_ORDER_IN_FEED_HISTORY = (By.XPATH, "//section[2]/div[1]/div")

    #Номер идентификатора заказа
    IDENTIFIER_ORDER = (By.XPATH, "//div[1]/h2[contains(text(),'')]")

    # Номер идентификатора заказа В работе
    IDENTIFIER_ORDER_IN_PROGRESS = (By.XPATH, "//div[1]/ul[2]/li")

    # Ссылка Зарегистрироваться
    REGISTRATION_LINK = (By.XPATH, "//a[contains(@href,'/register')]")

    # Кнопка Зарегистрироваться
    REGISTRATION_BUTTON = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")

    # Поле ввода имени в форме регистрации
    NAME_FIELD = (By.XPATH, "//label[(text()='Имя')]/../input")

    # Количество заказов Выполнено за все время
    COUNT_ORDERS_ALL = (By.XPATH, "//div[2]/p[2][contains(@class,'OrderFeed_number')]")

    #Количество заказов Выполнено за сегодня
    COUNT_ORDERS_TODAY = (By.XPATH, "//div[3]/p[2][contains(@class,'OrderFeed_number')]")

    # Дублирующее окно при создании заказа и блокирующее окно при открытии главной страницы в браузере Firefox
    DUPLICATE_MODAL_ID_ORDER = (By.XPATH, "//div/div[contains(@class,'Modal_modal_overlay__x2ZCr')]")

