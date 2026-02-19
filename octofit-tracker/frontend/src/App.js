import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import './App.css';
import Users from './components/Users';
import Activities from './components/Activities';
import Teams from './components/Teams';
import Leaderboard from './components/Leaderboard';
import Workouts from './components/Workouts';
import logo from './logo.png';

function App() {
  return (
    <div className="App">
      <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
        <div className="container-fluid">
          <Link className="navbar-brand" to="/">
            <img src={logo} alt="OctoFit Logo" className="navbar-logo" />
            OctoFit Tracker
          </Link>
          <button
            className="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarNav"
            aria-controls="navbarNav"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav">
              <li className="nav-item">
                <Link className="nav-link" to="/users">
                  Users
                </Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/activities">
                  Activities
                </Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/teams">
                  Teams
                </Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/leaderboard">
                  Leaderboard
                </Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/workouts">
                  Workouts
                </Link>
              </li>
            </ul>
          </div>
        </div>
      </nav>

      <Routes>
        <Route path="/" element={
          <div className="container mt-4">
            <div className="home-hero">
              <h1>Welcome to OctoFit Tracker</h1>
              <p className="lead">Track your fitness activities, compete with teams, and achieve your fitness goals!</p>
            </div>
            
            <div className="row mt-5">
              <div className="col-md-4 mb-4">
                <div className="card">
                  <div className="card-header">
                    <h5 className="mb-0">👥 Users</h5>
                  </div>
                  <div className="card-body">
                    <p className="card-text">Manage user profiles and track member fitness levels</p>
                    <a href="/users" className="btn btn-primary">View Users</a>
                  </div>
                </div>
              </div>
              
              <div className="col-md-4 mb-4">
                <div className="card">
                  <div className="card-header">
                    <h5 className="mb-0">🏃 Activities</h5>
                  </div>
                  <div className="card-body">
                    <p className="card-text">Log and track fitness activities and calories burned</p>
                    <a href="/activities" className="btn btn-primary">View Activities</a>
                  </div>
                </div>
              </div>
              
              <div className="col-md-4 mb-4">
                <div className="card">
                  <div className="card-header">
                    <h5 className="mb-0">🤝 Teams</h5>
                  </div>
                  <div className="card-body">
                    <p className="card-text">Join teams and compete together for fitness goals</p>
                    <a href="/teams" className="btn btn-primary">View Teams</a>
                  </div>
                </div>
              </div>
            </div>
            
            <div className="row">
              <div className="col-md-6 mb-4">
                <div className="card">
                  <div className="card-header">
                    <h5 className="mb-0">🏆 Leaderboard</h5>
                  </div>
                  <div className="card-body">
                    <p className="card-text">Check rankings and compete with other users</p>
                    <a href="/leaderboard" className="btn btn-primary">View Leaderboard</a>
                  </div>
                </div>
              </div>
              
              <div className="col-md-6 mb-4">
                <div className="card">
                  <div className="card-header">
                    <h5 className="mb-0">💪 Workouts</h5>
                  </div>
                  <div className="card-body">
                    <p className="card-text">Discover personalized workout suggestions</p>
                    <a href="/workouts" className="btn btn-primary">View Workouts</a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        } />
        <Route path="/users" element={<Users />} />
        <Route path="/activities" element={<Activities />} />
        <Route path="/teams" element={<Teams />} />
        <Route path="/leaderboard" element={<Leaderboard />} />
        <Route path="/workouts" element={<Workouts />} />
      </Routes>
    </div>
  );
}

export default App;
