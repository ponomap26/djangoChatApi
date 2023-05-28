import React from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import ChatList from './components/ChatList';
import ChatDetail from './components/ChatDetail';
import UserList from './components/UserList';

function App() {
  return (
    <Router>
      <Route exact path="/root/" component={ChatList} />
      <Route exact path="/message/:id/" component={ChatDetail} />
      <Route exact path="/users/" component={UserList} />
    </Router>
  );
}

function RegistrationLinks() {
  return (
    <div>
      <a href="/accounts/login/">Войти</a>
      <a href="/accounts/logout/">Выход</a>
      <a href="/accounts/signup/">Зарегистрироваться</a>
    </div>
  );
}

export { App, RegistrationLinks };