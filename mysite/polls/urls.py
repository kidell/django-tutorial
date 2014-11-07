from django.conf.urls import pattern, url

from polls import views

urlpatterns = patterns('',
		/polls/
	url(r'^$', views.index, name='index'),
		/polls/34/
	url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
		/polls/34/results/
	url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
		/polls/34/vote/
	url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)