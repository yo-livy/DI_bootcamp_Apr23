import React, { Component } from 'react';
import data from '../data2.json'

class Example1 extends Component {
  constructor(props) {
    super(props);
    this.state = {
      dataArr : data['SocialMedias']

    };
  }


  render() {
    const data = this.state.dataArr;

    return (
      <div>
        <h1>Example 1</h1>
        {data.map((item,indx) => {
         return <h2 key={indx+1}>{item}</h2>
       })}
      </div>
    );
  }
}

export default Example1;
