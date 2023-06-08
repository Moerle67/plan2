from django.db import models
from django.urls import reverse

# Create your models here.
class Mitarbeiter(models.Model):
    name = models.CharField("Name", max_length=100)
    kuerzel = models.CharField("Kürzel", max_length=10, primary_key=True)   

    class Meta:
        verbose_name = "Mitarbeiter"
        verbose_name_plural = "Mitarbeiter"

    def __str__(self):
        return f"{self.kuerzel} - {self.name}"

    def get_absolute_url(self):
        return reverse("Mitarbeiter_detail", kwargs={"pk": self.pk})

class Abteilung(models.Model):
    name = models.CharField(verbose_name="Abteilung", max_length=50)
    beschreibung = models.TextField(verbose_name="Beschreibung")
    class Meta:
        verbose_name = "Abteilung"
        verbose_name_plural = "Abteilungen"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Abteilung_detail", kwargs={"pk": self.pk})
class Ausbildungsberuf(models.Model):
    name = models.CharField("Beruf", max_length=50)
    details = models.CharField("detailiert Beruf", max_length=50)
    abteilung = models.ForeignKey(Abteilung, verbose_name="Abteilung", on_delete=models.RESTRICT)
    beschreibung = models.TextField("Beschreibung", blank=True)

    class Meta:
        verbose_name = "Ausbildungsberuf"
        verbose_name_plural = "Ausbildungsberufe"

    def __str__(self):
        return f"{self.name}/{self.abteilung.name}"

    def get_absolute_url(self):
        return reverse("Ausbildungsberuf_detail", kwargs={"pk": self.pk})
class Schlagwort(models.Model):
    name = models.CharField("Schlagwort", max_length=50, unique=True)
    class Meta:
        verbose_name = "Schlagwort"
        verbose_name_plural = "Schlagwörter"
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
class Lernfeld(models.Model):
    name = models.CharField("Lernfeld Nr:", max_length=10)
    inhalt = models.CharField("Inhalt", max_length=100)
    beschreibung = models.TextField("Beschreibung")
    stunden_jahr1 = models.IntegerField("Anzahl der Stunden (1.Jahr)")
    stunden_jahr2 = models.IntegerField("Anzahl der Stunden (2.Jahr)")
    stunden_jahr3 = models.IntegerField("Anzahl der Stunden (3.Jahr)")
    berufe = models.ManyToManyField(Ausbildungsberuf, verbose_name="Berufe")

    class Meta:
        verbose_name = "Lernfeld"
        verbose_name_plural = "Lernfelder"
        ordering = ['name']

    def __str__(self):
        str_beruf = ""
        ds_berufe = self.berufe.all()
        for beruf in ds_berufe:
            str_beruf += beruf.name +"/"    
        return f"LF {self.name} '{self.inhalt}' - {str_beruf[:-1]}"

    def get_absolute_url(self):
        return reverse("Lernfeld_detail", kwargs={"pk": self.pk})
class Lernbaustein(models.Model):
    nummer = models.CharField("Nummer", max_length=10)
    lernfeld = models.ForeignKey(Lernfeld, verbose_name="Lernfeld", on_delete=models.RESTRICT)
    schlagwoerter = models.ManyToManyField(Schlagwort, verbose_name="Schlagwörter")
    beschreibung = models.TextField("Beschreibung")
    stunden = models.IntegerField("Stunden", default=0)
    class Meta:
        verbose_name = "Lernbaustein"
        verbose_name_plural = "Lernbausteine"
        ordering = ['lernfeld__name', 'nummer']

    def __str__(self):
        string = ""
        ds = self.schlagwoerter.all()
        for element in ds:
            string += element.name +", "
        if len(string)>1:
            string = string[:-2]
        return f"LB {self.lernfeld.name}/{self.nummer} - {string} ({self.lernfeld})"

    def get_absolute_url(self):
        return reverse("Lernbaustein_detail", kwargs={"pk": self.pk})
    
class Sequenz(models.Model):
    name = models.CharField("Name", max_length=50)
    bemerkung = models.TextField("Eräuterungen")
    lernbausteine = models.ManyToManyField(Lernbaustein, verbose_name="Lernbausteine") 
    stunden = models.IntegerField("Geplante Stunden")
    mitarbeiter = models.ForeignKey(Mitarbeiter, verbose_name="Mitarbeiter", on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "Sequenz"
        verbose_name_plural = "Sequenzen"

    def __str__(self):
        # string = self.lernbausteine.all().values_list("lernfeld").join(", ")
        string = ""
        ds = self.lernbausteine.all()
        for element in ds:
            string += str(element.lernfeld) +", "
        if len(string)>1:
            string = string[:-2]
        return f"{self.name}/{self.stunden} Stunden, {string}"

    def get_absolute_url(self):
        return reverse("Sequenz_detail", kwargs={"pk": self.pk})
