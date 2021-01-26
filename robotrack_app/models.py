from django.db import models


class User(models.Model):
    last_name = models.CharField(max_length=30, verbose_name="Фамилия")
    first_name = models.CharField(max_length=30, verbose_name="Имя")
    middle_name = models.CharField(max_length=30, verbose_name="Отчество", blank=True, null=True)
    birthday = models.DateTimeField(blank=True, null=True)
    role = models.CharField(max_length=30)
    city = models.CharField(max_length=30, blank=True, null=True)
    organization = models.CharField(max_length=30, blank=True, null=True)
    ovz = models.BooleanField(default=False)


class Team(models.Model):
    name = models.CharField(max_length=50)
    user = models.ManyToManyField(User)


class TypeMatch(models.Model):
    name = models.CharField(max_length=50, verbose_name="Тип матча")


class AgeGroup(models.Model):
    name = models.CharField(max_length=50, verbose_name="Возрастная группа")
    age_from = models.IntegerField()
    age_to = models.IntegerField()


class Criterion(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название критерия")
    description = models.TextField(blank=True, null=True)
    type_criterion = models.CharField(max_length=50, verbose_name="Тип критерия", blank=True, null=True)
    range_criterion = models.CharField(max_length=50, verbose_name="Диапазон оценок критерия", blank=True, null=True)


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название категории")
    description = models.TextField(blank=True, null=True)


class Competition(models.Model):
    name = models.CharField(max_length=50, verbose_name="Соревнование")
    description = models.TextField(blank=True, null=True)
    date_range = models.DateTimeField()


class Match(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название матча")
    date = models.DateTimeField(blank=True, null=True)
    state = models.BooleanField(default=False)
    type_match = models.ForeignKey(TypeMatch, on_delete=models.CASCADE)
    criterion = models.ManyToManyField(Criterion)
    category = models.ManyToManyField(Category)
    competition = models.ManyToManyField(Competition)


class Statement(models.Model):
    signature = models.ImageField(upload_to='signature')
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    referee = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)


class StatementValue(models.Model):
    value = models.CharField(max_length=30, verbose_name="Значения по критериям")
    statement = models.ForeignKey(Statement, on_delete=models.CASCADE)
    criterion = models.ForeignKey(Criterion, on_delete=models.CASCADE)




