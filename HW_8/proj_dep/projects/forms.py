from django import forms


# класс форм, не связанных с моделью
class ContactForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    def form_valid(self, form):
        # print(form.cleaned_data)
        return super().form_valid(form)