import './Home.css';
import Header from './components/header.js';
import PersonImage from "./assets/person.jpg";
import PersonCard from './components/person-card.js';
export default function AboutUs() {
  return (
    <div className="AboutUs">
      <Header />
      <div className = "PersonCards">
        <PersonCard 
        name = "Matthew" 
        nim = "13522093"
        about = "Ganteng dan Bijaksana"/>
        <PersonCard 
        name = "Devinzen" 
        nim = "13522092"
        about = "test"/>
        <PersonCard 
        name = "Saad" 
        nim = "13522064"
        about = "test"/>
      </div>
    </div>
  );
}
