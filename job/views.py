from django.shortcuts import render
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from .models import Job, JobSkill, Candidate, CandidateSkill
from rest_framework import status
from django.db.models import Count, Q
from .serializers import CandidateSerializer
from functools import reduce
from operator import or_


class DeserveCandidate(APIView):
    
    def get(self, request):
        if job_name := request.query_params.get("job_name", None):
            if job := Job.objects.filter(job_title__icontains=job_name).first():
                return self._find_suitable_candidate(job)
            else:
                return Response({"message":f"No job with the name {job_name} found in database"}, status.HTTP_404_NOT_FOUND)

        return Response({"message":"Job name must be provided"}, status.HTTP_404_NOT_FOUND)

    def _find_suitable_candidate(self, job):
        job_skills = job.job_skills.all().values_list("skill_name", flat=True)
        q_object = reduce(or_, (Q(candidate_skills__skill_name__icontains=skill) for skill in job_skills))
        best_candidate = Candidate.objects.filter(q_object).annotate(count =Count("id")).order_by("-count").first()
        serializer = CandidateSerializer(best_candidate)
        return Response({"best_candidate_details":serializer.data})
                
                