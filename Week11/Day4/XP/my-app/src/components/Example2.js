import React, { Component } from 'react';
import data from '../data2.json'

class Example2 extends Component {
  constructor(props) {
    super(props);
    this.state = {
      dataArr : data['Skills']

    };
  }

  render() {
    const data = this.state.dataArr;

    return (
      <div>
        <h1>Example 2</h1>
        {data.map((item,indx) => {
         return (
            <div key={indx+1}>
               <h2>{item['Area']}</h2>
               {item['SkillSet'].map((skill,indx) => {
                return <li key={indx+1}>{skill['Name']}</li>
               })}
            </div>
         )
       })}
      </div>
    );
  }
}

export default Example2;