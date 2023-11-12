import './Home.css';
import Header from './components/header.js'
import DragAndDropFile from './components/DragAndDrop.js'
export default function Program() {
  return (
    <div className="Program">
      <Header />
      <div className='container'>
        <div className='upload'>
          <div className = "upload-image">
            <p> Upload a File </p>
            {/* <p> Upload Image </p> */}
            <DragAndDropFile />
          </div>

          <div className='button'>
            <div className='text'> </div>
            <div className='toggle'>

            </div>

            {/* <button></button> */}
          </div>
        </div>

        <div className='result'>

        </div>
      </div>
    </div>
  );
}
