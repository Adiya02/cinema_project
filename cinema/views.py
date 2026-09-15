from django.shortcuts import render, redirect
from .data import GENRES, MOVIES


def index(request):
    """Главная страница: показывает форму настроек и подборку фильмов."""
    current_genre = request.COOKIES.get("genre", "")
    theme = request.COOKIES.get("theme", "light")
    language = request.COOKIES.get("language", "ru")

    # Последние посещённые жанры (хранятся строкой через запятую)
    recent_raw = request.COOKIES.get("recent_genres", "")
    recent_genres = [g for g in recent_raw.split(",") if g][:5]

    selected_genre_data = GENRES.get(current_genre)
    movies = MOVIES.get(current_genre, [])

    context = {
        "genres": GENRES,
        "current_genre": current_genre,
        "selected_genre_data": selected_genre_data,
        "movies": movies,
        "theme": theme,
        "language": language,
        "recent_genres": recent_genres,
    }
    return render(request, "cinema/index.html", context)


def set_preferences(request):
    """Сохраняет настройки пользователя в cookies."""
    if request.method == "POST":
        genre = request.POST.get("genre", "")
        theme = request.POST.get("theme", "light")
        language = request.POST.get("language", "ru")

        # Обновляем список последних жанров
        recent_raw = request.COOKIES.get("recent_genres", "")
        recent = [g for g in recent_raw.split(",") if g]
        if genre and genre in recent:
            recent.remove(genre)
        if genre:
            recent.insert(0, genre)
        recent = recent[:5]

        response = redirect("cinema:index")
        response.set_cookie("genre", genre, max_age=60 * 60 * 24 * 30)
        response.set_cookie("theme", theme, max_age=60 * 60 * 24 * 30)
        response.set_cookie("language", language, max_age=60 * 60 * 24 * 30)
        response.set_cookie("recent_genres", ",".join(recent), max_age=60 * 60 * 24 * 30)
        return response

    return redirect("cinema:index")


def clear_preferences(request):
    """Сбрасывает cookies пользователя."""
    response = redirect("cinema:index")
    for key in ("genre", "theme", "language", "recent_genres"):
        response.delete_cookie(key)
    return response