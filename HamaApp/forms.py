from django.forms import ModelForm
from .models import Contact,Commentaire,Photos,Gestion,Mandat

class MandatForm(ModelForm):
    class Meta:
        model= Mandat
        fields= '__all__'


class ContactForm(ModelForm):
    class Meta:
        model= Contact
        fields= '__all__'


class CommentForm(ModelForm):
    class Meta:
        model= Commentaire
        fields= '__all__'



class ImageForm(ModelForm):
    class Meta:
        model= Photos
        fields='__all__'


class GestionForm(ModelForm):
    class Meta:
        model= Gestion
        fields='__all__'



#############################################################################
##############################################################################
'''
class DemandeForm(ModelForm):
    class Meta:
        model = Demande
        fields = '_all_'

class MAndatForm(ModelForm):
    class Meta:
        model = MAndat
        fields = '_all_'

class OffreForm(ModelForm):
    class Meta:
        model = Offre
        fields = '_all_'

class AchatForm(ModelForm):
    class Meta:
        model = Achat
        fields = '_all_'

class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = '_all_'

'''