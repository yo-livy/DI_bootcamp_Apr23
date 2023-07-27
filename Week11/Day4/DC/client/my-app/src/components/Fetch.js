import React, { Component } from 'react';

class Fetch extends Component {
  constructor(props) {
    super(props);
    this.state = {
        data: ''
    };
  }

  componentDidMount() {
    console.log('Mounted')
    const getData = async () => {
        const res = await fetch('http://localhost:3001/api/hello');
        this.setState({ data: await res.json()});
    }
    getData();
  }

  render() {

    return (
      <div>
        <h1>{this.state.data}</h1>
      </div>
    );
  }
}

export default Fetch;
