// src/components/NotificationService.js

import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './ServiceStatus.css'; // Reuse the styling for consistency

const NotificationService = () => {
  const [status, setStatus] = useState('loading');
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchServiceStatus = async () => {
      try {
        // Replace with the actual endpoint for Notification Service health check
        const response = await axios.get(`${process.env.REACT_APP_NOTIFICATION_SERVICE_URL}/api/health`);
        setStatus(response.data.status === "running" ? "Success" : "Error");
      } catch (err) {
        setStatus("Error");
        setError(err);
      }
    };

    fetchServiceStatus();
  }, []);

  return (
    <div className="service-status">
      <h2>Notification Service Status</h2>
      {status === 'loading' ? (
        <div>Loading...</div>
      ) : status === 'Error' ? (
        <div className="error-message">Error: {error ? error.message : "Notification Service is down"}</div>
      ) : (
        <div className="success-message">Notification Service is up and running!</div>
      )}
    </div>
  );
};

export default NotificationService;
