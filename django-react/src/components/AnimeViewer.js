import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

const AnimeViewer = () => {
    const { id } = useParams();
    const [viewer, setViewer] = useState(null);

    useEffect(() => {
        fetch(`http://127.0.0.1:8000/anime_viewer/${id}/`)
            .then(response => response.json())
            .then(data => setViewer(data))
            .catch(error => console.error("Ошибка:", error));
    }, [id]);

    if (!viewer) return <h2>Загрузка...</h2>;

    return (
        <div>
            <h1>{viewer.name}</h1>
            <p>Email: {viewer.email}</p>
            <h3>Просмотренные аниме:</h3>
            <ul>
                {viewer.watched_anime_list.map(anime => (
                    <li key={anime.id}>{anime.title}</li>
                ))}
            </ul>
        </div>
    );
};

export default AnimeViewer;
