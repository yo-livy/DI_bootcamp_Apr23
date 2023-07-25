import React, { Component } from 'react'

export default class BuggyCounter extends Component {
    constructor() {
        super();
        this.state = {
            counter: 0,
          };
    }

    handleClick = () => {
        
        this.setState((prevstate) => ({
          counter: prevstate.counter + 1,
        }));
      };  //Always create a new referance by creating a new object
    

    render() {
        if (this.state.counter === 5) {
            throw new Error("Counter cannot exceed 5");
        } else {
            return (
                <div>
                    <h1>Counter: {this.state.counter}</h1>
                    <button onClick={this.handleClick}>Increase</button>
                </div>
                )
        }
        
    }
}
