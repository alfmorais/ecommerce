from django.contrib.auth.models import User
from django.db import models

# from django.urls import reverse


class Category(models.Model):
    name = models.CharField(
        verbose_name="Nome da Categoria",
        max_length=255,
        db_index=True,
    )
    slug = models.SlugField(
        verbose_name="Slug da Categoria",
        max_length=255,
        unique=True,
    )

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    # def get_absolute_url(self):
    #    return reverse("store:category_list", args=[self.slug])

    def __str__(self) -> str:
        return f"{self.name}"


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        related_name="product",
        on_delete=models.CASCADE,
    )
    created_by = models.ForeignKey(
        User,
        related_name="product_creator",
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        verbose_name="Titulo do Produto",
        max_length=255,
    )
    author = models.CharField(
        verbose_name="Autor do Produto",
        max_length=255,
        default="admin",
    )
    description = models.TextField(
        verbose_name="Descrição do Produto",
        blank=True,
    )
    image = models.ImageField(
        verbose_name="Imagem do Produto",
        upload_to="images/",
    )
    slug = models.SlugField(
        verbose_name="Slug do Produto",
        max_length=255,
        unique=True,
    )
    price = models.DecimalField(
        verbose_name="Preço do Produto", max_digits=4, decimal_places=2
    )
    in_stock = models.BooleanField(
        verbose_name="Produto em Estoque?",
        default=True,
    )
    is_active = models.BooleanField(
        verbose_name="Produto está ativo?",
        default=True,
    )
    created = models.DateTimeField(
        verbose_name="Data de Criação",
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        verbose_name="Data de Atualização",
        auto_now=True,
    )

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ("-created",)

    def __str__(self) -> str:
        return f"{self.title}"
