from django.db import models
from comment.models import Comment
from django.urls import reverse_lazy
from django.contrib.contenttypes.fields import GenericRelation
from address.models import AddressField


class Agency(models.Model):
    name = models.CharField(max_length=255)
    comments = GenericRelation(Comment)
    data = models.JSONField(default=dict)

    feature_image = models.ForeignKey("default.Image", on_delete=models.SET_NULL, null=True)

    @property
    def description(self):
        return self.data.get("description", "no description yet...")

    @property
    def image(self):
        return self.data.get("image", "agency/128x128-agency.png")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy("house-detail", kwargs={"pk": self.pk})


class Branch(models.Model):
    address = AddressField()
    agency = models.ForeignKey("agency.Agency", on_delete=models.SET_NULL, null=True)
    comments = GenericRelation(Comment)
    data = models.JSONField(default=dict)

    feature_image = models.ForeignKey("default.Image", on_delete=models.SET_NULL, null=True)

    @property
    def description(self):
        return self.data.get("description", "no description yet...")

    @property
    def image(self):
        return self.data.get("image", "agency/128x128-branch.png")

    def __str__(self):
        return str(self.address)

    def get_absolute_url(self):
        return reverse_lazy("branch-detail", kwargs={"pk": self.pk, "agency-pk": self.agency.pk})


class Agent(models.Model):
    name = models.CharField(max_length=255)
    branches = models.ManyToManyField('agency.Branch')
    comments = GenericRelation(Comment)
    data = models.JSONField(default=dict)

    feature_image = models.ForeignKey("default.Image", on_delete=models.SET_NULL, null=True)

    @property
    def description(self):
        return self.data.get("description", "no description yet...")

    @property
    def image(self):
        return self.data.get("image", "agency/128x128-agent.png")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy("agent-detail", kwargs={"pk": self.pk})