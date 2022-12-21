from django.contrib import admin
from .models import Job, JobSkill, Candidate, CandidateSkill

# Register your models here.
admin.site.register(Job)
admin.site.register(JobSkill)
admin.site.register(Candidate)
admin.site.register(CandidateSkill)

