import React, { Component } from 'react'

export default class Child extends Component {

    componentWillUnmount = () => {
        alert('The component in Header is to be unmounted')
    }

    render() {
        return (
        <div>
            <h1>Hello world!</h1>
        </div>
        )
    }
}
