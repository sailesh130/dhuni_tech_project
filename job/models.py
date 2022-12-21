from django.db import models

# Create your models here.
class Job(models.Model):
    job_title = models.CharField(max_length=120, null=False)

    def __str__(self):
        return self.job_title

class JobSkill(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="job_skills")
    skill_name = models.CharField(max_length=120, null=False)

    def __str__(self):
        return self.skill_name

class Candidate(models.Model):
    first_name = models.CharField(max_length=80, null=False)
    last_name = models.CharField(max_length=80, null=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class CandidateSkill(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name="candidate_skills")
    skill_name = models.CharField(max_length=120, null=False)

    def __str__(self):
        return self.skill_name
