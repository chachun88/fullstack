import React from "react";
import ReactDOM from "react-dom";
import axios from 'axios'
import ReactTable from "react-table";
import "react-table/react-table.css";

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      postContent: []
    };
  }
  componentDidMount() {
    axios.get('/scraper/ajax')
      .then(response => {
        this.setState({
          postContent: response.data
        })
    })
  }
  render() {
    return (
      <div>
        <ReactTable
          data={this.state.postContent}
          columns={[
            {
              Header: "ID",
              accessor: "id",
              maxWidth: 100,
            },
            {
              Header: "Name",
              accessor: "name",
              maxWidth: 200
            }
          ]}
          defaultPageSize={10}
          className="-striped -highlight"
          filterable
        />
      </div>
    );
  }
}
ReactDOM.render(
  <App />,
  document.getElementById('categories')
);
