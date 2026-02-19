import React, { useState, useEffect } from 'react';

function Users() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchUsers = async () => {
      try {
        const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/users/`;
        console.log('Fetching users from:', apiUrl);
        
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log('Users data received:', data);
        
        // Handle both paginated (.results) and plain array responses
        const usersData = data.results || data;
        console.log('Processed users:', usersData);
        
        setUsers(usersData);
        setLoading(false);
      } catch (err) {
        console.error('Error fetching users:', err);
        setError(err.message);
        setLoading(false);
      }
    };

    fetchUsers();
  }, []);

  if (loading) return <div className="container mt-4"><div className="loading"><div className="spinner-border text-primary" role="status"><span className="visually-hidden">Loading...</span></div><p className="mt-3">Loading users...</p></div></div>;
  if (error) return <div className="container mt-4"><div className="alert alert-danger" role="alert"><strong>Error:</strong> {error}</div></div>;

  return (
    <div className="container mt-4">
      <h2 className="mb-4">👥 Users</h2>
      <div className="mb-3">
        <span className="badge bg-primary">Total Users: {users.length}</span>
      </div>
      <div className="table-responsive">
        <table className="table table-striped table-hover">
          <thead>
            <tr>
              <th>Avatar</th>
              <th>Name</th>
              <th>Superhero Name</th>
              <th>Email</th>
              <th>Team</th>
              <th>Total Points</th>
              <th>Date Joined</th>
            </tr>
          </thead>
          <tbody>
            {users.map((user) => (
              <tr key={user.id}>
                <td><span style={{fontSize: '1.5rem'}}>{user.avatar || '👤'}</span></td>
                <td><strong>{user.name || 'N/A'}</strong></td>
                <td><span className="text-primary fw-bold">{user.superhero_name || user.username || 'N/A'}</span></td>
                <td><small className="text-muted">{user.email}</small></td>
                <td>
                  {user.team_id ? (
                    <span className="badge bg-info">{user.team_id.replace('team_', '').toUpperCase()}</span>
                  ) : (
                    <span className="text-muted">No Team</span>
                  )}
                </td>
                <td>
                  <span className="badge bg-success">{user.total_points || 0} pts</span>
                </td>
                <td>{new Date(user.created_at).toLocaleDateString()}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Users;
