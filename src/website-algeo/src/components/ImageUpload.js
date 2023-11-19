import React, { Component } from "react";
import axios from "axios";
import Images from "./Image";
import DragAndDrop from "./DragAndDrop";
import Search from "./Search";
export default class ImageUpload extends Component {
  constructor(props) {
      super(props);
    
      this.state = {
          image: "",
          responseMsg: {
              status: "",
              message: "",
              error: "",
          },
      };
  }

  //  image onchange handler
  handleChange = (e) => {
      const imagesArray = [];
      
      for (let i = 0; i < e.target.files.length; i++) {
      this.fileValidate(e.target.files[i]);
      imagesArray.push(e.target.files[i]);
      }
      this.setState({
      image: imagesArray,
      });
  };

  // submit handler
  submitHandler = (e) => {
      e.preventDefault();
      const data = new FormData();
      for (let i = 0; i < this.state.image.length; i++) {
          data.append("files[]",this.state.image[i]);
      }

      axios.post("http://127.0.0.1:5000/upload", data)
      .then((response) => {
          console.log(response);
        if (response.status === 201){
          this.setState ({
              responseMsg: {
              status: response.data.status,
              message: response.data.essage,
              },
          });
          setTimeout(() => {
              this.setState({
                  image: "",
                  responseMsg: "",
              });
          }, 100000);

          document.querySelector("#imageForm").reset();
          // getting uploaded images
          this.refs.child.getImages();
        }
          alert("Successfully Uploaded");
      })
      .catch((error) => {
          console.error(error);
          if (error.response) {
              console.log(error.response)
              if (error.response.status === 401) {
                  alert("Invalid credentials");
              }
          }
      });
  };

  // file validation
  fileValidate = (file) => {
      if (
      file.type === "image/png" ||
      file.type === "image/jpg" ||
      file.type === "image/jpeg"
      ) {
        this.setState({
            responseMsg: {
            error: "",
            },
        });
        return true;
      } else {
          this.setState({
            responseMsg: {
              error: "File type allowed only jpg, png, jpeg",
            },
          });
          return false;
      }
  };

  render() {
      return (
        <div className="container py-5">
          <div className="row">
            <div className="col-lg-12">
              <form onSubmit={this.submitHandler} encType="multipart/form-data" id="imageForm">
                <div className="card shadow">
    
                  {this.state.responseMsg.status === "successs" ? (
                    <div className="alert alert-success">
                      {this.state.responseMsg.message}
                    </div>
                  ) : this.state.responseMsg.status === "failed" ? (
                    <div className="alert alert-danger">
                      {this.state.responseMsg.message}
                    </div>
                  ) : (
                    ""
                  )}
                  <div className="card-header">
                    <h4 className="card-title fw-bold">
                      React JS and Python Flask Multiple Image Upload with Show Uploaded Images
                    </h4>
                  </div>
    
                  <div className="card-body">
                    <div className="form-group py-2">
                      <label htmlFor="images">Images</label>
                      <input
                        type="file"
                        name="image"
                        multiple
                        onChange={this.handleChange}
                        className="form-control"
                      />
                      <span className="text-danger">
                        {this.state.responseMsg.error}
                      </span>
                    </div>
                  </div>
    
                  <div className="card-footer">
                    <button type="submit" className="btn btn-success">
                      Upload
                    </button>
                  </div>
                </div>
              </form>
            </div>
          </div>
          <DragAndDrop />
          <Search />
          <Images ref="child" />
        </div>
      );
    }
  }


// upload dataset
// dataset masuk folder
