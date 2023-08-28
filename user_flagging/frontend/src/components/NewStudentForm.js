import React from "react";
import { Button, Form, FormGroup, Input, Label } from "reactstrap";

import axios from "axios";

import { API_URL } from "../constants"

class NewCustomerForm extends React.Component
{
    state = 
        {
            id: 0. 
            first_name: "", 
            last_name: "" ,
            email: "", 
            phone: "",
            flags: [],  
        };

    componentDidMount()
    {
        if (this.props.customer)
        {
            const {id, first_name, last_name, email, phone, flags} = this,props.customer;
            this.setState({id, first_name, last_name, email, phone, flags});
        }
    }

    onChange = e =>
    {
        this.setState({ [e.target.name]: e.target.value })
    };

    createStudent = e =>
    {
        e.preventDefault();
        axios.post(API_URL, this.state).then(() =>
            {
                this.props.resetState();
                this.props.toggle();
            });
    };
}
