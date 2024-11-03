// src/components/Dashboard.js

import React from 'react';
import ServiceStatus from './ServiceStatus';

const Dashboard = () => {
    return (
        <div>
            <h1>Dashboard</h1>
            <ServiceStatus />
            {/* You can add other dashboard-related components or information here */}
        </div>
    );
};

export default Dashboard;
