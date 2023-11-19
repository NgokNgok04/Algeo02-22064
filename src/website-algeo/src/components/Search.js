import React, { Component } from 'react';
import axios from 'axios';

export default class Search extends Component {

  handleSearch = async () => {
    const formData = new FormData();
    formData.append('file', image);

    console.log(formData);
    var searchType = typeSearch
      ? 'http://localhost:8080/search-texture'
      : 'http://localhost:8080/search-color';

    setWaiting(true);

    try {
      const response = await fetch(searchType, {
        method: 'POST',
        body: formData,
      });
      const data = await response.json();

      const length = data.length;
      console.log('Panjang:', length);

      const endTime = performance.now();
      var temp = endTime - starttime;
      temp = temp / 1000;

      if (temp < 0) {
        temp = 0;
      }
      temp = temp.toFixed(2);
      setTime(temp);
      const lengthData = 'Menemukan ' + length + ' image.';
      Swal(lengthData);

      const responseData = data.data;
      console.log('Data:', responseData);

      // Directly set the state with the fetched data
      setListSimiliarImage(responseData.map((fileImg) => ({ ...fileImg, path: fileImg.path })));
    } catch (error) {
      console.error('Error uploading file', error);
      Swal(error.message || 'Error uploading file');
    } finally {
      console.log('Berhasil');
      setWaiting(false);
    }
  };
    render() {
      return (
        <div>
            <button onClick={handleSearch} className='btn btn-success'> Search </button>

        </div>
    )
  }
}
