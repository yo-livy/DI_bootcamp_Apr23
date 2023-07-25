import React, { Component } from 'react';

export default class ErrorBoundary extends Component {
    constructor() {
        super();
        this.state = {
            hasError: false
        };
    }

    componentDidCatch(error, errorInfo) {
      console.log("in component did");
        this.setState({
          hasError: true,
          error: error,
          errorInfo: errorInfo

        });
    }

    render() {
        if (this.state.error) {
            return (
            <details style={{ whiteSpace: 'pre-wrap' }}>
              {this.state.error && this.state.error.toString()}
              <br />
              {this.state.errorInfo.componentStack}
            </details>
        );
        }
        return (
          <div>
            <h1>Error boundary wrap</h1>
            <h2>{this.props.children}</h2>
          </div>
        
        );
    }
}
