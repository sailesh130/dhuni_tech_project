from rest_framework import serializers
from .models import Candidate, CandidateSkill

class CandidateSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    skills = serializers.SerializerMethodField()

    def get_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    def get_skills(self, obj):
        return obj.candidate_skills.all().values_list("skill_name", flat=True)
    
    class Meta:
        model = Candidate
        fields = ["id", "name", "skills"]
