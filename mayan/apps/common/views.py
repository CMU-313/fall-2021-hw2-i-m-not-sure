from django.contrib import messages
from django.templatetags.static import static
from django.utils.translation import ugettext_lazy as _
from django.views.generic import RedirectView
from django.db.models import Avg,F
from stronghold.views import StrongholdPublicMixin

from mayan.apps.views.generics import ConfirmView, SimpleView
from mayan.apps.views.mixins import (
    ExternalContentTypeObjectViewMixin, ObjectNameViewMixin
)

from .classes import ModelCopy
from .forms import LicenseForm
from .icons import icon_setup
from .menus import menu_tools, menu_setup
from .permissions import permission_object_copy
from .settings import setting_home_view
from mayan.apps.display.models import (
    Candidate, CandidateReview
)

class AboutView(SimpleView):
    extra_context = {'title': _('About')}
    template_name = 'appearance/about.html'

# View used for Statistics Page for HW2 Project
class StatisticsView(SimpleView):
    template_name = 'appearance/statistics.html'
    def get_extra_context(self):

        # Aggregates Candidates ranking from highest Exam/GPA score to lowest
        candidates = Candidate.objects.annotate(score = F('exam_score')/1600 + F('gpa_score')/4).order_by('-score')

        # Aggregates Reviews ranking from highest combined skills/experience score to lowest
        reviews = CandidateReview.objects.annotate(score = F('experience_score') + F('skills_score')).order_by('-score')

        # Computes average exam score across Candidates
        avg_exam = candidates.aggregate(Avg('exam_score'))

        # Computes average gpa score across Candidates
        avg_gpa = candidates.aggregate(Avg('gpa_score'))

        # Computes average experience score across Reviews
        avg_exp = reviews.aggregate(Avg('experience_score'))

        # Computes average skills score across Reviews        
        avg_skills = reviews.aggregate(Avg('skills_score'))
        return {
            'candidates': candidates,
            'reviews' : reviews,
            'avg_exam': avg_exam['exam_score__avg'],
            'avg_gpa': avg_gpa['gpa_score__avg'],
            'avg_exp': avg_exp['experience_score__avg'],
            'avg_skills': avg_skills['skills_score__avg'],
            'title': _('Statistics')
        }

# View used for Students Page for HW2 Project        
class StudentsView(SimpleView):
    template_name = 'appearance/students.html'
    def get_extra_context(self):

        # Aggregates Candidates ranking from highest Exam/GPA score to lowest
        candidates = Candidate.objects.annotate(score = F('exam_score')/1600 + F('gpa_score')/4).order_by('-score')
        
        # Aggregates Reviews ranking from highest combined skills/experience score to lowest
        reviews = CandidateReview.objects.annotate(score = F('experience_score') + F('skills_score')).order_by('-score')

        # Computes average exam score across Candidates
        student = Candidate.objects.get(id=self.kwargs['student_id'])

        # Computes average exam score across Candidates
        avg_exam = candidates.aggregate(Avg('exam_score'))

        # Computes average gpa score across Candidates
        avg_gpa = candidates.aggregate(Avg('gpa_score'))
        
        # Computes average experience score across Reviews
        avg_exp = reviews.aggregate(Avg('experience_score'))

        # Computes average skills score across Reviews 
        avg_skills = reviews.aggregate(Avg('skills_score'))

        # Aggregates reviews relating to particular candidate
        student_reviews = CandidateReview.objects.filter(candidate_name = student.candidate_name)

        # Computes average experience score across Reviews related to candidate
        student_avg_exp = student_reviews.aggregate(Avg('experience_score'))

        # Computes average skills score across Reviews related to candidate
        student_avg_skills = student_reviews.aggregate(Avg('skills_score'))

        return {
            'candidates': candidates,
            'reviews' : reviews,
            'student': student,
            'avg_exam': avg_exam['exam_score__avg'],
            'avg_gpa': avg_gpa['gpa_score__avg'],
            'avg_exp': avg_exp['experience_score__avg'],
            'avg_skills': avg_skills['skills_score__avg'],
            'student_reviews' : student_reviews,
            'student_avg_exp': student_avg_exp['experience_score__avg'],
            'student_avg_skills': student_avg_skills['skills_score__avg'],            
            'title': _('Students')
        }

class FaviconRedirectView(RedirectView):
    permanent = True

    def get_redirect_url(self, *args, **kwargs):
        """
        Hide the static tag import to avoid errors with static file
        processors
        """
        return static(path='appearance/images/favicon.ico')


class HomeView(SimpleView):
    extra_context = {
        'title': _('Dashboard'),
    }
    template_name = 'appearance/home.html'


class LicenseView(SimpleView):
    extra_context = {
        'form': LicenseForm(),
        'read_only': True,
        'title': _('License'),
    }
    template_name = 'appearance/generic_form.html'


class ObjectCopyView(
    ExternalContentTypeObjectViewMixin, ObjectNameViewMixin, ConfirmView
):
    external_object_permission = permission_object_copy

    def get_extra_context(self):
        model_copy = ModelCopy.get(model=self.external_object._meta.model)
        context = {
            'object': self.external_object,
            'subtitle': _('Fields to be copied: %s') % ', '.join(
                sorted(
                    map(
                        str, model_copy.get_fields_verbose_names()
                    )
                )
            )
        }

        context['title'] = _(
            'Make a copy of %(object_name)s "%(object)s"?'
        ) % {
            'object_name': self.get_object_name(context=context),
            'object': self.external_object
        }

        return context

    def view_action(self):
        self.external_object.copy_instance()
        messages.success(
            message=_('Object copied successfully.'),
            request=self.request
        )


class RootView(StrongholdPublicMixin, SimpleView):
    extra_context = {'home_view': setting_home_view.value}
    template_name = 'appearance/root.html'


class SetupListView(SimpleView):
    template_name = 'appearance/generic_list_horizontal.html'

    def get_extra_context(self, **kwargs):
        return {
            'no_results_icon': icon_setup,
            'no_results_text': _(
                'No results here means that don\'t have the required '
                'permissions to perform administrative task.'
            ),
            'no_results_title': _('No setup options available.'),
            'resolved_links': menu_setup.resolve(
                request=self.request, sort_results=True
            ),
            'title': _('Setup items'),
            'subtitle': _(
                'Here you can configure all aspects of the system.'
            )
        }


class ToolsListView(SimpleView):
    template_name = 'appearance/generic_list_horizontal.html'

    def get_extra_context(self):
        return {
            'resolved_links': menu_tools.resolve(
                request=self.request, sort_results=True
            ),
            'title': _('Tools'),
            'subtitle': _(
                'These modules are used to do system maintenance.'
            )
        }
