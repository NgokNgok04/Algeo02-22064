import '../Home.css';
import nnnlogo from "../assets/nnn-logo.png";
export default function Header (){
    return (
        <div className='header'>
            <div className='logo'>
                <img src={nnnlogo} alt = ''></img>
                <p>Nonstop Nubes November</p>
            </div>
            <div className='menu'>
                <p> Reverse Image Search </p>
                <p> How to Use </p>
                <p> About Us </p>
            </div>
        </div>
    )
}