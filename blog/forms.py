from django import forms


class SignUpForm(forms.Form):
    name = forms.CharField(max_length=250, required=True, widget=forms.TextInput(attrs={
        "class": "form-username form-control",
        "id": "form-username",
        "placeholder": "Username..."
    }))
    email = forms.EmailField(max_length=200, required=True, widget=forms.TextInput(attrs={
        "class": "form-email form-control",
        "id": "form-email",
        "placeholder": "Email..."
    }))
    password = forms.CharField(required=True, widget=forms.Textarea(attrs={
        "style": "height:100px", "class": 'form-control my-input',
        "name": "password",
        "id": "password",
        "placeholder": "Password..."
    }))
    # class Meta:
    #     model = List
    #     fields = ["name", "title", "content"]


class SignInForm(forms.Form):
    email = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={
        "class": 'form-control my-input',
        "name": "email",
        "id": "email",
        "placeholder": "Email"
    }))
    password = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={
        "class": "form-last-name form-control",
        "id": "form-last-name",
        "placeholder": "Password"
    }))


class AddForm(forms.Form):
    title = forms.CharField(max_length=250, required=True, widget=forms.TextInput(attrs={
        "class": "form-control",
        "data - validation - required - message": "Please enter your name.",
        "id": "name",
        "placeholder": "Name",
        "name": "title"

    }))
    subtext = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={
        "style": "height:100px",
        "class": 'form-control',
        "data-validation-required-message": "Please enter a brief summary",
        "id": "subtext",
        "placeholder": "Summary",
        "name": "subtext"
    }))
    category = forms.ChoiceField(choices=[('education', 'Education'), ('technology', 'Technology')], widget=forms.Select(attrs={
        "class": 'form-control',
        "id": "message",
        "placeholder": "Select",
        "data-validation-required-message": "Please select a category",
        "name": "content"
                                 }))
    content = forms.CharField(max_length=255, required=True, widget=forms.Textarea(attrs={
        "style": "height:200px",
        "class": 'form-control',
        "id": "message",
        "placeholder": "Your post goes here...",
        "data-validation-required-message": "Please enter your post",
        "name": "content"
    }))


class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=250, required=True, widget=forms.TextInput(attrs={
        "class": "form-control",
        "data - validation - required - message": "Please enter your name.",
        "id": "name",
        "placeholder": "Name"

    }))
    email = forms.EmailField(max_length=200, required=True, widget=forms.TextInput(attrs={
        "class": 'form-control',
        "data-validation-required-message": "Please enter your email address",
        "id": "email",
        "placeholder": "Email Address"
    }))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={
        "style": "height:100px",
        "rows": "5",
        "class": 'form-control',
        "id": "message",
        "placeholder": "Your message goes here...",
        "data-validation-required-message": "Please enter a message",
    }))

