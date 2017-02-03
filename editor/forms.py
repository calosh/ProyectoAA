from django import forms
from .models import Codigo


inicial = '''public class Main{
    public static void main(String args[]){
        System.out.println("Hola Mundito!!!!");
    }
}
'''

LENGUAJES = ( 
    ('java', 'Java'), 
    ('python', 'Python'), 
    ('c', 'C'),
    ('cpp', 'C++'),
) 

class MyForm(forms.Form):
    codeeditor = forms.CharField(widget=forms.Textarea(attrs={"id":"codeeditor"}), label="", initial=inicial)
    # http://stackoverflow.com/questions/26726500/how-do-i-check-a-radio-button-value-using-django-radioselect-widget
    lenguaje = forms.ChoiceField(widget=forms.RadioSelect(attrs={"id":"lenguaje"}), choices=LENGUAJES, initial='java')
    nombre = forms.CharField(required=False)
    nombre.widget = forms.TextInput(attrs={'name': "nombre", 'type':'text', 'class':"form-control", 'placeholder':'Nombre del codigo'})

    class Meta:
        model = Codigo



class CodigoForm(forms.ModelForm):
    nombre = forms.CharField(required=False)
    nombre.widget = forms.TextInput(attrs={'name': "nombre", 'type':'text', 'class':"form-control", 'placeholder':'Nombre del codigo'})
    codigo = forms.CharField(widget=forms.Textarea(attrs={"id":"codigo"}), label="", initial=inicial)
    tipo = forms.ChoiceField(widget=forms.RadioSelect(attrs={"id":"tipo"}), choices=LENGUAJES, initial='java')
    class Meta:
        model = Codigo
        exclude = ('usuario','slug','publ_priv')