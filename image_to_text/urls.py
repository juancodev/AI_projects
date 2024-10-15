from django.urls import path
from .views import hello, about, user, projects, tasks, project_with_id


urlpatterns = [
    path("", hello),
    path("about/", about),
    path("user/<str:username>", user),
    path("projects/", projects),
    path("projects/<int:id>", project_with_id),
    path("tasks/", tasks)
]
