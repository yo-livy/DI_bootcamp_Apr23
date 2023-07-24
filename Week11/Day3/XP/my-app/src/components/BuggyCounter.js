import React, { Component } from 'react'

export default class BuggyCounter extends Component {
    constructor() {
        super();
        this.state = {
            counter: 0,
          };
    }

    handleClick = () => {
        const { counter } = this.state;
        if (counter === 5) {
            throw new Error("Counter cannot exceed 5.");
        }
        this.setState((prevState) => ({
          counter: prevState.counter + 1,
        }));
      };  //Always create a new referance by creating a new object
    

    render() {
        return (
        <div>
            <h1>{this.state.counter}</h1>
            <button onClick={this.handleClick}>Increase</button>
        </div>
        )
    }
}
