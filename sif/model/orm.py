from sif.model.model import Movie


def create_movie(title, year, rated, director, actors):
    movie = Movie(
        title=title,
        year=year,
        rated=rated,
        director=director,
        actors=actors
    )
    movie.save()


def get_movie(title):
    movie = Movie.objects(title=title)
    return movie


def get_all_movie():
    movie = Movie.objects
    return movie
