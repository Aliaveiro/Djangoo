from django.db import models
import datetime

# Create your models here.
class Mandat(models.Model):
    Produit =models.CharField(max_length=100,null=True)
    Prix=models.CharField(max_length=100,null=False )
    date=models.DateField(("Date"), default=datetime.date.today)
    Honoraires=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.Produit


class Contact(models.Model):
    Prenom =models.CharField(max_length=100,null=True)
    Nom=models.CharField(max_length=100,null=False )
    Mail=models.CharField(max_length=100,null=True)
    Telephone=models.CharField(max_length=100,null=True)
    Societe=models.CharField(max_length=100,null=True)
    Adresse=models.CharField(max_length=100,null=True)
    CodePostale=models.CharField(max_length=100,null=True)
    Ville= models.CharField(max_length=100,null=True)
    Statut=models.CharField(max_length=100,null=True)
    CapitalSocial=models.CharField(max_length=100,null=True)
    NumRCS=models.CharField(max_length=100,null=True)
    VilleRCS=models.CharField(max_length=100,null=True)


    def __str__(self):
        return self.Nom


class Commentaire(models.Model):
    Titre = models.CharField(max_length=100,null=True)
    Description = models.TextField(max_length=10000,null=True )



    def __str__(self):
        return self.Titre

class Photos(models.Model):
    image = models.FileField()
    nom= models.CharField(max_length=100 , null=True)

    def __str__(self):
        return self.nom


class Gestion(models.Model):
    doc = models.FileField()
    nom= models.CharField(max_length=100 , null=True)

    def __str__(self):
        return self.nom



    ###########################################################
    ##########################################################



'''
#partie transaction

class Demande(models.Model):
    class Meta:
        pass

    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    resume = models.TextField()


class MAndat(models.Model):
    class Meta:
        pass

    product = models.ForeignKey(Produit, on_delete=models.CASCADE)
    prix = models.DecimalField(blank=True, max_digits=5, decimal_places=2)
    honoraire = models.DecimalField(blank=True, max_digits=5, decimal_places=2)
    date=models.DateField(default=datetime.date.today)

class Offre(models.Model):
    class Meta:
        pass

    product = models.ForeignKey(Produit, on_delete=models.CASCADE)


class Achat(models.Model):
    class Meta:
        pass

    offer = models.ForeignKey(Offre, on_delete=models.CASCADE)
    dateVisite = models.DateTimeField(default=timezone.now)
    honoraireHT = models.DecimalField(max_digits=5, decimal_places=2)
    honoraireTTC = models.DecimalField(max_digits=5, decimal_places=2)
    prixPropose = models.DecimalField(max_digits=5, decimal_places=2)
    indemnite = models.DecimalField(max_digits=5, decimal_places=2, default=5)
    activite = models.CharField(max_length=50)
    delaiValidite = models.DateTimeField(default=timezone.now)
     # conditions suspensives

    financement = models.BooleanField(default=False)
    montant = models.DecimalField(max_digits=5, decimal_places=2)
    taux = models.DecimalField(max_digits=5, decimal_places=2)
    duree = models.IntegerField()
    permisConstruction = models.BooleanField(default=False)
    droitPreemption = models.BooleanField(default=False)
    faculteSubstitution = models.BooleanField(default=False)

class Location(models.Model):
    class Meta:
        pass

    CHOIX_BAIL = (("DEROGATOIRE", "dérogatoire"), ("COMMERCIAL", "commercial"), ("PROFESSIONNEL", "professionnel"))

    offer = models.ForeignKey(Offre, on_delete=models.CASCADE)
    dateVisite = models.DateTimeField(default=timezone.now)
    honoraireHT = models.DecimalField(max_digits=5, decimal_places=2)
    honoraireTTC = models.DecimalField(max_digits=5, decimal_places=2)
    loyerPropose = models.DecimalField(max_digits=5, decimal_places=2)
    charges = models.DecimalField(max_digits=5, decimal_places=2)
    chargesAcquereur = models.BooleanField(default=False)
    chargesVendeur = models.BooleanField(default=False)
    bail = models.CharField(choices=CHOIX_BAIL, max_length=20, default=None)
    dureeBail = models.IntegerField()
    depotGranti = models.DecimalField(max_digits=5, decimal_places=2)
    taxeFrontiere = models.DecimalField(max_digits=5, decimal_places=2)
     # conditions suspensives

    financement = models.BooleanField(default=False)
    montant = models.DecimalField(max_digits=5, decimal_places=2)
    taux = models.DecimalField(max_digits=5, decimal_places=2)
    duree = models.IntegerField()
    permisConstruction = models.BooleanField(default=False)
    droitPreemption = models.BooleanField(default=False)
    faculteSubstitution = models.BooleanField(default=False)

'''
