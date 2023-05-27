import './App.css';
import axios from 'axios';
import React from 'react';

class App extends React.Component {
  state = { details: [] };

  componentDidMount() {
    let data;
    axios
      .get('http://localhost:8080/api')
      .then((response) => {
        data = response.data;
        this.setState({ details: data });
      })
      .catch((err) => {
        console.log(err);
      });
  }

  render() {
    return (
      <div className="App">
        <h1>ChatAPI</h1>

        {this.state.details.map((details, index) => {
          return (
            <div key={index}>
              <h2>{details.name}</h2>
              <p>{details.message}</p>
            </div>
          );
        })}
      </div>
    );
  }
}

export default App;