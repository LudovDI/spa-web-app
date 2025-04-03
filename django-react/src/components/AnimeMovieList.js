import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

const AnimeMovieList = () => {
    const [animeList, setAnimeList] = useState([]);

    useEffect(() => {
        fetch('http://127.0.0.1:8000/anime_movie/list/')
            .then((response) => response.json())
            .then((data) => {
                setAnimeList(data);
            })
            .catch((error) => console.error('Ошибка при загрузке списка аниме:', error));
    }, []);

    const addToWatched = (viewerId, animeId) => {
        fetch(`http://127.0.0.1:8000/anime_viewer/${viewerId}/add_anime/${animeId}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
        })
            .then((response) => response.json())
            .then((data) => {
                console.log('Аниме добавлено в просмотренные:', data);
            })
            .catch((error) => {
                console.error('Ошибка при добавлении аниме:', error);
            });
    };

    return (
        <div>
            <h1>Список аниме</h1>
            <ul>
                {animeList.map((anime) => (
                    <li key={anime.id}>
                        <h3>{anime.title}</h3>
                        <Link to={`/anime_movie/${anime.id}`}>Перейти к описанию</Link>
                        <button onClick={() => addToWatched(1, anime.id)}>Добавить в просмотренные</button>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default AnimeMovieList;