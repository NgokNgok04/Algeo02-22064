import React, { Component } from "react";
import axios from "axios";

export default class Images extends Component {
    constructor(props) {
        super(props);

        this.state = {
            title: [],
        };
       }

        componentDidMount() {
            this.getImages();
        }

        getImages = () => {
            axios
                .get("http://127.0.0.1:5000/images")
                .then((response) => {
                    if (response.status === 200) {
                        this.setState ({
                            title: response.data,
                        });
                        console.log(response.data);
                    }
                })
                .catch((error) => {
                    console.error(error);
                });
        };
    
    render() {
        return (
            <div className="container pt-4">
                <div className="row">
                    <div className="col-lg-12">
                        <div className="card shadow">
                            <div className="card-header">
                                <h4 className="card-title fw-bold"> Images List </h4>
                            </div>
                            <div className="card-body">
                                <div className="row">
                                    
                                    {
                                        this.state.title.length > 0 ? (
                                            this.state.title.map((image) => (
                                                <div className="col-lg-3" key={image.id}>
                                                    <img src={ "http://127.0.0.1:5000/static/uploads/" + image.title } className="img-fluid img-bordered" width="200px"
                                                    />
                                                </div>
                                            ))
                                        ) : (
                                            <h6 className="text-danger text-center"> No Image Found </h6>
                                        )
                                    }

                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}