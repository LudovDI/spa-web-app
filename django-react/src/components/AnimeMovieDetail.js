import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

const AnimeMovieDetail = () => {
    const { id } = useParams();
    const [anime, setAnime] = useState(null);

    useEffect(() => {
        fetch(`http://127.0.0.1:8000/anime_movie/${id}/`)
            .then((response) => response.json())
            .then((data) => setAnime(data))
            .catch((error) => console.error('Ошибка при получении данных:', error));
    }, [id]);

    if (!anime) return <div>Загрузка...</div>;

    return (
        <div>
            <h1>{anime.title}</h1>
            <p>{anime.description}</p>
            <img src={anime.image_url} alt={anime.title} />
        </div>
    );
};

export default AnimeMovieDetail;