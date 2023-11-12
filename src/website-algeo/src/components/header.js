import '../Home.css';
import nnnlogo from "../assets/nnn-logo.png";
import { BrowserRouter as Router, Route, Routes,Link } from 'react-router-dom';
// import styled from "styled-components";
const linkStyle = {
    color: 'white',
    textDecoration: 'none'
}
export default function Header (){
    return (
        <div className='header'>
            <div className='logo'>
                <img src={nnnlogo} alt = ''></img>
                <p>Nonstop Nubes November</p>
            </div>
            <div className='menu'>
                <p> <Link to="/" style = {linkStyle}>Reverse Image Search</Link> </p>
                <p> <Link to="/How-To-Use" style = {linkStyle}>How To Use </Link> </p>
                <p> <Link to="/about" style = {linkStyle}>About</Link> </p>
            </div>
        </div>
    )
}