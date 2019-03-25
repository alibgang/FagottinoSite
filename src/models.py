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
    bocal = models.BooleanField(default=False, null=True)
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
    bocal = models.BooleanField(default=False, null=True)
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

class JointLengths(models.Model):
	id_nr = models.CharField(max_length=20,blank=True,null=True)
	standinglengthtobell = models.CharField(max_length=20,blank=True,null=True)
	standinglengthtowingjoint=models.CharField(max_length=20,blank=True,null=True)
	wingjointlength=models.CharField(max_length=20,blank=True,null=True)
	wingjointtenonlen=models.CharField(max_length=20,blank=True,null=True)
	buttjointlength=models.CharField(max_length=20,blank=True,null=True)
	longjointlength=models.CharField(max_length=20,blank=True,null=True)
	longjointsouthtenonlength=models.CharField(max_length=20,blank=True,null=True)
	longjointnorthtenonlength=models.CharField(max_length=20,blank=True,null=True)
	belllength=models.CharField(max_length=20,blank=True,null=True)
	ventholedistancefromnorth=models.CharField(max_length=20,blank=True,null=True)
	ventholeapproxdiameter=models.CharField(max_length=20,blank=True,null=True)

	def __str__(self):
		return self.id_nr
		
class ToneholeDistanceAxis(models.Model):
	id_nr = models.CharField(max_length=20,blank=True,null=True)
	wingtonehole1distancfromnorth=models.CharField(max_length=20,blank=True,null=True)
	wingtonehole2distancefromnorth=models.CharField(max_length=20,blank=True,null=True)
	wingtonehole3distancefromnorth=models.CharField(max_length=20,blank=True,null=True)
	butttonehole4distancefromnorth=models.CharField(max_length=20,blank=True,null=True)
	butttonehole5distancefromnorth=models.CharField(max_length=20,blank=True,null=True)
	butttonehole6distancefromnorth=models.CharField(max_length=20,blank=True,null=True)
	butttoneholefdistancefromnorth=models.CharField(max_length=20,blank=True,null=True)
	butttoneholeedistancefromnorth=models.CharField(max_length=20,blank=True,null=True)
	butttoneholeabdistancefromnorth=models.CharField(max_length=20,blank=True,null=True)
	butttoneholefisdistancefromnorth=models.CharField(max_length=20,blank=True,null=True)
	longjointtoneholeddistancefromnorth=models.CharField(max_length=20,blank=True,null=True)
	longjointtoneholeebdistancefromnorth=models.CharField(max_length=20,blank=True,null=True)
	longjointtoneholecdistancefromnorth=models.CharField(max_length=20,blank=True,null=True)
	longjointtoneholebbdistancefromnorth=models.CharField(max_length=20,blank=True,null=True)
	wingmajoraxistonehole1=models.CharField(max_length=20,blank=True,null=True)
	wingmajoraxistonehole2=models.CharField(max_length=20,blank=True,null=True)
	wingmajoraxistonehole3=models.CharField(max_length=20,blank=True,null=True)
	buttmajoraxiss2stonehole4=models.CharField(max_length=20,blank=True,null=True)
	buttminoraxisf2btonehole4=models.CharField(max_length=20,blank=True,null=True)
	buttmajoraxiss2stonehole5=models.CharField(max_length=20,blank=True,null=True)
	buttminoraxisf2btonehole5=models.CharField(max_length=20,blank=True,null=True)
	buttmajoraxiss2stonehole6=models.CharField(max_length=20,blank=True,null=True)
	buttminoraxisf2btonehole6=models.CharField(max_length=20,blank=True,null=True)
	buttmajoraxiss2stoneholef=models.CharField(max_length=20,blank=True,null=True)
	buttminoraxisf2btoneholef=models.CharField(max_length=20,blank=True,null=True)
	buttmajoraxiss2stoneholee=models.CharField(max_length=20,blank=True,null=True)
	buttminoraxisf2btoneholee=models.CharField(max_length=20,blank=True,null=True)
	buttmajoraxiss2softhebottombuttellipse=models.CharField(max_length=20,blank=True,null=True)
	buttminoraxisf2bofthebottombuttellipse=models.CharField(max_length=20,blank=True,null=True)
	buttmajoraxiss2softhetopbuttellipse=models.CharField(max_length=20,blank=True,null=True)
	buttminoraxisf2bofthetopbuttellipse=models.CharField(max_length=20,blank=True,null=True)
	longjointminoraxisf2btoneholed=models.CharField(max_length=20,blank=True,null=True)
	longjointmajoraxiss2stoneholed=models.CharField(max_length=20,blank=True,null=True)
	longjointminoraxisf2btoneholeeb=models.CharField(max_length=20,blank=True,null=True)
	longjointmajoraxiss2stoneholeeb=models.CharField(max_length=20,blank=True,null=True)
	longjointminoraxisf2btoneholec=models.CharField(max_length=20,blank=True,null=True)
	longjointmajoraxiss2stoneholec=models.CharField(max_length=20,blank=True,null=True)
	longjointminoraxisf2btoneholebb=models.CharField(max_length=20,blank=True,null=True)
	longjointmajoraxiss2stoneholebb=models.CharField(max_length=20,blank=True,null=True)
	
	def __str__(self):
		return self.id_nr
		
		
class ToneholeAngleDiamLengthOut(models.Model):
	id_nr = models.CharField(max_length=20,blank=True,null=True)
	wingtonehole1angle = models.CharField(max_length=20,blank=True,null=True)
	wingtonehole2angle = models.CharField(max_length=20,blank=True,null=True)
	wingtonehole3angle = models.CharField(max_length=20,blank=True,null=True)
	wingtonehole1approxdiam = models.CharField(max_length=20,blank=True,null=True)
	wingtonehole2approxdiam = models.CharField(max_length=20,blank=True,null=True)
	wingtonehole3approxdiam = models.CharField(max_length=20,blank=True,null=True)
	wingtonehole1approxlength = models.CharField(max_length=20,blank=True,null=True)
	wingtonehole2approxlength = models.CharField(max_length=20,blank=True,null=True)
	wingtonehole3approxlength = models.CharField(max_length=20,blank=True,null=True)
	butttonehole4angle = models.CharField(max_length=20,blank=True,null=True)
	butttonehole5angle = models.CharField(max_length=20,blank=True,null=True)
	butttonehole6angle = models.CharField(max_length=20,blank=True,null=True)
	butttoneholeeangle = models.CharField(max_length=20,blank=True,null=True)
	butttonehole4approxdiam = models.CharField(max_length=20,blank=True,null=True)
	butttonehole5approxdiam = models.CharField(max_length=20,blank=True,null=True)
	butttonehole6approxdiam = models.CharField(max_length=20,blank=True,null=True)
	butttoneholeeapproxdiam = models.CharField(max_length=20,blank=True,null=True)
	butttonehole4approxlength = models.CharField(max_length=20,blank=True,null=True)
	butttonehole5approxlength = models.CharField(max_length=20,blank=True,null=True)
	butttonehole6approxlength = models.CharField(max_length=20,blank=True,null=True)
	butttoneholeeapproxlength = models.CharField(max_length=20,blank=True,null=True)
	buttcorkmajoraxiss2s = models.CharField(max_length=20,blank=True,null=True)
	buttcorkminoraxisf2b = models.CharField(max_length=20,blank=True,null=True)
	longjointtoneholecangle = models.CharField(max_length=20,blank=True,null=True)
	longjointtoneholecdiam = models.CharField(max_length=20,blank=True,null=True)
	longjointtoneholecapproxlength = models.CharField(max_length=20,blank=True,null=True)

	def __str__(self):
		return self.id_nr	
	
class InnerBoreLength(models.Model):
	id_nr = models.CharField(max_length=20,blank=True,null=True)
	borelen = models.CharField(max_length=20,blank=True,null=True)
	wingborelength = models.CharField(max_length=20,blank=True,null=True)
	buttsmallborelength = models.CharField(max_length=20,blank=True,null=True)
	buttbigborelength = models.CharField(max_length=20,blank=True,null=True)
	buttsmallboresocketlength = models.CharField(max_length=20,blank=True,null=True)
	buttbigboresocketlength = models.CharField(max_length=20,blank=True,null=True)
	buttsmallborebeginningofseptum = models.CharField(max_length=20,blank=True,null=True)
	buttbigborebeginningofseptum = models.CharField(max_length=20,blank=True,null=True)
	longjointlength = models.CharField(max_length=20,blank=True,null=True)
	belllength = models.CharField(max_length=20,blank=True,null=True)

	def __str__(self):
		return self.id_nr


class InnerBoreBeginningDiamNotSocket(models.Model):
	id_nr = models.CharField(max_length=20,blank=True,null=True)		
	wingborediamnorth = models.CharField(max_length=20,blank=True,null=True)
	wingborediamsouth = models.CharField(max_length=20,blank=True,null=True)
	bocalwelllength = models.CharField(max_length=20,blank=True,null=True)
	buttsmallborediamnorth = models.CharField(max_length=20,blank=True,null=True)
	buttbigborediamnorth = models.CharField(max_length=20,blank=True,null=True)
	longjointdiamnorth = models.CharField(max_length=20,blank=True,null=True)
	longjointdiamsouth = models.CharField(max_length=20,blank=True,null=True)
	bellborediamnorth = models.CharField(max_length=20,blank=True,null=True)
	bellborediamsouth = models.CharField(max_length=20,blank=True,null=True)
	bellsocketlength = models.CharField(max_length=20,blank=True,null=True)
	bocaldiamatbeginning = models.CharField(max_length=20,blank=True,null=True)
	bocalthicknessatbeginning = models.CharField(max_length=20,blank=True,null=True)
	bocaldiamattenon = models.CharField(max_length=20,blank=True,null=True)
	bocalthicknessattenon = models.CharField(max_length=20,blank=True,null=True)
	bocallengthalongtop = models.CharField(max_length=20,blank=True,null=True)


	def __str__(self):
		return self.id_nr
		
class CompleteOutside(models.Model):
	id_nr = models.CharField(max_length=20,blank=True,null=True)
	bocalwellthicknesswithferrule = models.CharField(max_length=20,blank=True,null=True)
	bocalwellferrulethickness = models.CharField(max_length=20,blank=True,null=True)
	wingtenonthickness = models.CharField(max_length=20,blank=True,null=True)
	wingtenonnorthexterndiam = models.CharField(max_length=20,blank=True,null=True)
	wingtenonsouthexterndiam = models.CharField(max_length=20,blank=True,null=True)
	wingtoneholeadistancefromnorth = models.CharField(max_length=20,blank=True,null=True)
	wingtoneholeaangle = models.CharField(max_length=20,blank=True,null=True)
	wingtoneholeaapproxdiam = models.CharField(max_length=20,blank=True,null=True)
	wingtoneholeaapproxlength = models.CharField(max_length=20,blank=True,null=True)
	wingtoneholecdistancefromnorth = models.CharField(max_length=20,blank=True,null=True)
	wingtoneholecangle = models.CharField(max_length=20,blank=True,null=True)
	wingtoneholecapproxdiam = models.CharField(max_length=20,blank=True,null=True)
	wingtoneholecapproxlength = models.CharField(max_length=20,blank=True,null=True)
	buttbigsocketthicknesswithferrule = models.CharField(max_length=20,blank=True,null=True) 
	buttsmallsocketthicknesswithferrule = models.CharField(max_length=20,blank=True,null=True)
	butttopferrulethickness = models.CharField(max_length=20,blank=True,null=True)
	minimumwallthicknessbetweenbuttsockets = models.CharField(max_length=20,blank=True,null=True)
	buttwoodspacebetweencorksbottom = models.CharField(max_length=20,blank=True,null=True)
	buttbigborecorkdiambottom = models.CharField(max_length=20,blank=True,null=True)
	buttsmallborecorkdiambottom = models.CharField(max_length=20,blank=True,null=True)
	buttwoodwallbetweencorkfrontsmallbore = models.CharField(max_length=20,blank=True,null=True)
	buttwoodwallbetweencorkfrontbigbore = models.CharField(max_length=20,blank=True,null=True)
	buttwoodwallbetweencorkbacksmallbore = models.CharField(max_length=20,blank=True,null=True)
	buttwoodwallbetweencorkbackbigbore = models.CharField(max_length=20,blank=True,null=True)
	woodwallbetweencorksidesmallbore = models.CharField(max_length=20,blank=True,null=True)
	woodwallbetweencorksidebigbore = models.CharField(max_length=20,blank=True,null=True)
	buttbottomferrulethickness = models.CharField(max_length=20,blank=True,null=True)
	longjointsouthtenonthickness = models.CharField(max_length=20,blank=True,null=True)
	longjointsouthtenonnorthernexterndiam = models.CharField(max_length=20,blank=True,null=True)
	longjointsouthtenonsouthernexterndiam = models.CharField(max_length=20,blank=True,null=True)
	longjointnorthtenonthickness = models.CharField(max_length=20,blank=True,null=True)
	longjointnorthtenonnorthernexterndiam = models.CharField(max_length=20,blank=True,null=True)
	longjointnorthtenonsouthernexterndiam = models.CharField(max_length=20,blank=True,null=True)
	bellsocketthicknesswithbrass = models.CharField(max_length=20,blank=True,null=True)
	brassthicknessofbellferrule = models.CharField(max_length=20,blank=True,null=True)
	bellferruleheight = models.CharField(max_length=20,blank=True,null=True)
	
	def __str__(self):
		return self.id_nr
		
class ToneHoleAngleDiamLengthIn(models.Model):
	id_nr = models.CharField(max_length=20,blank=True,null=True)
	butttoneholeabangle = models.CharField(max_length=20,blank=True,null=True)
	butttoneholefangle = models.CharField(max_length=20,blank=True,null=True)
	butttoneholefisangle = models.CharField(max_length=20,blank=True,null=True)
	butttoneholeabapproxdiam = models.CharField(max_length=20,blank=True,null=True)
	butttoneholefapproxdiam = models.CharField(max_length=20,blank=True,null=True)
	butttoneholefisapproxdiam = models.CharField(max_length=20,blank=True,null=True)
	butttoneholeabapproxlength = models.CharField(max_length=20,blank=True,null=True)
	butttoneholefapproxlength = models.CharField(max_length=20,blank=True,null=True)
	butttoneholefisapproxlength = models.CharField(max_length=20,blank=True,null=True)
	longjointtoneholed_angle = models.CharField(max_length=20,blank=True,null=True)
	longjointtonehole_eb_angle = models.CharField(max_length=20,blank=True,null=True)
	longjointtonehole_bb_angle = models.CharField(max_length=20,blank=True,null=True)
	longjointtonehole_d_approxdiam = models.CharField(max_length=20,blank=True,null=True)
	longjointtonehole_eb_approxdiam = models.CharField(max_length=20,blank=True,null=True)
	longjointtonehole_bb_approxdiam = models.CharField(max_length=20,blank=True,null=True)
	longjointtonehole_d_approxlength = models.CharField(max_length=20,blank=True,null=True)
	longjointtonehole_eb_approxlength = models.CharField(max_length=20,blank=True,null=True)
	longjointtonehole_bb_approxlength = models.CharField(max_length=20,blank=True,null=True)
	
	def __str__(self):
		return self.id_nr
		
class CompleteInside(models.Model):
	#id_nr = models.ForeignKey('FT_Catalogue')
    id_nr = models.CharField(max_length=20,blank=True,null=True)
    wingtonehole1distancefromsouth = models.CharField(max_length=20,blank=True,null=True)
    wingtonehole2distancefromsouth = models.CharField(max_length=20,blank=True,null=True)
    wingtonehole3distancefromsouth = models.CharField(max_length=20,blank=True,null=True)
    wingtonehole_a_distancefromsouth = models.CharField(max_length=20,blank=True,null=True)
    wingtonehole_c_distancefromsouth = models.CharField(max_length=20,blank=True,null=True)
    butttonehole_4_distancefromnorth = models.CharField(max_length=20,blank=True,null=True)
    butttonehole_5_distancefromnorth = models.CharField(max_length=20,blank=True,null=True)
    butttonehole_6_distancefromnorth = models.CharField(max_length=20,blank=True,null=True)
    butttonehole_ab_distancefromnorth = models.CharField(max_length=20,blank=True,null=True)
    butttonehole_f_distancefromnorth = models.CharField(max_length=20,blank=True,null=True)
    butttonehole_fis_distancefromnorth = models.CharField(max_length=20,blank=True,null=True)
    butttonehole_e_distancefromnorth = models.CharField(max_length=20,blank=True,null=True)
    longjointtonehole_d_distancefromnorth = models.CharField(max_length=20,blank=True,null=True)
    longjointtonehole_eb_distancefromnorth = models.CharField(max_length=20,blank=True,null=True)
    longjointtonehole_c_distancefromnorth = models.CharField(max_length=20,blank=True,null=True)
    longjointhole_bb_distancefromnorth = models.CharField(max_length=20,blank=True,null=True)
    bellventholedistancefromnorth = models.CharField(max_length=20,blank=True,null=True)
	
    def __str__(self):
        return self.id_nr


    #add a Reflections model to take in the reflections postings by team (through admin portal)