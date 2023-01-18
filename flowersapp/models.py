from django.db import models


class Payment(models.Model):
    сard_number = models.CharField(
        'Номер карты',
        max_length=200,
        db_index=True
    )
    card_date = models.DateField(
        'Срок годности карты',
        db_index=True
    )
    owner_name = models.CharField(
        'Имя и фамилия владельца',
        max_length=200,
        db_index=True
    )
    cvv = models.IntegerField(
        'CVV карты',
        db_index=True
    )

    def __str__(self) -> str:
        return self.owner_name

    class Meta:
        verbose_name = 'Средтсво оплаты'
        verbose_name_plural = 'Средтсва оплаты'


class Consultation(models.Model):
    full_name = models.CharField(
        'ФИО покупателя',
        max_length=200,
        db_index=True
    )
    phonenumber = models.CharField(
        'Номер телефона владельца',
        max_length=20,
        db_index=True
    )

    def __str__(self) -> str:
        return self.full_name

    class Meta:
        verbose_name = 'Консультация'
        verbose_name_plural = 'Консультации'


class Buyer(models.Model):
    full_name = models.CharField(
        'ФИО покупателя',
        max_length=200,
        db_index=True
    )
    address = models.TextField(
        'Адрес покупателя',
        db_index=True
    )
    email = models.EmailField(
        'Почта покупателя',
        db_index=True
    )
    phonenumber = models.CharField(
        'Номер телефона владельца',
        max_length=20,
        db_index=True
    )
    сonsultation = models.ForeignKey(
        'Consultation',
        on_delete=models.CASCADE,
        verbose_name='консультация',
        related_name='сonsultations',
        null=True
    )
    payment = models.ForeignKey(
        'Payment',
        on_delete=models.CASCADE,
        verbose_name='Оплата',
        related_name='payments',
        null=True
    )

    def __str__(self) -> str:
        return self.full_name

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'


class Shop(models.Model):
    shop_name = models.CharField(
        'Название магазина',
        max_length=200,
        db_index=True
    )
    store_photo = models.ImageField(
        'Фото магазина',
        upload_to='media',
        db_index=True
    )
    address = models.TextField(
        'Адрес Магазина',
        db_index=True
    )
    is_working = models.BooleanField(
        'Работает ли магазин',
        db_index=True
    )

    def __str__(self) -> str:
        return self.shop_name

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'


class Bouquet(models.Model):
    bouquet_name = models.CharField(
        'Название букета',
        max_length=200,
        db_index=True
    )
    bouquet_photo = models.ImageField(
        'Фото букета',
        upload_to='media',
        db_index=True
    )
    price = models.FloatField(
        'Цена букета',
        db_index=True
    )
    amount = models.IntegerField(
        'Количество букетов в наличии',
        db_index=True
    )

    def __str__(self) -> str:
        return self.bouquet_name

    class Meta:
        verbose_name = 'Букет'
        verbose_name_plural = 'Букеты'


class Order(models.Model):
    buyer = models.ForeignKey(
        'Buyer',
        on_delete=models.CASCADE,
        verbose_name='Покупатель',
        related_name='buyers'
    )
    shop = models.ForeignKey(
        'Shop',
        on_delete=models.CASCADE,
        verbose_name='Магазин',
        related_name='shops'
    )
    bouquet = models.ForeignKey(
        'Bouquet',
        on_delete=models.CASCADE,
        verbose_name='Букет',
        related_name='bouquets'
    )
    is_consultation = models.BooleanField(
        'Нужна ли консультация'
    )
    comment = models.TextField(
        'Комментарий к заказу'
    )
    delivery_time = models.DateTimeField(
        'Дата и время заказа'
    )

    def __str__(self) -> str:
        order = f'{self.pk} {self.buyer.full_name}'
        return order

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
