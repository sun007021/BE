from django.urls import path
from competition.views import (
    CompetitionTaView,
    CompetitionUserView,
    CompetitionView,
    CompetitionDetailView,
)
from submission.views import (
    SubmissionCompetitionView,
    SubmissionCompetitionListView,
    SubmissionCompetitionCheckView,
    SubmissionCompetitionDownloadView,
)

app_name = "competition"
urlpatterns = [
    path('', CompetitionView.as_view(), name="competition"),
    path('<int:competition_id>/', CompetitionDetailView.as_view(), name="competition_detail"),
    path('<int:competition_id>/participation/', CompetitionUserView.as_view(), name='competition_user'),
    path('<int:competition_id>/participation/ta/', CompetitionTaView.as_view(), name='competition_ta'),
    path('<int:competition_id>/submission/', SubmissionCompetitionView.as_view(), name='competition_submission'),
    path('<int:competition_id>/submissions/', SubmissionCompetitionListView.as_view(),
         name='competition_submission_list'),
    path('<int:competition_id>/submissions/download/', SubmissionCompetitionDownloadView.as_view(),
         name='competition_submission_download'),
    path('<int:competition_id>/check/', SubmissionCompetitionCheckView.as_view(), name='competition_leaderboard_check'),
]
