import React, { useState, useEffect } from 'react';

function Activities() {
  const [activities, setActivities] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchActivities = async () => {
      try {
        const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/`;
        console.log('Fetching activities from:', apiUrl);
        
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log('Activities data received:', data);
        
        // Handle both paginated (.results) and plain array responses
        const activitiesData = data.results || data;
        console.log('Processed activities:', activitiesData);
        
        setActivities(activitiesData);
        setLoading(false);
      } catch (err) {
        console.error('Error fetching activities:', err);
        setError(err.message);
        setLoading(false);
      }
    };

    fetchActivities();
  }, []);

  if (loading) return <div className="container mt-4"><div className="loading"><div className="spinner-border text-primary" role="status"><span className="visually-hidden">Loading...</span></div><p className="mt-3">Loading activities...</p></div></div>;
  if (error) return <div className="container mt-4"><div className="alert alert-danger" role="alert"><strong>Error:</strong> {error}</div></div>;

  const getActivityIcon = (type) => {
    const icons = {
      'run': '🏃',
      'Running': '🏃',
      'cycle': '🚴',
      'Cycling': '🚴',
      'swim': '🏊',
      'Swimming': '🏊',
      'weights': '🏋️',
      'Weightlifting': '🏋️',
      'yoga': '🧘',
      'Yoga': '🧘',
      'walk': '🚶',
      'Walking': '🚶',
      'hiit': '💥',
      'HIIT': '💥'
    };
    return icons[type] || '💪';
  };

  const totalCalories = activities.reduce((sum, activity) => sum + (activity.calories_burned || 0), 0);

  return (
    <div className="container mt-4">
      <h2 className="mb-4">🏃 Activities</h2>
      <div className="mb-3">
        <span className="badge bg-primary me-2">Total Activities: {activities.length}</span>
        <span className="badge bg-success">Total Calories: {totalCalories.toLocaleString()}</span>
      </div>
      <div className="table-responsive">
        <table className="table table-striped table-hover">
          <thead>
            <tr>
              <th>User</th>
              <th>Activity Type</th>
              <th>Duration (min)</th>
              <th>Calories Burned</th>
              <th>Points Earned</th>
              <th>Date</th>
              <th>Notes</th>
            </tr>
          </thead>
          <tbody>
            {activities.map((activity) => (
              <tr key={activity.id}>
                <td><span className="text-primary fw-bold">{activity.user_name || 'Unknown'}</span></td>
                <td>
                  {getActivityIcon(activity.activity_type)} <strong>{activity.activity_type.charAt(0).toUpperCase() + activity.activity_type.slice(1)}</strong>
                </td>
                <td><span className="badge bg-info">{activity.duration_minutes || 0} min</span></td>
                <td><span className="badge bg-success">{activity.calories_burned || 0} cal</span></td>
                <td><span className="badge bg-warning text-dark">{activity.points_earned || 0} pts</span></td>
                <td>{activity.date ? new Date(activity.date).toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' }) : 'N/A'}</td>
                <td><small className="text-muted">{activity.notes || '-'}</small></td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Activities;
