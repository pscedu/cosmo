from django.db import models


class Simulation(models.Model):
    name = models.CharField(max_length=64, default="")

    @property
    def alternative_name(self):
        return "BT"

    @property
    def side_length_of_simulation_box(self):
        return 400

    @property
    def dark_matter_particle_mass(self):
        return "1.19639x10^7"

    @property
    def gas_matter_particle_mass(self):
        return "2.36222x10^6"

    @property
    def number_of_dark_matter_particles(self):
        return 348913664000

    @property
    def number_of_gas_particles(self):
        return 348913664000

    @property
    def start_redshift(self):
        return 99

    @property
    def end_redshift(self):
        return 6.56

    @property
    def cosmology(self):
        return "WMAP-9"

    @property
    def total_matter_density(self):
        return 0.2814

    @property
    def dark_energy_density(self):
        return 0.7186

    @property
    def baryonic_matter_density(self):
        return 0.0464

    @property
    def hubble_param(self):
        return 0.697

    @property
    def gas_cooling(self):
        return "Radiative cooling (primordial + metal line)"

    @property
    def star_formation(self):
        return "Multi-phase SF model (SH03) + molecular based SF (Okamoto2010)"

    @property
    def stellar_feedback(self):
        return "Type-II SN wind feedback"

    @property
    def agn_formation_accretion_feedback(self):
        return "Same as MassiveBlack-II"


class Snapshot(models.Model):
    simulation = models.ForeignKey(Simulation, on_delete=models.PROTECT)
    name = models.CharField(max_length=64, default="")
    age = models.FloatField(default=0)
    lookback = models.FloatField(default=0)
    redshift = models.FloatField(default=0)
    dark_matter_in_group = models.IntegerField(default=0)
    gas_in_group = models.IntegerField(default=0)
    stars = models.IntegerField(default=0)
    black_holes = models.IntegerField(default=0)
    fof_groups = models.IntegerField(default=0)
    folder_size = models.FloatField(default=0)


class Species(models.Model):
    name = models.CharField(max_length=64, default="")
    species_type = models.IntegerField(default=-1)
    folder_size = models.FloatField(default=0)
    snapshot = models.ForeignKey(Snapshot, on_delete=models.PROTECT, related_name="species_set")


class FofGroups(models.Model):
    name = models.CharField(max_length=64, default="")
    folder_size = models.FloatField(default=0)
    snapshot = models.ForeignKey(Snapshot, on_delete=models.PROTECT, related_name="fof_group_set")
