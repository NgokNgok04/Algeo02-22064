import './Home.css';
import Header from './components/header.js'
import DragAndDropFile from './components/DragAndDrop.js'
import Toggle from './components/Toogle-switch.js';
export default function Program() {
  return (
    <div className="Program">
      <Header />
      <div className='container'>
        <div className='upload'>
          <div className = "upload-image">
            <p> Upload an Image </p>
            {/* <p> Upload Image </p> */}
            <DragAndDropFile />
          </div>

          <div className='button'>
            <div className='text'>
                <p> Warna</p>
                <p> Tekstur</p>
            </div>
            <div className='toggle'> 
              <Toggle />
            </div>

            <div className='search'>
              <button className='search-btn'> Search </button>
            </div>

          </div>
        </div>

      </div>
    </div>
  );
}
