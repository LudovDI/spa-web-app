import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import AnimeMovieList from './components/AnimeMovieList';
import AnimeMovieDetail from './components/AnimeMovieDetail';

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/anime_movie/list" element={<AnimeMovieList />} />
          <Route path="/anime_movie/:id" element={<AnimeMovieDetail />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;