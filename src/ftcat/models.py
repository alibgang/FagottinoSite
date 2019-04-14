from django.db import models

# Create your models here.
class FT_Catalogue(models.Model):
    id = models.AutoField(primary_key=True)
    id_nr = models.CharField(max_length=50, blank=True, null=True)
    maker = models.CharField(max_length=100, null=True)
    instrument = models.CharField(max_length=100)
    provenance = models.CharField(max_length=150, null=True)
    date = models.CharField(max_length=50, null=True)
    current_location = models.CharField(max_length=300, null=True)
    status = models.CharField(max_length=100)
    transposition = models.CharField(max_length=20, blank=True, null=True)
    total_num_keys = models.CharField(max_length=20, blank=True, null=True)
    wingjoint_num_keys = models.CharField(max_length=100, blank=True, null=True)
    buttjoint_num_keys = models.CharField(max_length=50, blank=True, null=True)
    longjoint_num_keys = models.CharField(max_length=50, blank=True, null=True)
    num_pieces = models.CharField(max_length=20, blank=True, null=True)
    bocal = models.NullBooleanField(default=False, null=True)
    standing_leng_butt_bell =  models.CharField(max_length=20, blank=True, null=True)
    standing_leng_butt_wing =  models.CharField(max_length=20, blank=True, null=True)
    materials =  models.CharField(max_length=50, blank=True, null=True)
    makers_stamp_all =  models.CharField(max_length=300, blank=True, null=True)
    description =  models.CharField(max_length=700, blank=True, null=True)
    reg_num =  models.CharField(max_length=50, blank=True, null=True)
    website_url =  models.CharField(max_length=100, blank=True, null=True)
    measured_on_date =  models.CharField(max_length=20, blank=True, null=True)
    measured_by =  models.CharField(max_length=20, blank=True, null=True)
    reference =  models.CharField(max_length=350, blank=True, null=True)
    photos_videos =  models.CharField(max_length=70, blank=True, null=True)
    meas_basic_complete =  models.CharField(max_length=50, blank=True, null=True)
    meas_wing =  models.CharField(max_length=50, blank=True, null=True)
    meas_butt_small_bore =  models.CharField(max_length=50, blank=True, null=True)
    meas_butt_big_bore =  models.CharField(max_length=50, blank=True, null=True)
    meas_longjoint =  models.CharField(max_length=50, blank=True, null=True)
    meas_bell =  models.CharField(max_length=50, blank=True, null=True)
    meas_bocal =  models.CharField(max_length=50, blank=True, null=True)



    def __str__(self):
        return self.maker

class Misc_Catalogue(models.Model):
    id = models.AutoField(primary_key=True)
    id_nr = models.CharField(max_length=50, blank=True, null=True)
    maker = models.CharField(max_length=100, null=True)
    instrument = models.CharField(max_length=100)
    provenance = models.CharField(max_length=100, blank=True, null=True)
    date = models.CharField(max_length=50, null=True)
    current_location = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=100)
    transposition =  models.CharField(max_length=20, blank=True, null=True)
    total_num_keys =  models.CharField(max_length=20, blank=True, null=True)
    wingjoint_num_keys =  models.CharField(max_length=20, blank=True, null=True)
    buttjoint_num_keys =  models.CharField(max_length=20, blank=True, null=True)
    longjoint_num_keys =  models.CharField(max_length=20, blank=True, null=True)
    num_pieces =  models.CharField(max_length=20, blank=True, null=True)
    bocal = models.NullBooleanField(default=False, null=True)
    standing_leng_butt_bell =  models.CharField(max_length=50, blank=True, null=True)
    standing_leng_butt_wing =  models.CharField(max_length=50, blank=True, null=True)
    materials =  models.CharField(max_length=50, blank=True, null=True)
    makers_stamp_all =  models.CharField(max_length=50, blank=True, null=True)
    description =  models.CharField(max_length=500, blank=True, null=True)
    reg_num =  models.CharField(max_length=20, blank=True, null=True)
    website_url =  models.CharField(max_length=50, blank=True, null=True)
    measured_on_date =  models.CharField(max_length=50, blank=True, null=True)
    measured_by =  models.CharField(max_length=20, blank=True, null=True)
    reference =  models.CharField(max_length=200, blank=True, null=True)
    photos_videos =  models.CharField(max_length=100, blank=True, null=True)
    meas_basic_complete =  models.CharField(max_length=50, blank=True, null=True)
    meas_wing =  models.CharField(max_length=50, blank=True, null=True)
    meas_butt_small_bore =  models.CharField(max_length=50, blank=True, null=True)
    meas_butt_big_bore =  models.CharField(max_length=50, blank=True, null=True)
    meas_longjoint  =  models.CharField(max_length=50, blank=True, null=True)
    meas_bell =  models.CharField(max_length=50, blank=True, null=True)
    meas_bocal =  models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.maker

class RepertoireList(models.Model):
    id = models.AutoField(primary_key=True)
    composer = models.CharField(max_length=100, blank=True, null=True)
    title_sm_bsn_sections =models.CharField(max_length=200, blank=True, null=True)
    date_of_work = models.CharField(max_length=20, blank=True, null=True)
    genre = models.CharField(max_length=50, blank=True, null=True)
    suggested_instrument = models.CharField(max_length=50, blank=True, null=True)
    instr_range = models.CharField(max_length=100, blank=True, null=True)
    playability = models.TextField(max_length=500, blank=True, null=True)
    transposition = models.TextField(max_length=300, blank=True, null=True)
    notes = models.CharField(max_length=500, blank=True, null=True)
    
    def __str__(self):
        return self.composer


    #add a Reflections model to take in the reflections postings by team (through admin portal)