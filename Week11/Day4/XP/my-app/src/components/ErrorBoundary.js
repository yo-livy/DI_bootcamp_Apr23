import React, { Component } from 'react';

class ErrorBoundary extends Component {
  constructor(props) {
    super(props);
    this.state = {
     hasError: false,
    };
  }

  componentDidCatch(error, info) {
    console.log('This is props', this.props);
    console.error('Error caught:', error);
    console.error('Error info:', info);
    this.setState({
      hasError: true,
    });
  }

  render() {

    return (
      <div>
       {this.state.hasError ? <h1>An error has accured.</h1> : this.props.children}
      </div>
    );
  }
}

export default ErrorBoundary;
