from django.http import HttpResponseRedirect, FileResponse
from .models import Mandat,Contact, Gestion, Photos, Commentaire
from django.shortcuts import render
from .forms import CommentForm, ImageForm, ContactForm, GestionForm, MandatForm
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


# Create your views here.
def pdf_mandat(request):
    def drawMyRuler(c):
        c.drawString(100, 10, 'X100')
        c.drawString(200, 10, 'X200')
        c.drawString(300, 10, 'X300')
        c.drawString(400, 10, 'X400')
        c.drawString(500, 10, 'X500')

        c.drawString(10, 100, 'y100')
        c.drawString(10, 200, 'y200')
        c.drawString(10, 300, 'y300')
        c.drawString(10, 400, 'y400')
        c.drawString(10, 500, 'y500')
        c.drawString(10, 600, 'y600')
        c.drawString(10, 700, 'y700')

    title1 = 'Inscription au Registre des Mandats COURCIER IMMOBILIER N°  '
    title2 = 'MANDAT DE VENTE AVEC EXCLUSIVITE'

    subtitle = 'ENTRE LES SOUSSIGNES :'
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    c.setTitle("MANDAT DE VENTE ")
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    c.drawString(2, 10, title1)
    textob.setFont("Helvetica", 27)
    c.drawString(50, 50, title2)
    textob.setFont("Helvetica", 8)
    c.drawString(2, 80, subtitle)
    c.line(2, 82, 153, 82)
    c.drawString(2, 100, paragh)
    drawMyRuler(c)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='mandat.pdf')


def mandat(request):
    form = MandatForm()
    if request.method == 'POST':
        form = MandatForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('mandat')
    else:
        form = MandatForm()
    dataMandat = Mandat.objects.all()

    context = {'form': form, 'dataMandat': dataMandat}

    return render(request, 'mandat.html', context)



def home(request):
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'Comment.html', context)


def index(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'Contact.html', context)


def photos(request):
    # Contacts= Contact.objects.all()
    # context={'Contacts':Contacts}

    if request.method == 'POST':

        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('photos')

    else:
        form = ImageForm()
    dataImage = Photos.objects.all()

    context = {'form': form, 'dataImage': dataImage}

    return render(request, 'mage.html', context)


def gestion(request):
    if request.method == 'POST':

        form = GestionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('gestion')

    else:
        form = GestionForm()
    dataGestion = Gestion.objects.all()
    context = {'form': form, 'dataGestion': dataGestion}

    return render(request, 'GED.html', context)


def delete_gestion(request, nom):
    gestion = Gestion.objects.get(pk=nom)
    gestion.delete()
    print("dedee")
    return HttpResponseRedirect('gestion')


def pdf(request):
    mandatt = Mandat.objects.all()
    context = {
        "first_name": "Anjaneyulu",
        "last_name": "Batta",
        "address": "Hyderabad, India"
    }
    return render(request, 'pdf.html', context)
#estimVenale


######################################################################
#########################################################################
'''

def choixis(choix2):
    global choix1
    choix1 = choix2


def choixis2(choix2):
    global choix_prod
    choix_prod = choix2


# Create your views here.

def formDemande(request):
    Demande = DemandeForm()

    if (request.method == "POST"):
        form = DemandeForm(request.POST)

        if form.is_valid():
            form.save()
            print("done")

        else:
            print(form.errors)

    else:
        print("button not save")

    con = {'Demande': Demande}
    return render(request, 'demande.html', con)


def formMandat(request):
    Mandat1 = MandatForm()
    global prix, honoraire, choix, date1, date2
    choix = Produit.objects.last()
    prix = 0
    honoraire = 0
    date1 = datetime.now()
    date2 = date1.strftime("%Y-%m-%d")

    if (request.method == "POST" and "prod" in request.POST):
        print("hi")
        prod = request.POST.get('product')
        print(prod)
        choix = Produit.objects.get(pk=prod)
        prix = choix.prixAffiche
        honoraire = choix.honoraire
        data1 = {'Mandat': Mandat1,
                 'prix': prix,
                 'honoraire': honoraire,
                 'date': date2
                 }
        return render(request, 'mandat.html', data1)

    elif (request.method == "POST" and "mandat" in request.POST):
        print("hello")

        mandat_tab = Mandat()
        mandat_tab.product = choix
        mandat_tab.prix = prix
        mandat_tab.honoraire = honoraire
        mandat_tab.date = date2
        mandat_tab.save()
        print("saved1")
        data2 = {'Mandat': Mandat1,
                 }
        return render(request, 'mandat.html', data2)
    else:
        print("button not save")
    print('perfecto')
    con = {'Mandat': Mandat1,
           }
    return render(request, 'mandat.html', con)


def formOffre(request):
    Offre1 = OffreForm()
    # Produit = ProductForm()
    Achat_f = AchatForm()
    Location_f = LocationForm()
    location_tab = Location()
    achat_tab = Achat()
    global choix1, choix_prod
    """
    default_dataL = {'offer': Offre.objects.last(), 'dateVisite' : timezone.now, 
                     'honoraireHT' : 0, 'honoraireTTC' : 0, 'loyerPropose': 0, 
                     'charges' : 0, 'chargesAcquereur' : False, 
                     'chargesVendeur' : False, 'bail' : None, 'dureeBail' : 0, 
                     'depotGranti': 0, 'taxeFrontiere' : 0, 'financement': False, 
                     'montant' : 0, 'taux' : 0, 'duree' : 0, 
                     'permisConstruction' : False, 'droitPreemption' : False, 
                     'faculteSubstitution': False
                     }
    """

    if (request.method == "POST" and 'offre' in request.POST):
        prod = request.POST.get('product')
        print(prod)
        choix3 = Produit.objects.get(pk=prod)
        choix = choix3.categorie
        print("le choix est " + choix)
        # choix = Produit.objects.get('TypeBien'==  Offre.product.TypeBien )
        # print("choix" + choix)

        offre_tab = Offre()
        offre_tab.product = choix3
        offre_tab.save()

        print("done")

        context = {'Offre': Offre1,
                   'choix': choix,
                   'Achat': Achat_f,
                   'Location': Location_f,
                   }

        choixis(choix)
        choixis2(choix3)

        # formchoix1 = formchoix
        return render(request, 'offre.html', context)




    elif (request.method == "POST" and 'send' in request.POST):
        print("hey")
        if (choix1 == 'LOCATION'):
            # formchoix = LocationForm(request.POST or None)
            """"location_tab.offer = Offre.objects.last()
            location_tab.dateVisite = request.POST.get('dateVisite')
            location_tab.honoraireHT = """

            print("okay")
        elif (choix1 == 'VENTE'):
            formchoix = AchatForm(request.POST)
        # if formchoix1 != NULL:
        if formchoix.is_valid():
            formchoix.save()
        #  print(choix + ' Bien enregistré ')
        else:
            print(" failed xD")
            print(formchoix.errors)

    # else:
    # print("form null ")
    else:
        print("button not save")
    con = {'Offre': Offre1,
           }
    return render(request, 'offre.html', con)
    
'''

