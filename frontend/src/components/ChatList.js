import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

function ChatList() {
  const [chats, setChats] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/room/')
      .then(response => {
        setChats(response.data);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);

  return (
    <div>
      <h1>Chats</h1>
      <ul>
        {chats.map(chat => (
          <li key={chat.id}>
            <Link to={`/chats/${chat.id}/`}>{chat.name}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ChatList;