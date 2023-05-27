import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import { App, RegistrationLink } from './App';
import reportWebVitals from './reportWebVitals';

ReactDOM.render(
  <React.StrictMode>
    <App />
    <RegistrationLink />
  </React.StrictMode>,
  document.getElementById('root')
);

reportWebVitals();