import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Transactions = () => {
  const [transactions, setTransactions] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8002/api/transactions')
      .then(response => setTransactions(response.data))
      .catch(error => console.error(error));
  }, []);

  return (
    <div>
      <h1>Transactions</h1>
      <ul>
        {transactions.map((txn) => (
          <li key={txn.id}>
            {txn.type} - ${txn.amount}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Transactions;
