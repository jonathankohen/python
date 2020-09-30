from django.db import models


class BandManager(models.Manager):
    def bandValidator(self, postData):
        errors = {}
        name_filter = Band.objects.filter(name=postData['name'])
        if len(postData['name']) == 0:
            errors['name_req'] = "Band Name field is required."
        else:
            if len(name_filter) == 0:
                errors['no_match'] = "This band is not in the database. Please add it!"


class Band(models.Model):
    name = models.CharField(max_length=255)
    recs = models.ManyToMany
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BandManager()

# m2m with itself (bands)
# related name that makes sense
# band_recs (this band, ones it recommends), given_recs/rec_for
# start w/front-end that can search artists on spot
#
