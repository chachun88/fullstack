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
  filterCaseInsensitive = (filter, row) => {
    const id = filter.pivotId || filter.id;
    const content = row[id];
    if (typeof content !== 'undefined') {
        // filter by text in the table or if it's a object, filter by key
        if (typeof content === 'object' && content !== null && content.key) {
            return String(content.key).toLowerCase().includes(filter.value.toLowerCase());
        } else {
            return String(content).toLowerCase().includes(filter.value.toLowerCase());
        }
    }

    return true;
  };

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
          defaultFilterMethod={this.filterCaseInsensitive}
        />
      </div>
    );
  }
}
ReactDOM.render(
  <App />,
  document.getElementById('categories')
);
