import React, { Component } from 'react'
import Child from './Child';

export default class Color extends Component {
    constructor() {
      super();
    
      this.state = {
         favColor: 'red',
         show: true
      }
    }
    
    changeColor = () => {
        this.setState((prevState) => ({
            favColor: 'blue'
        }));
    };

    shouldComponentUpdate = () => {
        return true;
    }

    componentDidMount = () => {
        console.log("componentDidMount");
        this.timer = setTimeout(() => {
            this.setState ({
                favColor: 'yellow'
            })
        }, 3000);
      };

    componentDidUpdate(prevProps, prevState, snapshot) {
            // Access the snapshot value here if needed
            console.log('After update');
        }



    getSnapshotBeforeUpdate(prevProps, prevState) {
        // Return the previous state as the snapshot value
        console.log('in getSnapshotBeforeUpdate')
        return null;
      }


    handleHeader = () => {
        this.setState({show: false})
    }

    render() {
        return (
        <div>
            <header>
               {this.state.show ? <div>{<Child />}</div> : null}
               <button onClick={this.handleHeader}>Delete</button>
            </header>
            
            <h1>My favorite color is {this.state.favColor}</h1>
            <button onClick={this.changeColor}>Change color</button>
        </div>
        )
    }
}

