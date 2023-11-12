import "./person-card.css";
import personCard from "../assets/person.jpg";
export default function PersonCard(props){
    return(
        <div className="PersonCard">
            <img src = {personCard} alt = ""></img>
            <p> {props.name} </p>
            <p class = "nim"> {props.nim} </p>
            <p class =  "about"> " {props.about} "</p>
        </div>
    )
}