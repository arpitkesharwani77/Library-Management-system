from django import forms
from django.core.exceptions import ValidationError
from datetime import date
from .models import Book


class BookForm(forms.Form):
    title = forms.CharField(max_length=200)
    author = forms.CharField(max_length=100)
    published_date = forms.DateField(
        widget=forms.widgets.DateInput(
            attrs={"type": "date", "min": date.today().strftime("%Y-%m-%d")}
        )
    )
    ISBN = forms.CharField(max_length=13)
    pages = forms.IntegerField()
    cover = forms.URLField(required=False)

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if not title or not title.strip() or len(title) < 5 or len(title) > 200:
            raise forms.ValidationError("Title must be between 2 and 200 characters.")
        return title

    def clean_author(self):
        author = self.cleaned_data.get("author")
        if not author or not author.strip() or len(author) < 5 or len(author) > 100:
            raise forms.ValidationError("Author must be between 2 and 100 characters.")
        return author

    def clean_published_date(self):
        published_date = self.cleaned_data.get("published_date")
        if not published_date:
            raise forms.ValidationError("Published date is required.")
        if published_date < date.today():
            raise forms.ValidationError("Published date cannot be in the past.")
        return published_date

    def clean_ISBN(self):
        ISBN = self.cleaned_data.get("ISBN")
        if len(ISBN) != 13:
            raise forms.ValidationError("ISBN must be 13 characters long.")
        return ISBN

    def clean_pages(self):
        pages = self.cleaned_data.get("pages")
        if not pages or pages <= 0:
            raise forms.ValidationError("Pages must be a positive number.")
        return pages

    def clean_cover(self):
        cover = self.cleaned_data.get("cover")
        if cover and not cover.startswith("http"):
            raise forms.ValidationError("Cover must be a valid URL.")
        return cover


class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "published_date", "ISBN", "pages", "cover"]
        widgets = {
            "published_date": forms.widgets.DateInput(
                attrs={"type": "date", "min": date.today().strftime("%Y-%m-%d")}
            ),
        }
