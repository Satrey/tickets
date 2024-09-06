from django.db import models


class Test(models.Model):
    pass


class Theme(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Тематика теста')
    slug = models.SlugField(max_length=60, db_index=True, null=True, blank=True, verbose_name='Слаг')

    class Meta:
        verbose_name = ('Тема')
        verbose_name_plural = ('Темы')

    def __str__(self):
        return self.name


class Ticket(models.Model):
    number = models.IntegerField(default=0, null=True, db_index=True, verbose_name='Билет')
    theme = models.ForeignKey('Theme', on_delete=models.CASCADE, related_name='theme')

    class Meta:
        verbose_name = ('Билет')
        verbose_name_plural = ('Билеты')

    def __str__(self):
        n = Ticket.objects.all()
        return "Билет №" + str(self.number) + '-' + str(self.theme.name)


class Question(models.Model):
    theme = models.ForeignKey('Theme', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Тема вопроса')
    ticket = models.ForeignKey('Ticket', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Билет')
    text = models.TextField(max_length=500, verbose_name='Вопрос')
    description = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Пояснение к вопросу')
    multiselect = models.BooleanField(default=False, verbose_name='Несколько вариантов')

    class Meta:
        verbose_name = ('Вопрос')
        verbose_name_plural = ('Вопросы')

    def __str__(self):
        return self.text[:50]


class Answer(models.Model):
    text = models.TextField(max_length=500, db_index=True)
    ques = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    correct = models.BooleanField(default=False)

    class Meta:
        verbose_name = ('Ответ')
        verbose_name_plural = ('Ответы')

    def __str__(self):
        return self.text[:30]

