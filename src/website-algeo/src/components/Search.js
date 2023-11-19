import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Search = () => {
  const [imagePaths, setImagePaths] = useState([]);

  const fetchImagePaths = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:5000/similarImages');
      // const data = await response.json();
      const data = response.data.message;
      console.log("test nang",data);
      setImagePaths(data);
      console.log("Data yang diterima",imagePaths);
    } catch (error) {
      console.error('Error fetching image paths:', error);
    }
  };

  return (
    <div>
      <button onClick={fetchImagePaths}>Fetch Images</button>
      {imagePaths.map ((path, index) => (
        <img key = {index} src={path} />
      ))}
    </div>
  );
};

export default Search;
//   const [data, setData] = useState([]);
//   const [loading, setLoading] = useState(false);

//   const handleSearch = async () => {
//     try {
//       setLoading(true);

//       const response = await axios.get('http://127.0.0.1:5000/similarImages');
//       const jsonData = response.data;
//       setData(jsonData);
//     }  catch (error) {
//       console.error('Error bang: ', error.message);

//       if (error.response) {
//         console.error('Response status: ', error.response.status);
//         console.error('Response data: ', error.response.data);
//       }
//     } finally {
//       setLoading(false);
//     }
//   };
  
//   return (
//     <div>
//         <button onClick={handleSearch} className='btn btn-success' disabled={loading}> 
//           {loading ? 'Loading...' : 'Fetch Data'}
//         </button>

//         {data.map((item, index) => (
//         <div key={index}> 
//           <img src={`/api/image?path=${encodeURIComponent(item.image_path)}`} alt={`Image ${index}`} />
//           <p>Similarity Score: {item.similarity_score}</p>
//         </div>
//       ))}

//     </div>
//   )
// }
// export default Search;