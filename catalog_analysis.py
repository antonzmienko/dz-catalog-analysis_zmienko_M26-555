import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155,
     "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

def average_rating(movies):
    i = 0
    ratingSum = 0
    
    for movie in movies:
        ratingSum += movie['rating']
        i += 1

    result = round(ratingSum / i, 1)
    
    return result

def catalog_age_stats(movies, current_year=2026):
    newest_movie_original_year = None
    oldest_movie_original_year = None
    all_years = 0
    
    for movie in movies:
        if 'year' not in movie:
            continue
        if oldest_movie_original_year is None:
            oldest_movie_original_year = movie['year']
        if newest_movie_original_year is None:
            newest_movie_original_year = movie['year']

        if movie['year'] < oldest_movie_original_year:
            oldest_movie_original_year = movie['year']
        if movie['year'] > newest_movie_original_year:
            newest_movie_original_year = movie['year']
        all_years += current_year - movie['year']

    new_current_years_diff = current_year - newest_movie_original_year
    old_current_years_diff = current_year - oldest_movie_original_year

    average_year = math.ceil(all_years / len(movies))

    return (old_current_years_diff, new_current_years_diff, average_year)

def duration_in_hours(minutes):
    hours = minutes // 60
    minutes = minutes % 60

    return f'{hours}ч {minutes}м'

def rating_tier(rating):
    if rating >= 9:
        return 'шедевр'
    elif 9 > rating >= 7:
        return 'хорошо'

    return 'средне' if 7 > rating >= 5 else 'слабо'

def decade_label(year):
    match year:
        case _ if year > 2020:
            return 'новые'
        case _ if 2020 >= year >= 2015:
            return 'недавние'
        case _ if 2015 > year:
            return 'старые'

def show_not_comedy_movies(movies):
    for movie in movies:
        if 'comedy' in movie['genres']:
            continue
        
        print(movie['title'])

def show_first_masterpiece(movies):
    masterpiece = None
    i = 0

    while masterpiece is None and i <= len(movies) - 1:
        if movies[i]['rating'] > 9:
            masterpiece = movies[i]
            print(movies[i]['title'])
            break
        i += 1
    else:
        print("Шедевров не найдено")

    return masterpiece

def count_long_movies(movies, threshold=120):
    count = 0
    for movie in movies:
        if movie['duration_min'] > threshold:
            count += 1
    
    return count

def normalize_title(title):
    result_string = ''
    separated_title_list = title.split()
    for word in separated_title_list:
        capitalized_word = word[0].upper() + word[1:]
        result_string += capitalized_word + ' '
    return result_string.strip()

def make_slug(title):
    slug = title.lower().replace(' ', '-')
    return slug

def format_report_line(movie):
    genres = ', '.join(sorted(movie['genres']))
    title = normalize_title(movie['title'])
    duration = duration_in_hours(movie['duration_min'])
    return (
        f'"{title}" ({movie["year"]}) — {movie["rating"]}/10, '
        f'{duration}, жанры: {genres}'
    )

def titles_sorted_by_rating(movies):
    sortedList = sorted(movies, key=lambda x: x['rating'], reverse=True)
    return [movie['title'] for movie in sortedList]

def top_n_by_rating(movies, n=3):
    sortedList = sorted(movies, key=lambda x: x['rating'], reverse=True)
    return [(movie['title'], movie['rating']) for movie in sortedList[:n]]

def count_by_genre(movies):
    genre_count_dict = {}
    for movie in movies:
        for genre in movie["genres"]:
            genre_count_dict[genre] = genre_count_dict.get(genre, 0) + 1
    return genre_count_dict

def actor_filmography(movies):
    actor_filmography_dict = {}
    for movie in movies:
        for actor in movie.get('actors'):
            if actor in actor_filmography_dict:
                actor_filmography_dict[actor] += [movie['title']]
            else:
                actor_filmography_dict[actor] = [movie['title']]
    return actor_filmography_dict

def dict_title_rating_grande_average(movies):
    average_rating_float = average_rating(movies)
    return {
        key['title']: key['rating']
        for key in movies
        if key['rating'] > average_rating_float
    }
    
def all_genres(movies):
    genres_list = set()
    for movie in movies:
        genres_list.update(movie.get('genres'))
            
    return genres_list

def common_actors(movie1, movie2):
    actors = set(movie1.get('actors')) & set(movie2.get('actors'))
    return actors

def genres_only_in_one(movies_a, movies_b):
    return all_genres(movies_a) - all_genres(movies_b)

def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie.get('rating', 0) >= min_rating:
            yield movie

def generator_report(movies, min_rating=8.0):
    for movie in iter_high_rated(movies, min_rating):
        print(format_report_line(movie))

duration_sum = sum(m["duration_min"] for m in movies if m["rating"] > 7)

def build_report(movies):
    *_, average_age = catalog_age_stats(movies)
    movies_by_title = {movie["title"]: movie for movie in movies}

    print("ОТЧЁТ ПО КАТАЛОГУ")
    print(f"Средний рейтинг: {average_rating(movies)}")
    print(f"Средний возраст фильмов: {average_age} лет")
    print()
    print("Топ-3 фильма:")
    for title, _rating in top_n_by_rating(movies):
        movie = dict(movies_by_title[title])
        movie["genres"] = sorted(movie["genres"])
        print(f"  {format_report_line(movie)}")
    print()
    print("Фильмов по жанрам:")
    for genre, count in sorted(
        count_by_genre(movies).items(),
        key=lambda item: (-item[1], item[0]),
    ):
        print(f"  {genre} — {count}")
    print()
    print(f"Все жанры каталога: {', '.join(sorted(all_genres(movies)))}")


build_report(movies)

