from django.db import models


class Poll(models.Model):
    """Опросы"""
    poll_name = models.CharField("Название опроса", max_length=200, help_text="Не более 200 символов")
    str_date = models.DateField("Время старта опроса",
                                help_text="Помните: Если опрос по времени стартанул - то изменить его уже нельзя будет")
    end_date = models.DateField("Время окончания опроса",
                                help_text="Укажите, когда перестанет быть активным опрос")
    poll_description = models.TextField("Описание опроса")

    def __str__(self):
        return self.poll_name

    class Meta:
        verbose_name = "Опрос"
        verbose_name_plural = "Опросы"


class Question(models.Model):
    """Вопросы"""
    CHOICES = (
        ('Т', 'ответ текстом'),
        ('О', 'один ответ'),
        ('М', 'много ответов'),
    )
    poll = models.ForeignKey("Poll", verbose_name="Опросник", related_name='questions', on_delete=models.CASCADE)
    question_text = models.CharField("Вопрос", max_length=200)
    question_type = models.CharField("Тип вопроса", max_length=10, choices=CHOICES,
                                     help_text="Выберите какой тип ответа нужен для этого вопроса")

    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


class Options(models.Model):
    """Выбор"""
    question = models.ForeignKey("Question", verbose_name="Вопрос", related_name='options', on_delete=models.CASCADE)
    options_text = models.CharField("Вариант ответа", max_length=100, help_text="не более 100 символов")

    def __str__(self):
        return self.options_text

    class Meta:
        verbose_name = "Вариант ответа"
        verbose_name_plural = "Варианты ответа"


class User(models.Model):
    """Пользователи"""
    anonymous = models.BooleanField("Аноним", default=False)
    user_name = models.CharField("ФИО пользователя", max_length=100, help_text="не более 100 символов", blank=True)
    mail = models.CharField("Электронная почта", max_length=50, help_text="не более 50 символов", blank=True)
    number = models.CharField("Номер телефона", max_length=15, help_text="не более 15 символов", blank=True)

    def __str__(self):
        if self.anonymous:
            return "Аноним"
        return self.user_name

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Answer(models.Model):
    """Ответы"""

    user = models.ForeignKey("User", verbose_name="Пользователь", related_name='user', on_delete=models.CASCADE)
    poll = models.ForeignKey("Poll", verbose_name="Опрос", related_name='poll', on_delete=models.CASCADE)
    question = models.ForeignKey("Question", verbose_name="Вопрос", related_name='question',
                                 on_delete=models.CASCADE)
    options_text = models.CharField("Ответ текстом", max_length=100, blank=True, default="")
    options_one = models.ForeignKey("Options", verbose_name="Выбрать ответ", on_delete=models.CASCADE, blank=True,
                                    null=True)
    options_many = models.ManyToManyField("Options", verbose_name="Несколько ответов", related_name='options_many',
                                          blank=True)

    def __str__(self):
        if self.options_text:
            return self.options_text
        elif self.options_one:
            return "%s [%s]" % ("Вариант", self.options_one)
        elif self.options_many:
            return "%s [%s]" % (self.user, "Несколько вариантов")

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"
