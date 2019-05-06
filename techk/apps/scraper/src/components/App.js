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
  filterCaseInsensitive = (filter, row) => {
    const id = filter.pivotId || filter.id;
    const content = row[id];
    console.log(row.subRows);
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

  alertMe(e) {
    e.preventDefault();
    axios.get('/scraper/ajax')
      .then(response => {
        this.setState({
          postContent: response.data
        })
    })
    alert("i have been clicked!");
  }

  render() {
    return (
      <div>
        <button id="init_scrapping" onClick={this.alertMe.bind(this)}>Scrapear</button>
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
              maxWidth: 200,
            },
            {
              Header: "Book",
              accessor: (d) => d.book,
              maxWidth: 100,
              Cell: (props) => <span>{console.log(props)}</span>,
            },
          ]}
          defaultPageSize={10}
          className="-striped -highlight"
          filterable
          defaultFilterMethod={this.filterCaseInsensitive}
          pivotBy={["id"]}
          SubComponent={row => {
            return (
              <div>
                subcomponent
              </div>
            )
          }}
        />
      </div>
    );
  }
}
ReactDOM.render(
  <App />,
  document.getElementById('categories')
);
