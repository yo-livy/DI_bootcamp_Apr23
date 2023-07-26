import React, { Component } from 'react';
import data from '../data2.json'
import { Link } from 'react-router-dom';

class Example3 extends Component {
  constructor(props) {
    super(props);
    this.state = {
      dataArr : data['Experiences']
    };
  }

  render() {
    const data = this.state.dataArr;

    return (
      <div>
        <h1>Example 3</h1>
        {data.map((item, indx) => {
         return (
            <div key={indx + 1}>
               <img src={item['logo']}/>
               <h2>{<Link to={item['url']}>{item['companyName']}</Link>}</h2>
               {item['roles'].map((role, indx) => {
                return (
                    <div key={indx+1}>
                      <p>{role['title']}</p>
                      <span>{role['startDate']}</span><span>{role['location']}</span>
                      <p>{role['description']}</p>
                    </div>   
                )
               })}
            </div>
         )
       })}
      </div>
    );
  }
}

export default Example3;