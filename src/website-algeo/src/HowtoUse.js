import './Home.css';
import Header from './components/header.js'
export default function HowToUse() {
  return (
    <div className="HowToUse">
      <Header />
      <div className='detail'>
        <p>1 Masukkan dataset</p>
        <p>2 Masukkan gambar</p>
        <p className='terakhir'>3 Gambar yang mirip akan muncul</p>
      </div>
    </div>
  );
}
