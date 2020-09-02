from django import forms

class ActionTaskForm(forms.Form):

    option = forms.BooleanField(
        label = 'Deletar último registro',
        required=False
    )

    # deleteAll = forms.BooleanField(
    #     label = 'Deletar todos os registros',
    #     required=False
    # )

    def form_valid(self, form):
        option = form.cleaned_data['options']
        # deleteAll = form.cleaned_data['deleteAll']
        return super(ActionTaskForm, self).form_valid(form)


class IndexForm(forms.Form):
    report = forms.BooleanField(label='Exportar')

    def form_valid(self, form):
        report = form.cleaned_data['report']
        return super(ActionTaskForm, self).form_valid(form)