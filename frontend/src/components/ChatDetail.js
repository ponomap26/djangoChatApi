import React, { useState, useEffect } from 'react';
import axios from 'axios';
import io from 'socket.io-client';

function ChatDetail(props) {
  const [chat, setChat] = useState(null);
  const [messages, setMessages] = useState([]);
  const [text, setText] = useState('');
  const [socket, setSocket] = useState(null);

  useEffect(() => {
    axios.get(`http://localhost:8000/chats/${props.match.params.id}/`)
      .then(response => {
        setChat(response.data);
      })
      .catch(error => {
        console.log(error);
      });

    axios.get(`http://localhost:8000/messages/?chat=${props.match.params.id}`)
      .then(response => {
        setMessages(response.data);
      })
      .catch(error => {
        console.log(error);
      });

    const newSocket = io('http://localhost:8000');
    newSocket.on('connect', () => {
      console.log('Connected to WebSocket');
      setSocket(newSocket);
    });
    newSocket.on('disconnect', () => {
      console.log('Disconnected from WebSocket');
      setSocket(null);
    });
    newSocket.on('message', message => {
      setMessages([...messages, message]);
    });

    return () => {
      if (socket) {
        socket.disconnect();
      }
    };
  }, [props.match.params.id, messages, socket]);

  const handleSubmit = event => {
    event.preventDefault();
    axios.post('http://localhost:8000/message/', {
      text: text,
      sender: 1, // TODO: Replace with actual user ID
      receiver: chat.members[0].id, // TODO: Replace with actual receiver ID
      chat: chat.id,
    })
      .then(response => {
        setText('');
        if (socket) {
          socket.emit('message', response.data);
        }
      })
      .catch(error => {
        console.log(error);
      });
  };

  return (
    <div>
      {chat && (
        <div>
          <h1>{chat.name}</h1>
          <ul>
            {messages.map(message => (
              <li key={message.id}>
                {message.sender.username}: {message.text}
              </li>
            ))}
          </ul>
          <form onSubmit={handleSubmit}>
            <input type="text" value={text} onChange={event => setText(event.target.value)} />
            <button type="submit">Send</button>
          </form>
        </div>
      )}
    </div>
  );
}

export default ChatDetail;