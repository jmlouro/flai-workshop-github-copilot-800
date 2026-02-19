import React, { useState, useEffect } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchWorkouts = async () => {
      try {
        const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;
        console.log('Fetching workouts from:', apiUrl);
        
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log('Workouts data received:', data);
        
        // Handle both paginated (.results) and plain array responses
        const workoutsData = data.results || data;
        console.log('Processed workouts:', workoutsData);
        
        setWorkouts(workoutsData);
        setLoading(false);
      } catch (err) {
        console.error('Error fetching workouts:', err);
        setError(err.message);
        setLoading(false);
      }
    };

    fetchWorkouts();
  }, []);

  if (loading) return <div className="container mt-4"><div className="loading"><div className="spinner-border text-primary" role="status"><span className="visually-hidden">Loading...</span></div><p className="mt-3">Loading workouts...</p></div></div>;
  if (error) return <div className="container mt-4"><div className="alert alert-danger" role="alert"><strong>Error:</strong> {error}</div></div>;

  const getDifficultyBadge = (difficulty) => {
    const badges = {
      'Easy': 'success',
      'Medium': 'warning',
      'Hard': 'danger'
    };
    return badges[difficulty] || 'secondary';
  };

  const getCategoryIcon = (category) => {
    const icons = {
      'Cardio': '❤️',
      'Strength': '💪',
      'Flexibility': '🤸',
      'Balance': '⚖️',
      'Endurance': '🏃'
    };
    return icons[category] || '🏋️';
  };

  return (
    <div className="container mt-4">
      <h2 className="mb-4">💪 Workouts</h2>
      <div className="mb-3">
        <span className="badge bg-primary">Total Workouts: {workouts.length}</span>
      </div>
      <div className="table-responsive">
        <table className="table table-striped table-hover">
          <thead>
            <tr>
              <th>#</th>
              <th>Workout Name</th>
              <th>Description</th>
              <th>Difficulty</th>
              <th>Duration (min)</th>
              <th>Category</th>
            </tr>
          </thead>
          <tbody>
            {workouts.map((workout) => (
              <tr key={workout.id}>
                <td><strong>{workout.id}</strong></td>
                <td><span className="text-primary fw-bold">{workout.name}</span></td>
                <td><small>{workout.description}</small></td>
                <td>
                  <span className={`badge bg-${getDifficultyBadge(workout.difficulty)}`}>
                    {workout.difficulty}
                  </span>
                </td>
                <td><span className="badge bg-info">{workout.duration} min</span></td>
                <td>{getCategoryIcon(workout.category)} {workout.category}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Workouts;
