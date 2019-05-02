import React from "react";
import ReactDOM from "react-dom";
import axios from 'axios'

class App extends React.Component {
  constructor(props) {
    super(props);
    axios.get('/scraper/ajax')
      .then(function (response) {
        console.log(response);
    })
  }
  render() {
    return (
      <div>
      </div>
    );
  }
}
ReactDOM.render(
  <App />,
  document.getElementById('categories')
);
