from django.test import TestCase
from django.test.client import RequestFactory
from django.urls.base import reverse, reverse_lazy

from core.models import Movie
from core.views import MovieList

class MovieListPaginationTestCase(TestCase):
    ACTIVE_PAGINATION_HTML = """
    <li class='page-item active'>
    <a href='{}?page={}' class='page-link'>{}</a>
    </li>
    """
    def setUp(self):
        for n in range(50):
            Movie.objects.create(
                title=f"Film {n}",
                year=1990 + n,
                runtime=100,
            )
    def testFirstPage(self):
        movie_list_path = reverse_lazy('core:MovieList')
        request = RequestFactory().get(path=movie_list_path)
        response = MovieList.as_view()(request)
        self.assertEqual(200, response.status_code)
        self.assertTrue(response.context_data['is_paginated'])
        html = self.ACTIVE_PAGINATION_HTML.format(
        movie_list_path, 1, 1)
        self.assertInHTML(
            html,
            response.rendered_content)
